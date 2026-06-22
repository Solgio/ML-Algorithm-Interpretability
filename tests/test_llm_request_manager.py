import os
import base64
import json
from pathlib import Path
from types import SimpleNamespace

import pandas as pd
import pytest

os.environ.setdefault("OPENAI_API_KEY", "test-key-for-coverage")

from src.core.llm import LLMRequestManager as llm_mgr


@pytest.mark.parametrize(
    "factory,expected",
    [
        (lambda p: p.with_suffix(".json"), '{\n  "a": 1\n}'),
        (lambda p: p.with_suffix(".csv"), "a\n1"),
        (lambda p: p.with_suffix(".txt"), "Nessuna metrica testuale disponibile."),
    ],
)
def test_load_metrics_branches(tmp_path, factory, expected):
    target = factory(tmp_path / "metrics")
    if target.suffix == ".json":
        target.write_text(json.dumps({"a": 1}))
    elif target.suffix == ".csv":
        pd.DataFrame({"a": [1]}).to_csv(target, index=False)

    result = llm_mgr.load_metrics(target)
    if target.suffix == ".csv":
        assert "a" in result and "1" in result
    else:
        assert expected in result


@pytest.mark.parametrize(
    "factory,expected",
    [
        (lambda p: p.with_suffix(".json"), '{\n  "b": 2\n}'),
        (lambda p: p.with_suffix(".csv"), "b\n2"),
        (lambda p: p.with_suffix(".txt"), "Nessun coefficiente testuale disponibile."),
    ],
)
def test_load_coefficients_branches(tmp_path, factory, expected):
    target = factory(tmp_path / "coefficients")
    if target.suffix == ".json":
        target.write_text(json.dumps({"b": 2}))
    elif target.suffix == ".csv":
        pd.DataFrame({"b": [2]}).to_csv(target, index=False)

    result = llm_mgr.load_coefficients(target)
    if target.suffix == ".csv":
        assert "b" in result and "2" in result
    else:
        assert expected in result


def test_encode_image_success_and_missing(tmp_path):
    image = tmp_path / "image.bin"
    image.write_bytes(b"abc")

    encoded = llm_mgr.encode_image([image])
    assert encoded == [base64.b64encode(b"abc").decode("utf-8")]

    with pytest.raises(FileNotFoundError):
        llm_mgr.encode_image([tmp_path / "missing.png"])


def test_fetch_model_response_success_and_error(monkeypatch):
    class FakeResponse:
        choices = [SimpleNamespace(message=SimpleNamespace(content="ok"))]

    fake_client = SimpleNamespace(
        chat=SimpleNamespace(
            completions=SimpleNamespace(create=lambda **kwargs: FakeResponse())
        )
    )
    monkeypatch.setattr(llm_mgr, "client", fake_client)

    model, content = llm_mgr.fetch_model_response("m", "system", "prompt", ["img"])
    assert model == "m"
    assert content == "ok"

    def raise_error(**kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr(
        llm_mgr,
        "client",
        SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=raise_error))),
    )
    model, content = llm_mgr.fetch_model_response("m2", "system", "prompt", [])
    assert model == "m2"
    assert "Errore:" in content


def test_analyze_statistics_uses_executor_and_collects_results(monkeypatch, tmp_path):
    metrics = tmp_path / "metrics.json"
    coefficients = tmp_path / "coefficients.json"
    image = tmp_path / "plot.png"
    metrics.write_text(json.dumps({"acc": 1.0}))
    coefficients.write_text(json.dumps({"coef": 2.0}))
    image.write_bytes(b"png")

    monkeypatch.setattr(llm_mgr, "model_list_img_supp", ["model-a"])
    monkeypatch.setattr(llm_mgr, "fetch_model_response", lambda *args, **kwargs: ("model-a", "result"))

    class FakeFuture:
        def __init__(self, value):
            self._value = value

        def result(self):
            return self._value

    class FakeExecutor:
        def __init__(self, max_workers):
            self.max_workers = max_workers

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def submit(self, fn, *args, **kwargs):
            return FakeFuture(("model-a", "result"))

    monkeypatch.setattr(llm_mgr.concurrent.futures, "ThreadPoolExecutor", FakeExecutor)
    monkeypatch.setattr(llm_mgr.concurrent.futures, "as_completed", lambda futures: list(futures.keys()))

    results = llm_mgr.analyze_statistics(
        metrics_path=metrics,
        coefficients_path=coefficients,
        image_path=[image],
        algo_name="algo",
        algo_type="classification",
        dataset_description="desc",
        algo_prompt="prompt",
    )

    assert results == {"model-a": "result"}


def test_analyze_statistics_handles_future_exception(monkeypatch, tmp_path):
    metrics = tmp_path / "metrics.json"
    coefficients = tmp_path / "coefficients.json"
    image = tmp_path / "plot.png"
    metrics.write_text(json.dumps({"acc": 1.0}))
    coefficients.write_text(json.dumps({"coef": 2.0}))
    image.write_bytes(b"png")

    monkeypatch.setattr(llm_mgr, "model_list_img_supp", ["model-a"])

    class FailingFuture:
        def result(self):
            raise RuntimeError("boom")

    class FakeExecutor:
        def __init__(self, max_workers):
            self.max_workers = max_workers

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def submit(self, fn, *args, **kwargs):
            return FailingFuture()

    monkeypatch.setattr(llm_mgr.concurrent.futures, "ThreadPoolExecutor", FakeExecutor)
    monkeypatch.setattr(llm_mgr.concurrent.futures, "as_completed", lambda futures: list(futures.keys()))

    results = llm_mgr.analyze_statistics(
        metrics_path=metrics,
        coefficients_path=coefficients,
        image_path=[image],
        algo_name="algo",
        algo_type="classification",
        dataset_description="desc",
        algo_prompt="prompt",
    )

    assert results == {"model-a": "Errore: boom"}
