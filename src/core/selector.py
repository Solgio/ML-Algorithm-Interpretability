"""
selector.py — Selezione interattiva da CLI di dataset e algoritmo.

Restituisce un dizionario con le scelte effettuate, pronto per l'orchestratore.
"""
from config.datasets_config import DATASETS
from domain.enums import Algorithm, TaskType
from infrastructure.models.model_factory import ModelFactory


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

    dataset_name, dataset_cfg = select_dataset()
    dataset_task = dataset_cfg["task"]
    algo_enum= select_algorithm(dataset_task)
    options                   = select_options()
    config = {
        "dataset_name": dataset_name,
        "dataset_cfg":  dataset_cfg,
        "algo_enum": algo_enum,
        "algo_name": str(algo_enum),
        "algo_info": ModelFactory.get_all_info(algo_enum, dataset_task),
        **options,
    }

    # Riepilogo
    print("\n" + "═" * 50)
    print("   RIEPILOGO CONFIGURAZIONE")
    print("═" * 50)
    print(f"  Dataset    : {dataset_name}")
    print(f"  Algoritmo  : {algo_enum}")
    print(f"  Test size  : {options['test_size']}")
    print(f"  SHAP       : {'sì' if options['run_shap'] else 'no'}")
    print(f"  LLM        : {'sì' if options['run_llm'] else 'no'}")
    print("═" * 50)

    if not _confirm("Avviare la pipeline con questa configurazione?"):
        print("\n  Pipeline annullata.\n")
        raise SystemExit(0)

    return config


if __name__ == "__main__":
    cfg = run_selector()
    print("\nConfig pronta:", cfg)

