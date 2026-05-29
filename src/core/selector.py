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
            "prompt": "Questo modello ha un'altissima trasparenza intrinseca e i suoi parametri sono interpretabili direttamente. Spiega l'impatto (magnitudo) e la direzione (segno positivo o negativo) dei coefficienti principali. Descrivi come l'aumento unitario di un fattore causa una variazione proporzionale nella previsione finale, ma avverti che si tratta di correlazioni e non di leggi causali assolute.",
        },
        "Decision tree":{
            "module": "models.DecTree",
            "class": "DecisionTreeR",
            "description": "Albero decisionale (sklearn)",
            "prompt": "Questo modello possiede un'elevata tracciabilità locale basata su una spiegabilità strutturale.Spiega le decisioni come una sequenza di regole logiche 'se... allora' (cammino decisionale) che rispecchiano fedelmente il ragionamento umano. Utilizza la feature importance globale per evidenziare qual è il criterio di sbarramento fondamentale al vertice dell'albero.",
            "param_grid": {
            'criterion': ['squared_error', 'absolute_error', 'friedman_mse', 'poisson'],
            'max_depth': [None, 5, 20],
            'min_samples_split': [2, 10],
            'min_samples_leaf': [1, 4],
            'ccp_alpha': [0.0, 0.1]
        }
        },
        "Random Forest":{
            "module": "models.RandForest",
            "class": "RandomForestR",
            "description": "Random Forest (sklearn)",
            "prompt": "Questo modello è un 'Ensemble' con trasparenza media, che richiede l'uso della feature importance (spiegabilità post-hoc) per essere compreso.Spiega che l'algoritmo crea molti scenari paralleli e prende la decisione a maggioranza. I fattori principali identificati rappresentano gli argomenti che hanno convinto la maggioranza, compensando eventuali errori dei singoli.",
            "param_grid": {
            'n_estimators': [100, 200],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 10],
            'min_samples_leaf': [1, 4],
            'max_features': ['sqrt', 'log2'],
            'ccp_alpha': [0.0, 0.1],
            'criterion': ['squared_error', 'absolute_error', 'friedman_mse', 'poisson'],
            'min_impurity_decrease': [0.0, 0.1]
        }
        },
        "XGBoost":{
            "module": "models.XGBoost",
            "class": "XGBoostR",
            "description": "XGBRegressor (xgboost)",
            "prompt": "Questo modello ha una bassa trasparenza intrinseca (modello opaco) e si affida a spiegazioni post-hoc.Spiega che l'algoritmo procede per passaggi successivi, concentrandosi progressivamente sui casi più difficili. Usa l'importanza delle feature per illustrare quali variabili sono state più utili a correggere gli errori durante questo processo di apprendimento.",
            "param_grid": {
            'n_estimators': [100, 300],
            'max_depth': [3, 10],
            'learning_rate': [0.01, 0.2],
            'subsample': [0.8, 1.0],
            'colsample_bytree': [0.6, 1.0],
            'gamma': [0, 0.2]
            }
        },
    },
    "classification": {
        "Logistic Regression": {
            "module": "models.LogR",
            "class": "LogisticRegression",
            "description": "Regressione logistica (sklearn)",
            "prompt": "Questo modello offre una spiegabilità di tipo probabilistico. Non parlare di logaritmi, ma spiega come l'aumento di una specifica variabile moltiplichi le probabilità (odds ratio) che un evento si verifichi. Commenta la sicurezza del modello ricordando che probabilità molto vicine allo 0 o al 100 indicano alta confidenza.",
            },
        "SVM":{
            "module": "models.SVM",
            "class": "SVM",
            "description": "Support Vector Machine (sklearn.svm.SVC)",
            "prompt": "Questo è un modello opaco con bassa trasparenza. Spiega che l'algoritmo ignora i casi ovvi e cerca la linea di demarcazione ottimale concentrandosi solo sulle istanze limite, ovvero quelle più ambigue (i vettori di supporto). Usa le feature più importanti per spiegare quali 'coordinate' definiscono questo confine critico.",
            "param_grid": {
              'C': [0.1, 1, 10, 100],   
              'gamma':['scale', 'auto', 0.1, 0.01, 0.001, 0.0001],
              'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],
              'class_weight': [None, 'balanced'],
              'degree': [2, 4]
              }
        },
        "Decision tree":{
            "module": "models.DecTree",
            "class": "DecisionTreeC",
            "description": "Albero decisionale (sklearn)",
            "prompt": "Questo modello possiede un'elevata tracciabilità locale basata su una spiegabilità strutturale. Spiega le decisioni come una sequenza di regole logiche 'se... allora' (cammino decisionale) che rispecchiano fedelmente il ragionamento umano. Utilizza la feature importance globale per evidenziare qual è il criterio di sbarramento fondamentale al vertice dell'albero.",
            "param_grid": {
            'criterion': ['gini', 'entropy'],
            'max_depth': [None, 5, 20],
            'min_samples_split': [2, 10],
            'min_samples_leaf': [1, 4],
            'ccp_alpha': [0.0, 0.1]
        }
        },
        "Random Forest":{
            "module": "models.RandForest",
            "class": "RandomForestC",
            "description": "Random Forest (sklearn)",
            "prompt": "Questo modello è un 'Ensemble' con trasparenza media, che richiede l'uso della feature importance (spiegabilità post-hoc) per essere compreso. Spiega che l'algoritmo crea molti scenari paralleli e prende la decisione a maggioranza. I fattori principali identificati rappresentano gli argomenti che hanno convinto la maggioranza, compensando eventuali errori dei singoli.",
            "param_grid": {
            'n_estimators': [100, 200],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 10],
            'min_samples_leaf': [1, 4],
            'max_features': ['sqrt', 'log2'],
            'ccp_alpha': [0.0, 0.1],
            'criterion': ['gini', 'entropy', 'log_loss'],
            'min_impurity_decrease': [0.0, 0.1]
        }
        },
        "XGBoost":{
            "module": "models.XGBoost",
            "class": "XGBoostC",
            "description": "XGBClassifier (xgboost)",
            "prompt": "Questo modello ha una bassa trasparenza intrinseca (modello opaco) e si affida a spiegazioni post-hoc. Spiega che l'algoritmo procede per passaggi successivi, concentrandosi progressivamente sui casi più difficili. Usa l'importanza delle feature per illustrare quali variabili sono state più utili a correggere gli errori durante questo processo di apprendimento.",
            "param_grid": {
            'n_estimators': [100, 300],
            'max_depth': [3, 10],
            'learning_rate': [0.01, 0.2],
            'subsample': [0.8, 1.0],
            'colsample_bytree': [0.6, 1.0],
            'gamma': [0, 0.2],
        }
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

