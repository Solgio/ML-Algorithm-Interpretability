import importlib
import logging
import sys
import traceback
from pathlib import Path
from abc import ABC, abstractmethod
 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)
 
 
def _load_model(algo_info: dict, dataset_name: str, dataset_path: str):
    """
    Importa dinamicamente il modulo e istanzia la classe del modello.
    Usa il registro in selector.ALGORITHMS — nessun import hardcoded.
    """
    module = importlib.import_module(algo_info["module"])
    cls    = getattr(module, algo_info["class"])
    param_grid = algo_info.get("param_grid")
    return cls(dataset=dataset_name, dataset_path=dataset_path, param_grid=param_grid)
 
def step_load_data(model, dataset_cfg: dict, test_size: float):
    log.info("━━  STEP 1: Caricamento dati")
    X_train, X_test, y_train, y_test = model.import_data(
        drop_columns=dataset_cfg["drop_columns"],
        objective_column=dataset_cfg["objective_column"],
        test_size=test_size,
    )
    log.info(f"    Train: {X_train.shape}  |  Test: {X_test.shape}")
    return X_train, X_test, y_train, y_test
 
 
def step_fit(model, X_train, y_train, X_test, y_test):
    log.info("━━  STEP 2: Training")
    model.fit(X_train, y_train, X_test, y_test)
    log.info("    Modello addestrato.")
 
 
def step_plots(model, dataset_cfg: dict):
    log.info("━━  STEP 3: Generazione plot")
    binary_features = dataset_cfg.get("binary_categorical_features", [])
    paths = model.generate_plots(binary_features=binary_features)
    algorithm_specific_paths = model.generate_algorithm_specific_plots()
    paths.update(algorithm_specific_paths)
    log.info(f"    Plot salvati: {list(paths.values())}")
    return paths
 
 
def step_shap(model, dataset_cfg: dict):
    log.info("━━  STEP 4: Analisi SHAP")
    dependence_var = dataset_cfg.get("shap_dependence_variable")
    if dependence_var is None:
        log.warning("    'shap_dependence_variable' non definita nel config — SHAP saltato.")
        return {}
 
    x_sample = model.X.sample(n=min(200, len(model.X)), random_state=42)
    paths = model.SHAP_analysis(x_sample=x_sample, dependence_variable=dependence_var[0])
    log.info(f"    SHAP plot salvati: {list(paths.values())}")
    return paths
 
 
def step_export(model) -> dict:
    log.info("━━  STEP 5: Export risultati")
    results = model.export_results()
    log.info(f"    Metriche  : {results['metrics']}")
    log.info(f"    Output dir: {results['plot_dir']}")
    return results
 
 
def step_llm(export_results: dict, plot_paths: dict, config: dict):
    log.info("━━  STEP 6: Analisi LLM")
    try:
        from llm.LLMRequestManager import analyze_statistics
    except ImportError:
        log.error(f"    Impossibile importare 'test.py'. Assicurati che sia nella stessa cartella.{e}")
        return {}
 
    output_dir = export_results.get("plot_dir")
    image_paths = []
   
    if output_dir:
        p_dir = Path(output_dir)
        image_paths.extend(list(p_dir.glob("*.png")))
       
    if not image_paths:
        log.warning("    Nessuna immagine trovata nella directory di output — l'analisi LLM procederà solo con i dati testuali.")
 
    algo_name =config["algo_name"]
    algo_type = config["dataset_cfg"]["task"]
    dataset_description = config["dataset_cfg"]["description"]
    algo_prompt = config["algo_info"]["prompt"]
 
    metrics_path      = export_results.get("metrics_path")
    coefficients_path = export_results.get("coefficients_path")
    if not metrics_path:
        log.warning("    metrics_path mancante — analisi LLM saltata.")
        return {}
 
    risultati = analyze_statistics(
        metrics_path=metrics_path,
        coefficients_path=coefficients_path or metrics_path,
        image_path=image_paths,
        algo_name=algo_name,
        algo_type=algo_type,
        dataset_description=dataset_description,
        algo_prompt=algo_prompt,        
    )
 
    print("\n" + "═" * 60)
    print("   RISULTATI ANALISI LLM")
    print("═" * 60)
    for modello, risposta in risultati.items():
        print(f"\n[{modello}]\n{risposta}\n{'─' * 60}")
       
    output_dir = export_results.get("plot_dir", ".")
    report_path = Path(output_dir) / "LLM_Analysis_Report.md"
   
    try:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("# Report Analisi Interpretativa LLM\n\n")
           
            for modello, risposta in risultati.items():
                f.write(f"## Modello: `{modello}`\n\n")
                f.write(f"{risposta}\n\n")
                f.write("---\n\n")
               
        log.info(f"    ✔ Report LLM salvato con successo in: {report_path}")
    except Exception as e:
        log.exception(f"    Errore durante il salvataggio del report LLM: {e}")
 
    return risultati
 
 
 
# ------------------------------------------------------------------ #
#  Template Method: Pipeline base class and default implementation   #
# ------------------------------------------------------------------ #
 
 
class BasePipeline(ABC):
    """Template Method pattern: subclasses implement primitive steps.
 
    `run()` defines the pipeline skeleton and calls primitive methods that
    concrete subclasses must implement.
    """
 
    def run(self, config: dict) -> dict:
        dataset_name = config["dataset_name"]
        dataset_path = config["dataset_cfg"]["path"]
        dataset_cfg = config["dataset_cfg"]
        algo_info = config["algo_info"]
        test_size = config.get("test_size", 0.2)
        run_shap = config.get("run_shap", False)
        run_llm = config.get("run_llm", False)
 
        log.info("═" * 60)
        log.info(f"  Pipeline avviata: {config['algo_name']} su '{dataset_name}'")
        log.info("═" * 60)
 
        # primitive operations implemented by subclass
        model = self.load_model(algo_info, dataset_name, dataset_path)
 
        X_train, X_test, y_train, y_test = self.load_data(model, dataset_cfg, test_size)
 
        self.fit(model, X_train, y_train, X_test, y_test)
 
        plot_paths = self.plots(model, dataset_cfg)
 
        shap_paths = {}
        if run_shap:
            shap_paths = self.shap(model, dataset_cfg)
 
        export_res = self.export(model)
 
        llm_results = {}
        if run_llm:
            all_plot_paths = {**plot_paths, **shap_paths}
            llm_results = self.llm(export_res, all_plot_paths, config)
 
        log.info("═" * 60)
        log.info("  Pipeline completata con successo.")
        log.info("═" * 60)
 
        return {
            "model": model,
            "plot_paths": {**plot_paths, **shap_paths},
            "export": export_res,
            "llm_results": llm_results,
        }
 
    @abstractmethod
    def load_model(self, algo_info: dict, dataset_name: str, dataset_path: str):
        raise NotImplementedError()
 
    @abstractmethod
    def load_data(self, model, dataset_cfg: dict, test_size: float):
        raise NotImplementedError()
 
    @abstractmethod
    def fit(self, model, X_train, y_train, X_test, y_test):
        raise NotImplementedError()
 
    @abstractmethod
    def plots(self, model, dataset_cfg: dict):
        raise NotImplementedError()
 
    @abstractmethod
    def shap(self, model, dataset_cfg: dict):
        raise NotImplementedError()
 
    @abstractmethod
    def export(self, model) -> dict:
        raise NotImplementedError()
 
    @abstractmethod
    def llm(self, export_results: dict, plot_paths: dict, config: dict):
        raise NotImplementedError()
 
 
class DefaultPipeline(BasePipeline):
    """Default pipeline that delegates to the module-level helper functions.
 
    This keeps the procedural helpers (step_*) while exposing an explicit
    Template Method for easier extension and testing.
    """
 
    def load_model(self, algo_info: dict, dataset_name: str, dataset_path: str):
        return _load_model(algo_info, dataset_name, dataset_path)
 
    def load_data(self, model, dataset_cfg: dict, test_size: float):
        return step_load_data(model, dataset_cfg, test_size)
 
    def fit(self, model, X_train, y_train, X_test, y_test):
        return step_fit(model, X_train, y_train, X_test, y_test)
 
    def plots(self, model, dataset_cfg: dict):
        return step_plots(model, dataset_cfg)
 
    def shap(self, model, dataset_cfg: dict):
        return step_shap(model, dataset_cfg)
 
    def export(self, model) -> dict:
        return step_export(model)
 
    def llm(self, export_results: dict, plot_paths: dict, config: dict):
        return step_llm(export_results, plot_paths, config)
 
 
def run_pipeline(config: dict) -> dict:
    """Backward-compatible wrapper that runs the default pipeline."""
    pipeline = DefaultPipeline()
    return pipeline.run(config)
 
 
# ------------------------------------------------------------------ #
#  Entry point                                                         #
# ------------------------------------------------------------------ #
 
if __name__ == "__main__":
    try:
        from selector import run_selector
        config = run_selector()
        run_pipeline(config)
    except KeyboardInterrupt:
        print("\n\n  Interrotto dall'utente.")
        sys.exit(0)
    except Exception:
        log.error("Errore critico nella pipeline:")
        traceback.print_exc()
        sys.exit(1)