from types import  SimpleNamespace
import pandas as pd
from src.core.infrastructure.explainers.base import Explainer

class DummyExplainer(Explainer):
    def _compute_shap_values(self, x_sample: pd.DataFrame):
        return SimpleNamespace(base_values=0.5)

    def _generate_plots(self, shap_values, x_sample: pd.DataFrame, dependence_variable: str):
        return {"plot": "plot.png"}


def test_base_explainer_explain_and_helpers(tmp_path):
    model = SimpleNamespace()
    explainer = DummyExplainer(model=model, x_train=pd.DataFrame({"a": [1, 2]}))
    explainer.plot_dir = str(tmp_path / "plots")

    result = explainer.explain(pd.DataFrame({"a": [1]}), "a")
    assert result.base_value == 0.5
    assert result.feature_names == ["a"]
    assert result.plot_paths == {"plot": "plot.png"}

    assert explainer._ensure_plot_dir() == str(tmp_path / "plots")
    assert explainer._extract_base_model() is model


def test_base_explainer_extracts_pipeline_base_model():
    from sklearn.pipeline import Pipeline

    class BaseModel:
        pass

    pipeline = Pipeline([("step1", object()), ("final", BaseModel())])
    explainer = DummyExplainer(model=pipeline, x_train=pd.DataFrame({"a": [1]}))

    assert isinstance(explainer._extract_base_model(), BaseModel)