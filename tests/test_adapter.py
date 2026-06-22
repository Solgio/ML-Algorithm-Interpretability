from types import  SimpleNamespace
import pandas as pd
import pytest
from src.core.domain.enums import Algorithm, TaskType
from src.core.infrastructure.explainers.adapter import SHAPAnalyzerAdapter
from src.core.infrastructure.explainers.strategy import ExplainerStrategy


def test_adapter_candidate_names_and_alias_extraction():
    class LinearRegression:
        pass

    class Wrapped:
        def __init__(self):
            self.model = LinearRegression()
            self.estimator = SimpleNamespace()

    adapter = SHAPAnalyzerAdapter(model=Wrapped(), x_train=pd.DataFrame({"a": [1]}), plot_dir=".", task_type=TaskType.CLASSIFICATION)
    names = list(adapter._candidate_model_class_names(adapter.model))
    assert names[0] == "Wrapped"
    assert "SimpleNamespace" in names

    assert adapter._extract_model_type() == Algorithm.LINEAR_REGRESSION


def test_adapter_create_explainer_and_explain_flow(monkeypatch, tmp_path):
    class FakeExplainer:
        def __init__(self, model, x_train):
            self.model = model
            self.x_train = x_train
            self.plot_dir = None

        def explain(self, x_sample, dependence_variable):
            return SimpleNamespace(plot_paths={"plot": "ok.png"})

    monkeypatch.setattr(
        "src.core.infrastructure.explainers.adapter.select_explainer_strategy",
        lambda algorithm, task_type: ExplainerStrategy.KERNEL,
    )
    monkeypatch.setitem(SHAPAnalyzerAdapter._EXPLAINER_MAP, ExplainerStrategy.KERNEL, FakeExplainer)

    model = SimpleNamespace()
    model.model = SimpleNamespace()
    adapter = SHAPAnalyzerAdapter(model=model, x_train=pd.DataFrame({"a": [1, 2]}), plot_dir=str(tmp_path), task_type=TaskType.REGRESSION)
    monkeypatch.setattr(adapter, "_extract_model_type", lambda: Algorithm.LINEAR_REGRESSION)

    x_sample = pd.DataFrame({"a": [1, 2]})
    result = adapter.explain(x_sample, "a")
    assert result.plot_paths == {"plot": "ok.png"}


def test_adapter_explain_rejects_non_dataframe(monkeypatch):
    adapter = SHAPAnalyzerAdapter(model=SimpleNamespace(model=SimpleNamespace()), x_train=pd.DataFrame({"a": [1]}), plot_dir=".", task_type=TaskType.REGRESSION)
    monkeypatch.setattr(adapter, "_extract_model_type", lambda: Algorithm.LINEAR_REGRESSION)
    monkeypatch.setattr(
        "src.core.infrastructure.explainers.adapter.select_explainer_strategy",
        lambda algorithm, task_type: ExplainerStrategy.KERNEL,
    )

    class FakeExplainer:
        def __init__(self, model, x_train):
            self.plot_dir = None

        def explain(self, x_sample, dependence_variable):
            return SimpleNamespace(plot_paths={})

    monkeypatch.setitem(SHAPAnalyzerAdapter._EXPLAINER_MAP, ExplainerStrategy.KERNEL, FakeExplainer)

    with pytest.raises(TypeError):
        adapter.explain([1, 2, 3], "a")


def test_adapter_extract_model_type_unknown_raises():
    adapter = SHAPAnalyzerAdapter(model=SimpleNamespace(), x_train=pd.DataFrame({"a": [1]}), plot_dir=".", task_type=TaskType.CLASSIFICATION)

    with pytest.raises(ValueError):
        adapter._extract_model_type()


def test_adapter_create_explainer_rejects_unsupported_strategy():
    adapter = SHAPAnalyzerAdapter(model=SimpleNamespace(), x_train=pd.DataFrame({"a": [1]}), plot_dir=".", task_type=TaskType.CLASSIFICATION)

    with pytest.raises(ValueError):
        adapter._create_explainer(object())

