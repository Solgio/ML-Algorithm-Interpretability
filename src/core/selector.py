"""
selector.py — Interactive CLI selection of dataset and algorithm.

Returns a dictionary with the choices made, ready for the orchestrator.
"""
from src.core.config.datasets_config import DATASETS
from src.core.domain.enums import Algorithm, AnalysisType, TaskType
from src.core.infrastructure.models.model_factory import ModelFactory


def _print_menu(title: str, options: list[str]) -> int:
    """Prints a numbered menu and returns the chosen index (0-based)."""
    print(f"\n{'─'*50}")
    print(f"  {title}")
    print(f"{'─'*50}")
    for i, opt in enumerate(options, start=1):
        print(f"  [{i}] {opt}")
    print(f"{'─'*50}")

    while True:
        raw = input("  Choice: ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return int(raw) - 1
        print(f"  ⚠  Please enter a number between 1 and {len(options)}.")


def _confirm(question: str) -> bool:
    ans = input(f"\n  {question} [y/n]: ").strip().lower()
    return ans in ("y", "yes", "s", "si", "sì")


def select_analysis_type()-> AnalysisType:
    """Prompt the user to select the type of analysis to perform (comparative run or single model)."""
    options = ["Run a comparison between multiple models", "Run an analysis on a single model"]
    idx = _print_menu("Select type of analysis", options)
    return AnalysisType.COMPARATIVE if idx == 0 else AnalysisType.SINGLE

def select_dataset() -> tuple[str, dict]:
    """Fa scegliere all'utente un dataset. Restituisce (nome, config)."""
    names = list(DATASETS.keys())
    labels = [f"{n}  [{DATASETS[n]['task']}]" for n in names]

    idx = _print_menu("Select the DATASET", labels)
    name = names[idx]
    cfg = DATASETS[name]

    print(f"\n  ✔  Selected Dataset : {name}")
    print(f"     Task               : {cfg['task']}")
    print(f"     Description        : {cfg['description']}")
    return name, cfg


def select_algorithm(task_type: TaskType) -> Algorithm:
    """
    Make user choose an algorithm compatible with the given task type."
    """
    available_names = ModelFactory.list_algorithms(task_type)
    
    if not available_names:
        raise ValueError(f"\n  ⚠  No algorithm available for task '{task_type}'.")
    
    print("\n" + "═" * 50)
    print(f"  Select the ALGORITHM for task: {task_type}")
    print("═" * 50)
    
    available_enums = []
    for i, name in enumerate(available_names, start=1):
        enum_val = name.lower().replace(" ", "_")
        algo_enum = Algorithm(enum_val)
        available_enums.append(algo_enum)
        
        description = ModelFactory.get_description(algo_enum, task_type)
        print(f"  [{i}] {name} - {description}")
    
    print("═" * 50)
    
    while True:
        choice = input("  Choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(available_enums):
            selected_algo = available_enums[int(choice) - 1]
            print(f"\n  ✔  Selected Algorithm: {selected_algo}")
            return selected_algo
        print(f"  ⚠  Please enter a number between 1 and {len(available_enums)}.")
        
def input_user_prompt() -> str:
    """Asks the user to enter a custom prompt for the LLM analysis."""
    print("\n" + "─" * 50)
    print("  Enter a custom prompt for the LLM analysis (or leave empty for default):")
    print("─" * 50)
    prompt = input("  Prompt: ").strip()
    return prompt

def select_options() -> dict:
    """Collects additional options (test_size, SHAP, LLM)."""
    print(f"\n{'─'*50}")
    print("  Advanced options")
    print(f"{'─'*50}")

    while True:
        raw = input("  Test set size [default 0.2]: ").strip()
        if raw == "":
            test_size = 0.2
            break
        try:
            test_size = float(raw)
            if 0 < test_size < 1:
                break
            print("  ⚠  Enter a value between 0 and 1 (e.g., 0.2).")
        except ValueError:
            print("  ⚠  Invalid value.")

    run_shap = _confirm("Run SHAP analysis?")
    run_llm  = _confirm("Start LLM analysis at the end?")

    return {
        "test_size": test_size,
        "run_shap": run_shap,
        "run_llm": run_llm,
    }


def run_selector() -> dict:
    """
    Runs the complete interactive selection.
    Returns a dictionary with all the choices, ready for the orchestrator.
    """
    print("\n" + "═" * 50)
    print("   ML PIPELINE — Configuration")
    print("═" * 50)

    analysis_type = select_analysis_type()
    dataset_name, dataset_cfg = select_dataset()
    dataset_task = dataset_cfg["task"]
    
    algorithms_to_run=[]
    if analysis_type == AnalysisType.SINGLE:
        algo_enum = select_algorithm(dataset_task)
        algorithms_to_run.append(algo_enum)
    else:
        available_algorithms = ModelFactory.list_algorithms(dataset_task)
        for algo_name in available_algorithms:
            algo_enum = Algorithm(algo_name.lower().replace(" ", "_"))
            algorithms_to_run.append(algo_enum)

    options = select_options()
    config = {
        "analysis_type": analysis_type,
        "dataset_name": dataset_name,
        "dataset_cfg":  dataset_cfg,
        "algorithms": algorithms_to_run,
        **options,
    }
    
    if options["run_llm"]:
        config["user_prompt"] = input_user_prompt()
    else:
        config["user_prompt"] = None

    if analysis_type == AnalysisType.SINGLE:
        config["algo_enum"] = algorithms_to_run[0]
        config["algo_name"] = str(algorithms_to_run[0])
        config["algo_info"] = ModelFactory.get_all_info(algorithms_to_run[0], dataset_task)

    # Riepilogo
    print("\n" + "═" * 50)
    print("   Configuration Summary")
    print("═" * 50)
    print(f"  Analysis type : {analysis_type.value.title()}")
    print(f"  Dataset    : {dataset_name}")
    if analysis_type == AnalysisType.SINGLE:
        print(f"  Algorithm   : {algorithms_to_run[0]}")
    else:
        print(f"  Algorithms   : {', '.join([str(a) for a in algorithms_to_run])}")
    print(f"  Test size  : {options['test_size']}")
    print(f"  SHAP       : {'yes' if options['run_shap'] else 'no'}")
    print(f"  LLM        : {'yes' if options['run_llm'] else 'no'}")
    if config["user_prompt"]:
        print(f"  Prompt LLM  : {config['user_prompt']}")
    print("═" * 50)

    if not _confirm("Start the pipeline with this configuration?"):
        print("\n  Pipeline cancelled.\n")
        raise SystemExit(0)

    return config


if __name__ == "__main__":
    cfg = run_selector()
    print("\nConfig pronta:", cfg)

