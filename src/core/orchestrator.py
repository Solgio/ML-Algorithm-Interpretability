import importlib
import logging
import os
import sys   
import traceback
from pathlib import Path
from dotenv import load_dotenv
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from src.core.domain.enums import Algorithm, AnalysisType, TaskType
from src.core.infrastructure.models.model_factory import ModelFactory
from src.core.infrastructure.models.exceptions import ModelNotFoundError, ModelCreationError

from src.core.infrastructure.models.registry_initializer import initialize_model_registry
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parents[1]
env_path = project_root / '.env'
load_dotenv(dotenv_path=env_path)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)
 
def _load_model(config: dict):
    """
    Dynamically import the model class based on the provided algorithm information and instantiate it.
    """
    algorithm = config["algo_enum"]
    task_type = config["dataset_cfg"]["task"]
    dataset_name = config["dataset_name"]
    dataset_path = config["dataset_cfg"]["path"]
    
    try:
        log.info(f"Creating model: {algorithm} ({task_type})")
        
        model = ModelFactory.create(
            algorithm=algorithm,
            task_type=task_type,
            dataset=dataset_name,
            dataset_path=dataset_path
        )
        
        log.info(f"✓ Model created: {type(model).__name__}")
        return model
    
    except ModelNotFoundError as e:
        log.exception(f"Algorithm not found: {e}")
        print(f"\n✗ ERROR: {e}")
        sys.exit(1)
    except ModelCreationError as e:
        log.exception(f"Error creating model: {e}")
        print(f"\n✗ ERROR: {e}")
        sys.exit(1)
 
def step_load_data(model, dataset_cfg: dict, test_size: float):
    log.info("━━  STEP 1: Loading data")
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
    log.info("    Model trained.")
 
 
def step_plots(model, dataset_cfg: dict):
    log.info("━━  STEP 3: Plot generation")
    binary_features = dataset_cfg.get("binary_categorical_features", [])
    paths = model.generate_plots(binary_features=binary_features)
    algorithm_specific_paths = model.generate_algorithm_specific_plots()
    paths.update(algorithm_specific_paths)
    log.info(f"    Plots saved: {list(paths.values())}")
    return paths
 
 
def step_shap(model, dataset_cfg: dict):
    log.info("━━  STEP 4: SHAP analysis")
    dependence_var = dataset_cfg.get("shap_dependence_variable")
    if dependence_var is None:
        log.warning("    'shap_dependence_variable' not defined in config — SHAP skipped.")
        return {}
 
    x_sample = model.X.sample(n=min(200, len(model.X)), random_state=42)
    result = model.explain_with_shap(x_sample=x_sample, dependence_variable=dependence_var[0])
    plot_paths = getattr(result, 'plot_paths', {}) if result is not None else {}
    log.info(f"    SHAP plots saved: {list(plot_paths.values())}")
    return result
 
 
def step_export(model) -> dict:
    log.info("━━  STEP 5: Results export")
    results = model.export_results()
    log.info(f"    Metrics   : {results['metrics']}")
    log.info(f"    Output dir: {results['plot_dir']}")
    return results
 
 
def step_llm(export_results: dict, plot_paths: dict, config: dict):
    log.info("━━  STEP 6: LLM analysis")
    try:
        from src.core.llm.services import OpenAILLMService
        from src.core.llm.strategies import AlgorithmWiseStrategy
        from src.core.llm.orchestrator_context import LLMOrchestrator
        from src.core.llm.LLMDataWarehouse import model_list_img_supp
    except ImportError as e:
        log.exception(f"    Failed to import LLM components: {e}")
        return {}
 
    output_dir = export_results.get("plot_dir")
    image_paths = []
   
    if output_dir:
        p_dir = Path(output_dir)
        image_paths.extend(list(p_dir.glob("*.png")))
       
    if not image_paths:
        log.warning("    No images found in output directory — LLM analysis will proceed with textual data only.")
 
    algo_name =config["algo_name"]
    algo_type = config["dataset_cfg"]["task"]
    dataset_description = config["dataset_cfg"]["description"]
    user_prompt = config["user_prompt"]
    algo_prompt = config["algo_info"]["prompt"]
 
    metrics_path      = export_results.get("metrics_path")
    coefficients_path = export_results.get("coefficients_path")
    if not metrics_path:
        log.warning("    metrics_path missing — LLM analysis skipped.")
        return {}
 
    task = {
        "algo_name": algo_name,
        "algo_type": algo_type,
        "dataset_description": dataset_description,
        "user_prompt": user_prompt,
        "algo_prompt": algo_prompt,
        "metrics_path": metrics_path,
        "coefficients_path": coefficients_path or metrics_path,
        "image_paths": image_paths
    }
    
    models = config.get("selected_llms") if config.get("selected_llms") is not None else model_list_img_supp
    import os
    print("API KEY FOUND:", os.getenv("OPENAI_API_KEY") is not None)
    llm_service = OpenAILLMService()
    orchestrator = LLMOrchestrator(AlgorithmWiseStrategy(), llm_service)
    results = orchestrator.run([task], models)
    risultati = results.get(algo_name, {})
 
    print("\n" + "═" * 60)
    print("   LLM ANALYSIS RESULTS")
    print("═" * 60)
    for modello, risposta in risultati.items():
        print(f"\n[{modello}]\n{risposta}\n{'─' * 60}")
       
    output_dir = export_results.get("plot_dir", ".")
    report_path = Path(output_dir) / "LLM_Analysis_Report.md"
   
    try:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("# LLM Interpretative Analysis Report\n\n")
           
            for modello, risposta in risultati.items():
                f.write(f"## Model: `{modello}`\n\n")
                f.write(f"{risposta}\n\n")
                f.write("---\n\n")
               
        log.info(f"    ✔ LLM Report saved successfully in: {report_path}")
    except Exception as e:
        log.exception(f"    Error during LLM report saving: {e}")
 
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
        dataset_cfg = config["dataset_cfg"]
        test_size = config.get("test_size", 0.2)
        run_shap = config.get("run_shap", False)
        run_llm = config.get("run_llm", False)
 
        log.info("═" * 60)
        log.info(f"  Pipeline started: {config['algo_name']} on '{dataset_name}'")
        log.info("═" * 60)
 
        # primitive operations implemented by subclass
        model = self.load_model(config)
 
        X_train, X_test, y_train, y_test = self.load_data(model, dataset_cfg, test_size)
 
        self.fit(model, X_train, y_train, X_test, y_test)
 
        plot_paths = self.plots(model, dataset_cfg)
 
        shap_paths = {}
        if run_shap:
            shap_result = self.shap(model, dataset_cfg)
            # shap_result may be either the legacy dict or the new ExplainerResult
            if isinstance(shap_result, dict):
                shap_paths = shap_result
            else:
                shap_paths = getattr(shap_result, 'plot_paths', {})
 
        export_res = self.export(model)
 
        llm_results = {}
        if run_llm:
            all_plot_paths = {**plot_paths, **shap_paths}
            llm_results = self.llm(export_res, all_plot_paths, config)
 
        log.info("═" * 60)
        log.info("  Pipeline completed successfully.")
        log.info("═" * 60)
 
        return {
            "model": model,
            "plot_paths": {**plot_paths, **shap_paths},
            "export": export_res,
            "llm_results": llm_results,
        }
 
    @abstractmethod
    def load_model(self, config: dict):
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
 
    def load_model(self, config: dict):
        return _load_model(config)
 
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
    analysis_type = config.get("analysis_type", AnalysisType.SINGLE)
    results_map={}
    
    algorithms = config.get("algorithms", [config.get("algo_enum")])
    run_llm = config.get("run_llm", False)
    llm_execution_mode = config.get("llm_execution_mode", "algorithm_wise")
    selected_llms = config.get("selected_llms")
    
    print("\n" + "█" * 60)
    print(f"  STARTING WORKFLOW: {analysis_type.value.upper()} on dataset '{config['dataset_name']}'")
    print("█" * 60)

    for algo in algorithms:
        local_config = config.copy()
        local_config["algo_enum"] = algo
        local_config["algo_name"] = str(algo)
        local_config["algo_info"] = ModelFactory.get_all_info(algo, config["dataset_cfg"]["task"])
        
        # If running LLM-wise, suppress LLM execution during individual pipeline runs
        if llm_execution_mode == "llm_wise":
            local_config["run_llm"] = False
        
        try:
            pipeline_output = pipeline.run(local_config)
            results_map[str(algo)] = pipeline_output
        except Exception as e:
            log.exception(f"❌ Critical error during the execution of {algo}: {e}")
            traceback.print_exc()
            print("\n Passing to the next algorithm...\n")
            continue
        
    # Batch LLM-wise execution after all ML models are trained and analyzed
    if run_llm and llm_execution_mode == "llm_wise" and results_map:
        log.info("━━  BATCH STEP: LLM-wise analysis")
        tasks = []
        for algo in algorithms:
            algo_str = str(algo)
            if algo_str not in results_map:
                continue
            out = results_map[algo_str]
            export_results = out["export"]
            
            output_dir = export_results.get("plot_dir")
            image_paths = []
            if output_dir:
                p_dir = Path(output_dir)
                image_paths.extend(list(p_dir.glob("*.png")))
                
            tasks.append({
                "algo_name": algo_str,
                "algo_type": config["dataset_cfg"]["task"],
                "dataset_description": config["dataset_cfg"]["description"],
                "user_prompt": config["user_prompt"],
                "algo_prompt": ModelFactory.get_all_info(algo, config["dataset_cfg"]["task"])["prompt"],
                "metrics_path": export_results.get("metrics_path"),
                "coefficients_path": export_results.get("coefficients_path") or export_results.get("metrics_path"),
                "image_paths": image_paths
            })
            
        try:
            from src.core.llm.services import OpenAILLMService
            from src.core.llm.strategies import LLMWiseStrategy
            from src.core.llm.orchestrator_context import LLMOrchestrator
            
            llm_service = OpenAILLMService()
            orchestrator = LLMOrchestrator(LLMWiseStrategy(), llm_service)
            risultati_batch = orchestrator.run(tasks, selected_llms)
            
            # Map results back to each algorithm output
            for algo_str, out in results_map.items():
                if algo_str in risultati_batch:
                    out["llm_results"] = risultati_batch[algo_str]
                    
                    print("\n" + "═" * 60)
                    print(f"   LLM ANALYSIS RESULTS FOR {algo_str}")
                    print("═" * 60)
                    for modello, risposta in risultati_batch[algo_str].items():
                        print(f"\n[{modello}]\n{risposta}\n{'─' * 60}")
                        
                    output_dir = out["export"].get("plot_dir", ".")
                    report_path = Path(output_dir) / "LLM_Analysis_Report.md"
                    
                    try:
                        with open(report_path, "w", encoding="utf-8") as f:
                            f.write(f"# LLM Interpretative Analysis Report for {algo_str}\n\n")
                            for modello, risposta in risultati_batch[algo_str].items():
                                f.write(f"## Model: `{modello}`\n\n")
                                f.write(f"{risposta}\n\n")
                                f.write("---\n\n")
                        log.info(f"    ✔ LLM Report saved successfully in: {report_path}")
                    except Exception as e:
                        log.exception(f"    Error during LLM report saving: {e}")
        except Exception as e:
            log.exception(f"❌ Critical error during the batch LLM execution: {e}")
        
    if analysis_type == AnalysisType.COMPARATIVE and len(results_map) > 1:
        print("\n" + "═" * 60)
        print("   FINAL METRIC COMPARISON")
        print("═" * 60)
        for algo_name, out in results_map.items():
            metrics = out["export"].get("metrics", {})
            print(f"  > {algo_name}: {metrics}")
        print("═" * 60)

    return results_map
 
 
# ------------------------------------------------------------------ #
#  Entry point                                                         #
# ------------------------------------------------------------------ #
 
if __name__ == "__main__":
    try:
        initialize_model_registry()
        from src.core.selector import run_selector
        config = run_selector()
        run_pipeline(config)
    except KeyboardInterrupt:
        print("\n\n  Interrupted by user.")
        sys.exit(0)
    except Exception:
        log.error("Critical error in the pipeline:")
        traceback.print_exc()
        sys.exit(1)