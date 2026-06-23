import sys
from types import SimpleNamespace
from pathlib import Path

import pytest

from src.core import orchestrator


def test_step_llm_invokes_analyze_and_writes_report(monkeypatch, tmp_path):
    called = {}

    def fake_run(self, tasks, models):
        called['invoked'] = True
        return {"a": {"model1": "analysis text"}}
    monkeypatch.setenv("OPENAI_API_KEY", "fake-test-key-123")

    monkeypatch.setattr("src.core.llm.orchestrator_context.LLMOrchestrator.run", fake_run)

    out_dir = tmp_path / "out"
    out_dir.mkdir()
    img = out_dir / "plot1.png"
    img.write_text("png")

    export_results = {
        "plot_dir": str(out_dir),
        "metrics_path": str(tmp_path / "metrics.json"),
        "coefficients_path": None,
    }

    config = {
        "algo_name": "a",
        "dataset_cfg": {"task": "classification", "description": "desc"},
        "algo_info": {"prompt": "p"},
        "user_prompt": None,
    }

    res = orchestrator.step_llm(export_results, {}, config)
    assert called.get('invoked', False) is True

    report = Path(out_dir) / "LLM_Analysis_Report.md"
    assert report.exists()


def test_run_pipeline_continues_on_algorithm_error(monkeypatch):
    from src.core.infrastructure.models import model_factory

    monkeypatch.setattr(model_factory.ModelFactory, 'get_all_info', lambda a, t: {"prompt": "p"})

    class FakeModel:
        def import_data(self, drop_columns, objective_column, test_size):
            return (SimpleNamespace(shape=(1, 1)), SimpleNamespace(shape=(1, 1)), None, None)

        def fit(self, X_train, y_train, X_test, y_test):
            self.fitted = True

        def generate_plots(self, binary_features=None):
            return {"p": "x.png"}

        def generate_algorithm_specific_plots(self):
            return {}

        def explain_with_shap(self, x_sample, dependence_variable):
            return None

        def export_results(self):
            return {"metrics": {"acc": 0.9}, "plot_dir": ".", "metrics_path": None, "coefficients_path": None}

    def fake_create(algorithm, task_type, dataset, dataset_path):
        if str(algorithm) == "bad":
            raise Exception("creation failed")
        return FakeModel()

    monkeypatch.setattr(model_factory.ModelFactory, 'create', fake_create)

    config = {
        "analysis_type": orchestrator.AnalysisType.COMPARATIVE,
        "dataset_name": "d",
        "dataset_cfg": {"task": "classification", "path": ".", "drop_columns": [], "objective_column": "y"},
        "algorithms": ["bad", "good"],
        "test_size": 0.2,
        "run_shap": False,
        "run_llm": False,
    }

    results = orchestrator.run_pipeline(config)
    assert "good" in results
    assert "bad" not in results
