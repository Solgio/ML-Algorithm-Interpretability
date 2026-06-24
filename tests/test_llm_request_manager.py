import os
import base64
import json
from pathlib import Path
from types import SimpleNamespace

import pandas as pd
import pytest

from src.core.llm import LLMRequestManager as llm_mgr
from src.core.llm.interfaces import LLMService, OrchestrationStrategy
from src.core.llm.services import DataPreparationService, PromptBuilder, OpenAILLMService
from src.core.llm.strategies import AlgorithmWiseStrategy, LLMWiseStrategy
from src.core.llm.orchestrator_context import LLMOrchestrator

os.environ.setdefault("OPENAI_API_KEY", "test-key-for-coverage")


# --- DataPreparationService Tests ---

@pytest.mark.parametrize(
    "suffix,content,expected_assertion",
    [
        (".json", '{"a": 1}', lambda res: "a" in res and "1" in res),
        (".csv", "a\n1", lambda res: "a" in res and "1" in res),
        (".txt", "plain text", lambda res: "No textual metrics available." in res),
    ],
)
def test_load_metrics_branches(tmp_path, suffix, content, expected_assertion):
    target = tmp_path / f"metrics{suffix}"
    if suffix == ".json":
        target.write_text(content)
    elif suffix == ".csv":
        pd.DataFrame({"a": [1]}).to_csv(target, index=False)
    else:
        target.write_text(content)

    result = DataPreparationService.load_metrics(str(target))
    assert expected_assertion(result)


def test_load_metrics_missing_and_empty():
    assert DataPreparationService.load_metrics(None) == "No metrics path provided."
    assert DataPreparationService.load_metrics("") == "No metrics path provided."
    assert DataPreparationService.load_metrics("non_existent_file.json") == "Metrics file not found."


@pytest.mark.parametrize(
    "suffix,content,expected_assertion",
    [
        (".json", '{"b": 2}', lambda res: "b" in res and "2" in res),
        (".csv", "b\n2", lambda res: "b" in res and "2" in res),
        (".txt", "plain text", lambda res: "No textual coefficients available." in res),
    ],
)
def test_load_coefficients_branches(tmp_path, suffix, content, expected_assertion):
    target = tmp_path / f"coefficients{suffix}"
    if suffix == ".json":
        target.write_text(content)
    elif suffix == ".csv":
        pd.DataFrame({"b": [2]}).to_csv(target, index=False)
    else:
        target.write_text(content)

    result = DataPreparationService.load_coefficients(str(target))
    assert expected_assertion(result)


def test_load_coefficients_missing_and_empty():
    assert DataPreparationService.load_coefficients(None) == "No coefficients path provided."
    assert DataPreparationService.load_coefficients("") == "No coefficients path provided."
    assert DataPreparationService.load_coefficients("non_existent_file.json") == "Coefficients file not found."


def test_encode_images_success_and_missing(tmp_path):
    image = tmp_path / "image.png"
    image.write_bytes(b"abc")

    encoded = DataPreparationService.encode_images([str(image)])
    assert encoded == [base64.b64encode(b"abc").decode("utf-8")]

    with pytest.raises(FileNotFoundError):
        DataPreparationService.encode_images([str(tmp_path / "missing.png")])


# --- PromptBuilder Tests ---

def test_prompt_builder():
    prompt = PromptBuilder.build_prompt(
        algo_name="LR",
        algo_type="regression",
        dataset_description="desc",
        user_prompt="user expect",
        algo_prompt="algo instruct",
        raw_metrics="metrics raw",
        raw_coefficients="coefficients raw",
        general_prompt="general instruct"
    )
    assert "ALGORITHM: LR" in prompt
    assert "Algorithm type: regression" in prompt
    assert "Dataset description: desc" in prompt
    assert "User expectations: user expect" in prompt
    assert "metrics raw" in prompt
    assert "coefficients raw" in prompt
    assert "algo instruct" in prompt
    assert "general instruct" in prompt


# --- OpenAILLMService Tests ---

def test_openai_llm_service_success_and_error(monkeypatch):
    class FakeResponse:
        choices = [SimpleNamespace(message=SimpleNamespace(content="ok"))]

    fake_client = SimpleNamespace(
        chat=SimpleNamespace(
            completions=SimpleNamespace(create=lambda **kwargs: FakeResponse())
        )
    )
    
    service = OpenAILLMService(client=fake_client)
    content = service.generate_response("m", "system", "prompt", ["img"])
    assert content == "ok"

    def raise_error(**kwargs):
        raise RuntimeError("boom")

    service_error = OpenAILLMService(
        client=SimpleNamespace(
            chat=SimpleNamespace(completions=SimpleNamespace(create=raise_error))
        )
    )
    content_error = service_error.generate_response("m2", "system", "prompt", [])
    assert "Error: boom" in content_error


# --- Strategies and Orchestrator Tests ---

class MockLLMService(LLMService):
    def __init__(self):
        self.calls = []

    def generate_response(self, model, system_prompt, user_prompt, images=None):
        self.calls.append((model, system_prompt, user_prompt, images))
        return f"resp-{model}"


def test_algorithm_wise_strategy(tmp_path):
    metrics = tmp_path / "metrics.json"
    metrics.write_text(json.dumps({"acc": 1.0}))
    
    task = {
        "algo_name": "LR",
        "algo_type": "regression",
        "dataset_description": "desc",
        "user_prompt": "user expect",
        "algo_prompt": "algo instruct",
        "metrics_path": str(metrics),
        "coefficients_path": str(metrics),
        "image_paths": []
    }
    
    service = MockLLMService()
    strategy = AlgorithmWiseStrategy()
    results = strategy.execute([task], ["model-a", "model-b"], service)
    
    assert results == {"LR": {"model-a": "resp-model-a", "model-b": "resp-model-b"}}
    assert len(service.calls) == 2
    assert service.calls[0][0] == "model-a"
    assert service.calls[1][0] == "model-b"


def test_llm_wise_strategy(tmp_path):
    metrics = tmp_path / "metrics.json"
    metrics.write_text(json.dumps({"acc": 1.0}))
    
    task1 = {
        "algo_name": "LR",
        "algo_type": "regression",
        "dataset_description": "desc",
        "user_prompt": "user expect",
        "algo_prompt": "algo instruct",
        "metrics_path": str(metrics),
        "coefficients_path": str(metrics),
        "image_paths": []
    }
    task2 = {
        "algo_name": "SVM",
        "algo_type": "classification",
        "dataset_description": "desc2",
        "user_prompt": None,
        "algo_prompt": "algo instruct2",
        "metrics_path": str(metrics),
        "coefficients_path": str(metrics),
        "image_paths": []
    }
    
    service = MockLLMService()
    strategy = LLMWiseStrategy()
    results = strategy.execute([task1, task2], ["model-a"], service)
    
    assert results == {
        "LR": {"model-a": "resp-model-a"},
        "SVM": {"model-a": "resp-model-a"}
    }
    assert len(service.calls) == 2
    assert service.calls[0][0] == "model-a"
    assert "ALGORITHM: LR" in service.calls[0][2]
    assert service.calls[1][0] == "model-a"
    assert "ALGORITHM: SVM" in service.calls[1][2]


def test_llm_orchestrator():
    class DummyStrategy(OrchestrationStrategy):
        def execute(self, tasks, models, llm_service):
            return {"strategy": type(self).__name__}

    strategy = DummyStrategy()
    service = MockLLMService()
    orchestrator = LLMOrchestrator(strategy, service)
    
    assert orchestrator.strategy is strategy
    assert orchestrator.llm_service is service
    
    new_strategy = DummyStrategy()
    new_service = MockLLMService()
    orchestrator.strategy = new_strategy
    orchestrator.llm_service = new_service
    assert orchestrator.strategy is new_strategy
    assert orchestrator.llm_service is new_service
    
    assert orchestrator.run([], []) == {"strategy": "DummyStrategy"}


# --- Legacy Facade Tests ---

def test_legacy_facade_analyze_statistics(monkeypatch, tmp_path):
    metrics = tmp_path / "metrics.json"
    metrics.write_text(json.dumps({"acc": 1.0}))
    
    called_run = []
    class MockOrchestrator:
        def __init__(self, strategy, service):
            pass
        def run(self, tasks, models):
            called_run.append((tasks, models))
            return {"LR": {"model-a": "facade-response"}}
            
    monkeypatch.setattr("src.core.llm.LLMRequestManager.LLMOrchestrator", MockOrchestrator)
    
    res = llm_mgr.analyze_statistics(
        metrics_path=str(metrics),
        coefficients_path=None,
        image_path=[],
        algo_name="LR",
        algo_type="regression",
        dataset_description="desc",
        user_prompt="user expect",
        algo_prompt="algo instruct",
        model_list=["model-a"]
    )
    
    assert res == {"model-a": "facade-response"}
    assert len(called_run) == 1
    assert called_run[0][0][0]["algo_name"] == "LR"
    assert called_run[0][1] == ["model-a"]


def test_legacy_facade_analyze_statistics_llm_wise(monkeypatch, tmp_path):
    metrics = tmp_path / "metrics.json"
    metrics.write_text(json.dumps({"acc": 1.0}))
    
    called_run = []
    class MockOrchestrator:
        def __init__(self, strategy, service):
            pass
        def run(self, tasks, models):
            called_run.append((tasks, models))
            return {"LR": {"model-a": "facade-response"}}
            
    monkeypatch.setattr("src.core.llm.LLMRequestManager.LLMOrchestrator", MockOrchestrator)
    
    tasks = [{
        "algo_name": "LR",
        "algo_type": "regression",
        "dataset_description": "desc",
        "user_prompt": "user expect",
        "algo_prompt": "algo instruct",
        "metrics_path": str(metrics),
        "coefficients_path": None,
        "image_paths": None
    }]
    
    res = llm_mgr.analyze_statistics_llm_wise(tasks, ["model-a"])
    
    assert res == {"LR": {"model-a": "facade-response"}}
    assert len(called_run) == 1
    assert called_run[0][0][0]["algo_name"] == "LR"
    assert called_run[0][1] == ["model-a"]


def test_openai_llm_service_with_dict_images():
    class FakeResponse:
        choices = [SimpleNamespace(message=SimpleNamespace(content="ok"))]

    created_payloads = []
    class FakeCompletions:
        def create(self, **kwargs):
            created_payloads.append(kwargs)
            return FakeResponse()

    fake_client = SimpleNamespace(
        chat=SimpleNamespace(
            completions=FakeCompletions()
        )
    )
    
    service = OpenAILLMService(client=fake_client)
    
    images_input = [
        {"name": "correlation_matrix.png", "base64": "abc"},
        {"name": "photo.jpeg", "base64": "def"}
    ]
    content = service.generate_response("m", "system", "prompt", images_input)
    assert content == "ok"
    assert len(created_payloads) == 1
    
    messages = created_payloads[0]["messages"]
    user_content = messages[1]["content"]
    
    # 1 prompt text, plus 2 texts and 2 images = 5 elements total
    assert len(user_content) == 5
    assert user_content[0]["text"] == "prompt"
    
    # First image assertions
    assert user_content[1]["type"] == "text"
    assert "Attached Graph/Plot: correlation_matrix.png" in user_content[1]["text"]
    assert user_content[2]["type"] == "image_url"
    assert user_content[2]["image_url"]["url"] == "data:image/png;base64,abc"
    
    # Second image assertions
    assert user_content[3]["type"] == "text"
    assert "Attached Graph/Plot: photo.jpeg" in user_content[3]["text"]
    assert user_content[4]["type"] == "image_url"
    assert user_content[4]["image_url"]["url"] == "data:image/jpeg;base64,def"

