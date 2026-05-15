"""
selector.py — Selezione interattiva da CLI di dataset e algoritmo.

Restituisce un dizionario con le scelte effettuate, pronto per l'orchestratore.
"""
from config.datasets_config import DATASETS

ALGORITHMS = {
    "regression": {
        "Linear Regression": {
            "module": "models.LR",
            "class": "LinearRegression",
            "description": "Regressione lineare OLS (sklearn)",
        },
        "Decision tree":{
            "module": "models.DecTree",
            "class": "DecisionTreeR",
            "description": "Albero decisionale (sklearn)",
        },
        "Random Forest":{
            "module": "models.RandForest",
            "class": "RandomForestR",
            "description": "Random Forest (sklearn)",
        },
        "XGBoost":{
            "module": "models.XGBoost",
            "class": "XGBoostModel",
            "description": "XGBoost (xgboost)",
        },
    },
    "classification": {
        "Logistic Regression": {
            "module": "models.LogR",
            "class": "LogisticRegression",
            "description": "Regressione logistica (sklearn)",
            },
        "SVM":{
            "module": "models.SVM",
            "class": "SVM",
            "description": "Support Vector Machine (sklearn.svm.SVC)",
        },
        "Decision tree":{
            "module": "models.DecTree",
            "class": "DecisionTreeC",
            "description": "Albero decisionale (sklearn)",
        },
        "Random Forest":{
            "module": "models.RandForest",
            "class": "RandomForestC",
            "description": "Random Forest (sklearn)",
        },
        "XGBoost":{
        "module": "models.XGBoost",
        "class": "XGBoostModel",
        "description": "XGBoost (xgboost)",
        },
    },
}


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


def select_algorithm(task_type: str) -> tuple[str, dict]:
    """
    Fa scegliere all'utente un algoritmo compatibile con task_type.
    Restituisce (nome, info_dict).
    """
    algos = ALGORITHMS.get(task_type, {})
    if not algos:
        raise ValueError(
            f"Nessun algoritmo registrato per il task '{task_type}'. "
            "Aggiungi un entry in selector.ALGORITHMS."
        )

    names = list(algos.keys())
    labels = [f"{n}  — {algos[n]['description']}" for n in names]

    idx = _print_menu(f"Seleziona l'ALGORITMO  (task: {task_type})", labels)
    name = names[idx]
    info = algos[name]

    print(f"\n  ✔  Algoritmo selezionato : {name}")
    return name, info

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
    algo_name, algo_info      = select_algorithm(dataset_cfg["task"])
    options                   = select_options()

    config = {
        "dataset_name": dataset_name,
        "dataset_cfg":  dataset_cfg,
        "algo_name":    algo_name,
        "algo_info":    algo_info,
        **options,
    }

    # Riepilogo
    print("\n" + "═" * 50)
    print("   RIEPILOGO CONFIGURAZIONE")
    print("═" * 50)
    print(f"  Dataset    : {dataset_name}")
    print(f"  Algoritmo  : {algo_name}")
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

