from types import SimpleNamespace
from pathlib import Path
import pytest
from src.core import orchestrator
from src.core.infrastructure.models.exceptions import ModelCreationError, ModelNotFoundError


def test_step_load_data_calls_import_data():
    model = SimpleNamespace()
    def import_data(drop_columns, objective_column, test_size):
        return (
            SimpleNamespace(shape=(10, 2)),
            SimpleNamespace(shape=(5, 2)),
            "ytr",
            "yte",
        )

    model.import_data = import_data

    X_train, X_test, y_train, y_test = orchestrator.step_load_data(
        model, {"drop_columns": [], "objective_column": "y"}, 0.25
    )

    assert X_train.shape == (10, 2)
    assert X_test.shape == (5, 2)
    assert y_train == "ytr"
    assert y_test == "yte"


def test_load_model_exits_on_model_not_found(monkeypatch):
    from src.core.infrastructure.models import model_factory

    def raise_not_found(**kwargs):
        raise ModelNotFoundError("a", "classification")

    monkeypatch.setattr(model_factory.ModelFactory, "create", raise_not_found)

    config = {"algo_enum": "a", "dataset_cfg": {"task": "classification", "path": "."}, "dataset_name": "ds"}

    with pytest.raises(SystemExit):
        orchestrator._load_model(config)


def test_load_model_exits_on_model_creation_error(monkeypatch):
    from src.core.infrastructure.models import model_factory

    def raise_creation_error(**kwargs):
        raise ModelCreationError("a", "classification", RuntimeError("boom"))

    monkeypatch.setattr(model_factory.ModelFactory, "create", raise_creation_error)

    config = {"algo_enum": "a", "dataset_cfg": {"task": "classification", "path": "."}, "dataset_name": "ds"}

    with pytest.raises(SystemExit):
        orchestrator._load_model(config)
        

def test_step_fit_invokes_model_fit():
    class M:
        def __init__(self):
            self.fitted = False

        def fit(self, X_train, y_train, X_test, y_test):
            self.fitted = True

    m = M()
    orchestrator.step_fit(m, None, None, None, None)
    assert m.fitted is True


def test_step_plots_merges_paths():
    model = SimpleNamespace()
    model.generate_plots = lambda binary_features: {"a": "p1.png"}
    model.generate_algorithm_specific_plots = lambda: {"b": "p2.png"}

    paths = orchestrator.step_plots(model, {})
    assert paths["a"] == "p1.png"
    assert paths["b"] == "p2.png"


def test_step_shap_calls_explain_with_shap_and_returns_result():
    class FakeX:
        def __init__(self, n):
            self._n = n

        def __len__(self):
            return self._n

        def sample(self, n, random_state=None):
            # return a small sample object acceptable to the explainer
            return ["row1", "row2"]

    model = SimpleNamespace()
    model.X = FakeX(10)

    def explain_with_shap(x_sample, dependence_variable):
        return SimpleNamespace(plot_paths={"shap": "s.png"})

    model.explain_with_shap = explain_with_shap

    result = orchestrator.step_shap(model, {"shap_dependence_variable": ["col"]})
    assert hasattr(result, "plot_paths")
    assert result.plot_paths["shap"] == "s.png"

def test_step_shap_without_dependence_variable_returns_empty_dict():
    model = SimpleNamespace()
    assert orchestrator.step_shap(model, {}) == {}


def test_step_shap_with_dict_result(monkeypatch):
    class FakeX:
        def __len__(self):
            return 1

        def sample(self, n, random_state=None):
            return [1]

    model = SimpleNamespace(X=FakeX())
    model.explain_with_shap = lambda x_sample, dependence_variable: {"plot_paths": {"shap": "p.png"}}

    result = orchestrator.step_shap(model, {"shap_dependence_variable": ["dep"]})
    assert result["plot_paths"]["shap"] == "p.png"


def test_step_export_returns_results_from_model():
    model = SimpleNamespace()
    model.export_results = lambda: {"metrics": {"m": 1}, "plot_dir": "."}

    res = orchestrator.step_export(model)
    assert res["metrics"]["m"] == 1
    assert res["plot_dir"] == "."


def test_step_llm_import_error_returns_empty_dict(monkeypatch):
    import builtins

    original_import = builtins.__import__

    def fake_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name == "src.core.llm.LLMRequestManager":
            raise ImportError("missing")
        return original_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, "__import__", fake_import)

    export_results = {"plot_dir": ".", "metrics_path": "metrics.json", "coefficients_path": "coeff.json"}
    config = {"algo_name": "a", "dataset_cfg": {"task": "classification", "description": "d"}, "algo_info": {"prompt": "p"}}

    assert orchestrator.step_llm(export_results, {}, config) == {}


def test_step_llm_missing_metrics_path_returns_empty_dict(monkeypatch):
    import src.core.llm.LLMRequestManager as mgr

    monkeypatch.setattr(mgr, "analyze_statistics", lambda *args, **kwargs: {"m": "ok"})

    export_results = {"plot_dir": ".", "metrics_path": None, "coefficients_path": None}
    config = {"algo_name": "a", "dataset_cfg": {"task": "classification", "description": "d"}, "algo_info": {"prompt": "p"}}

    assert orchestrator.step_llm(export_results, {}, config) == {}


def test_step_llm_empty_image_dir_still_runs(monkeypatch, tmp_path):
    import src.core.llm.LLMRequestManager as mgr

    called = {}

    def fake_analyze_statistics(**kwargs):
        called["image_path"] = kwargs["image_path"]
        return {"m": "ok"}

    monkeypatch.setattr(mgr, "analyze_statistics", fake_analyze_statistics)

    out_dir = tmp_path / "plots"
    out_dir.mkdir()
    export_results = {"plot_dir": str(out_dir), "metrics_path": str(tmp_path / "metrics.json"), "coefficients_path": str(tmp_path / "coeff.json")}
    config = {"algo_name": "a", "dataset_cfg": {"task": "classification", "description": "d"}, "algo_info": {"prompt": "p"}}

    result = orchestrator.step_llm(export_results, {}, config)
    assert result == {"m": "ok"}
    assert called["image_path"] == []


def test_step_llm_report_write_failure_is_handled(monkeypatch, tmp_path):
    import builtins
    import src.core.llm.LLMRequestManager as mgr

    monkeypatch.setattr(mgr, "analyze_statistics", lambda **kwargs: {"m": "ok"})

    original_open = builtins.open

    def fake_open(file, mode="r", *args, **kwargs):
        if str(file).endswith("LLM_Analysis_Report.md") and "w" in mode:
            raise OSError("disk full")
        return original_open(file, mode, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", fake_open)

    out_dir = tmp_path / "plots"
    out_dir.mkdir()
    export_results = {"plot_dir": str(out_dir), "metrics_path": str(tmp_path / "metrics.json"), "coefficients_path": str(tmp_path / "coeff.json")}
    config = {"algo_name": "a", "dataset_cfg": {"task": "classification", "description": "d"}, "algo_info": {"prompt": "p"}}

    result = orchestrator.step_llm(export_results, {}, config)
    assert result == {"m": "ok"}


def test_run_pipeline_comparative_collects_multiple_results(monkeypatch):
    from src.core.infrastructure.models import model_factory

    monkeypatch.setattr(model_factory.ModelFactory, "get_all_info", lambda a, t: {"prompt": "p"})

    class FakeModel:
        def import_data(self, drop_columns, objective_column, test_size):
            return (SimpleNamespace(shape=(1, 1)), SimpleNamespace(shape=(1, 1)), None, None)

        def fit(self, X_train, y_train, X_test, y_test):
            return None

        def generate_plots(self, binary_features=None):
            return {}

        def generate_algorithm_specific_plots(self):
            return {}

        def explain_with_shap(self, x_sample, dependence_variable):
            return None

        def export_results(self):
            return {"metrics": {"acc": 1.0}, "plot_dir": ".", "metrics_path": str(Path("metrics.json")), "coefficients_path": str(Path("coeff.json"))}

    monkeypatch.setattr(model_factory.ModelFactory, "create", lambda **kwargs: FakeModel())

    config = {
        "analysis_type": orchestrator.AnalysisType.COMPARATIVE,
        "dataset_name": "d",
        "dataset_cfg": {"task": "classification", "path": ".", "drop_columns": [], "objective_column": "y", "description": "desc"},
        "algorithms": ["a1", "a2"],
        "test_size": 0.2,
        "run_shap": False,
        "run_llm": False,
    }

    results = orchestrator.run_pipeline(config)
    assert set(results.keys()) == {"a1", "a2"}


def test_default_pipeline_passthrough_methods(monkeypatch):
    pipeline = orchestrator.DefaultPipeline()

    monkeypatch.setattr(orchestrator, "step_shap", lambda model, dataset_cfg: {"shap": "p.png"})
    monkeypatch.setattr(orchestrator, "step_llm", lambda export_results, plot_paths, config: {"llm": "ok"})

    assert pipeline.shap("model", {}) == {"shap": "p.png"}
    assert pipeline.llm({}, {}, {}) == {"llm": "ok"}
