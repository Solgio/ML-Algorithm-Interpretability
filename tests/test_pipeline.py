from src.core.orchestrator import BasePipeline


class DummyPipeline(BasePipeline):
    def load_model(self, config):
        return "model_obj"

    def load_data(self, model, dataset_cfg, test_size):
        return (None, None, None, None)

    def fit(self, model, X_train, y_train, X_test, y_test):
        self.fitted = True

    def plots(self, model, dataset_cfg):
        return {'p': 'path.png'}

    def shap(self, model, dataset_cfg):
        return {}

    def export(self, model):
        return {'metrics': {'acc': 1.0}, 'plot_dir': '.'}

    def llm(self, export_results, plot_paths, config):
        return {'llm': 'ok'}


def test_base_pipeline_run():
    pipeline = DummyPipeline()
    config = {
        "dataset_name": "dummy",
        "dataset_cfg": {"task": "classification"},
        "test_size": 0.2,
        "run_shap": False,
        "run_llm": False,
        "algo_name": "dummy_algo",
    }

    out = pipeline.run(config)

    assert out['model'] == "model_obj"
    assert 'plot_paths' in out
    assert out['export']['metrics']['acc'] == 1.0


def test_base_pipeline_run_merges_dict_shap_and_calls_llm():
    class DictShapPipeline(BasePipeline):
        def load_model(self, config):
            return "model_obj"

        def load_data(self, model, dataset_cfg, test_size):
            return (None, None, None, None)

        def fit(self, model, X_train, y_train, X_test, y_test):
            return None

        def plots(self, model, dataset_cfg):
            return {"plot": "base.png"}

        def shap(self, model, dataset_cfg):
            return {"shap": "dict.png"}

        def export(self, model):
            return {'metrics': {'acc': 1.0}, 'plot_dir': '.'}

        def llm(self, export_results, plot_paths, config):
            self.llm_called = True
            self.llm_plot_paths = plot_paths
            return {'llm': 'ok'}

    pipeline = DictShapPipeline()
    config = {
        "dataset_name": "dummy",
        "dataset_cfg": {"task": "classification"},
        "test_size": 0.2,
        "run_shap": True,
        "run_llm": True,
        "algo_name": "dummy_algo",
    }

    out = pipeline.run(config)

    assert out['plot_paths'] == {'plot': 'base.png', 'shap': 'dict.png'}
    assert out['llm_results'] == {'llm': 'ok'}
    assert pipeline.llm_called is True
    assert pipeline.llm_plot_paths == {'plot': 'base.png', 'shap': 'dict.png'}


def test_base_pipeline_run_uses_plot_paths_from_shap_object():
    class ObjectShapPipeline(BasePipeline):
        def load_model(self, config):
            return "model_obj"

        def load_data(self, model, dataset_cfg, test_size):
            return (None, None, None, None)

        def fit(self, model, X_train, y_train, X_test, y_test):
            return None

        def plots(self, model, dataset_cfg):
            return {}

        def shap(self, model, dataset_cfg):
            return type("ShapResult", (), {"plot_paths": {"shap": "obj.png"}})()

        def export(self, model):
            return {'metrics': {'acc': 1.0}, 'plot_dir': '.'}

        def llm(self, export_results, plot_paths, config):
            return {}

    pipeline = ObjectShapPipeline()
    config = {
        "dataset_name": "dummy",
        "dataset_cfg": {"task": "classification"},
        "test_size": 0.2,
        "run_shap": True,
        "run_llm": False,
        "algo_name": "dummy_algo",
    }

    out = pipeline.run(config)

    assert out['plot_paths'] == {'shap': 'obj.png'}
