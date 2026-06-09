"""
selector.py — Selezione interattiva da CLI di dataset e algoritmo.

Restituisce un dizionario con le scelte effettuate, pronto per l'orchestratore.
"""
from src.core.config.datasets_config import DATASETS
from src.core.domain.enums import Algorithm, AnalysisType, TaskType
from src.core.infrastructure.models.model_factory import ModelFactory


def _print_menu(title: str, options: list[str]) -> int:
    """Stampa un menu numerato e restituisce l'indice scelto (0-based)."""
    print(f"\n{'─'*50}")
    print(f"  {title}")
    print(f"{'─'*50}")
    for i, opt in enumerate(options, start=1):
        print(f"  [{i}] {opt}")
    print(f"{'─'*50}")

    while True:
        raw = input("  Scelta: ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return int(raw) - 1
        print(f"  ⚠  Inserisci un numero tra 1 e {len(options)}.")


def _confirm(question: str) -> bool:
    ans = input(f"\n  {question} [s/n]: ").strip().lower()
    return ans in ("s", "si", "sì", "y", "yes")


def select_analysis_type()-> AnalysisType:
    """Prompt the user to select the type of analysis to perform (comparative run or single model)."""
    options = ["Eseguire un confronto tra più modelli", "Eseguire un'analisi su un singolo modello"]
    idx = _print_menu("Seleziona il tipo di analisi", options)
    return AnalysisType.COMPARATIVE if idx == 0 else AnalysisType.SINGLE

def select_dataset() -> tuple[str, dict]:
    """Fa scegliere all'utente un dataset. Restituisce (nome, config)."""
    names = list(DATASETS.keys())
    labels = [f"{n}  [{DATASETS[n]['task']}]" for n in names]

    idx = _print_menu("Seleziona il DATASET", labels)
    name = names[idx]
    cfg = DATASETS[name]

    print(f"\n  ✔  Dataset selezionato : {name}")
    print(f"     Task               : {cfg['task']}")
    print(f"     Descrizione        : {cfg['description']}")
    return name, cfg


def select_algorithm(task_type: TaskType) -> Algorithm:
    """
    Make user choose an algorithm compatible with the given task type."
    """
    available_names = ModelFactory.list_algorithms(task_type)
    
    if not available_names:
        raise ValueError(f"\n  ⚠  Nessun algoritmo disponibile per il task '{task_type}'.")
    
    print("\n" + "═" * 50)
    print(f"  Seleziona l'ALGORITMO per task: {task_type}")
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
        choice = input("  Scelta: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(available_enums):
            selected_algo = available_enums[int(choice) - 1]
            print(f"\n  ✔  Algoritmo selezionato: {selected_algo}")
            return selected_algo
        print(f"  ⚠  Inserisci un numero tra 1 e {len(available_enums)}.")
        
def input_user_prompt() -> str:
    """Chiede all'utente di inserire un prompt personalizzato per l'analisi LLM."""
    print("\n" + "─" * 50)
    print("  Inserisci un prompt personalizzato per l'analisi LLM (o lascia vuoto per default):")
    print("─" * 50)
    prompt = input("  Prompt: ").strip()
    return prompt

def select_options() -> dict:
    """Raccoglie opzioni aggiuntive (test_size, SHAP, LLM)."""
    print(f"\n{'─'*50}")
    print("  Opzioni avanzate")
    print(f"{'─'*50}")

    while True:
        raw = input("  Dimensione test set [default 0.2]: ").strip()
        if raw == "":
            test_size = 0.2
            break
        try:
            test_size = float(raw)
            if 0 < test_size < 1:
                break
            print("  ⚠  Inserisci un valore tra 0 e 1 (es. 0.2).")
        except ValueError:
            print("  ⚠  Valore non valido.")

    run_shap = _confirm("Eseguire l'analisi SHAP?")
    run_llm  = _confirm("Avviare l'analisi LLM al termine?")

    return {
        "test_size": test_size,
        "run_shap": run_shap,
        "run_llm": run_llm,
    }


def run_selector() -> dict:
    """
    Esegue la selezione interattiva completa.
    Restituisce un dizionario con tutte le scelte, pronto per l'orchestratore.
    """
    print("\n" + "═" * 50)
    print("   ML PIPELINE — Configurazione")
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
        "user_prompt": input_user_prompt(),
        **options,
    }
    
    if analysis_type == AnalysisType.SINGLE:
        config["algo_enum"] = algorithms_to_run[0]
        config["algo_name"] = str(algorithms_to_run[0])
        config["algo_info"] = ModelFactory.get_all_info(algorithms_to_run[0], dataset_task)

    # Riepilogo
    print("\n" + "═" * 50)
    print("   RIEPILOGO CONFIGURAZIONE")
    print("═" * 50)
    print(f"  Tipo analisi : {analysis_type.value.title()}")
    print(f"  Dataset    : {dataset_name}")
    if analysis_type == AnalysisType.SINGLE:
        print(f"  Algoritmo   : {algorithms_to_run[0]}")
    else:
        print(f"  Algoritmi   : {', '.join([str(a) for a in algorithms_to_run])}")
    print(f"  Test size  : {options['test_size']}")
    print(f"  SHAP       : {'sì' if options['run_shap'] else 'no'}")
    print(f"  LLM        : {'sì' if options['run_llm'] else 'no'}")
    if config["user_prompt"]:
        print(f"  Prompt LLM  : {config['user_prompt']}")
    print("═" * 50)

    if not _confirm("Avviare la pipeline con questa configurazione?"):
        print("\n  Pipeline annullata.\n")
        raise SystemExit(0)

    return config


if __name__ == "__main__":
    cfg = run_selector()
    print("\nConfig pronta:", cfg)

