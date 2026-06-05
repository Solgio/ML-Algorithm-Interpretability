import os
import sys
import streamlit as st
import logging
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.core.config.datasets_config import DATASETS
from src.core.domain.enums import AnalysisType, Algorithm
from src.core.infrastructure.models.model_factory import ModelFactory
from src.core.orchestrator import run_pipeline
from src.core.infrastructure.models.registry_initializer import initialize_model_registry

initialize_model_registry()

class StreamlitLogHandler(logging.Handler):
    def __init__(self, st_container):
        super().__init__()
        self.st_container = st_container
        self.log_buffer = []

    def emit(self, record):
        msg = self.format(record)
        self.log_buffer.append(msg)
        if len(self.log_buffer) > 50:
            self.log_buffer.pop(0)
        self.st_container.code("\n".join(self.log_buffer), language="log")

st.set_page_config(page_title="ML Pipeline Dashboard", layout="wide")
st.title("Machine Learning Pipeline Orchestrator")

st.header("1. Configurazione Iniziale")
col1, col2 = st.columns(2)

with col1:
    dataset_names = list(DATASETS.keys())
    selected_dataset = st.selectbox("Scegli un dataset:", dataset_names, index=0)
    dataset_cfg = DATASETS[selected_dataset]
    task_type = dataset_cfg["task"]
    st.info(f"**Task:** {task_type}  \n**Descrizione:** {dataset_cfg['description']}")

with col2:
    tipo_analisi = st.radio("Tipo di Esecuzione:", ["Singolo Modello", "Comparativa (Tutti i modelli)"])
    is_comparative = tipo_analisi == "Comparativa (Tutti i modelli)"
    analysis_type = AnalysisType.COMPARATIVE if is_comparative else AnalysisType.SINGLE

st.header("2. Selezione Algoritmo")
disponibili_algos = ModelFactory.list_algorithms(task_type)

if not disponibili_algos:
    st.error(f"Nessun algoritmo configurato per il task: {task_type}")
    st.stop()

algorithms_to_run = []

if is_comparative:
    selected_comparative_algos = st.multiselect(
        "Scegli gli algoritmi da confrontare:", 
        options=disponibili_algos, 
        default=disponibili_algos 
    )
    
    if not selected_comparative_algos:
        st.warning("⚠ Seleziona almeno un algoritmo per avviare il confronto.")
        st.stop()

    st.success(f"Verranno addestrati e confrontati in sequenza: **{', '.join(selected_comparative_algos)}**")
    
    for algo_name in selected_comparative_algos:
        algorithms_to_run.append(Algorithm(algo_name.lower().replace(" ", "_")))
        
else:
    selected_algo_name = st.selectbox("Scegli l'algoritmo da addestrare:", disponibili_algos, index=0)
    algo_enum = Algorithm(selected_algo_name.lower().replace(" ", "_"))
    algorithms_to_run.append(algo_enum)
    st.caption(f"*Descrizione modello:* {ModelFactory.get_description(algo_enum, task_type)}")

st.header("3. Parametri e Opzioni")
with st.expander("Configurazioni di esecuzione", expanded=True):
    test_size = st.slider("Dimensione del Test Set (proporzione):", min_value=0.1, max_value=0.5, value=0.2, step=0.05)
    run_shap = st.checkbox("Esegui analisi SHAP interpretativa", value=False)
    run_llm = st.checkbox("Genera report finale tramite LLM", value=False)

config = {
    "analysis_type": analysis_type,
    "dataset_name": selected_dataset,
    "dataset_cfg":  dataset_cfg,
    "algorithms": algorithms_to_run,
    "test_size":    test_size,
    "run_shap":     run_shap,
    "run_llm":      run_llm,
}

if analysis_type == AnalysisType.SINGLE:
    config["algo_enum"] = algorithms_to_run[0]
    config["algo_name"] = str(algorithms_to_run[0])
    config["algo_info"] = ModelFactory.get_all_info(algorithms_to_run[0], task_type)

st.markdown("---")

col_azioni1, col_azioni2 = st.columns([1, 5])

with col_azioni1:
    avvia_pipeline = st.button("Avvia Pipeline", type="primary")

with col_azioni2:
    if st.button("Nuova Analisi / Reset", type="secondary"):
        st.session_state.clear()
        st.rerun()               

if "risultati_pipeline" not in st.session_state:
    st.session_state["risultati_pipeline"] = None

if avvia_pipeline:
    st.subheader("Console di Esecuzione")
    
    log_container = st.empty()
    sl_handler = StreamlitLogHandler(log_container)
    sl_handler.setFormatter(logging.Formatter("%(asctime)s  %(levelname)-8s  %(message)s", datefmt="%H:%M:%S"))
    root_logger = logging.getLogger()
    root_logger.addHandler(sl_handler)
    
    progress_bar = st.progress(0, text="Inizializzazione in corso...")

    try:
        st.session_state["risultati_pipeline"] = run_pipeline(config)
        progress_bar.progress(100, text="Esecuzione completata!")
        st.success("Pipeline terminata con successo.")
    except Exception as e:
        progress_bar.empty()
        st.error(f"Si è verificato un errore critico: {e}")
    finally:
        root_logger.removeHandler(sl_handler)

if st.session_state["risultati_pipeline"] is not None:
    risultati = st.session_state["risultati_pipeline"]
    
    st.header("Metriche di Performance")
    
    if is_comparative:
        metrics_data = {}
        for algo, out in risultati.items():
            if "export" in out and "metrics" in out["export"]:
                metrics_data[algo] = out["export"]["metrics"]
        
        if metrics_data:
            df_metrics = pd.DataFrame(metrics_data).T
            st.dataframe(df_metrics, use_container_width=True)
    else:
        algo_key = str(algorithms_to_run[0])
        if algo_key in risultati and "export" in risultati[algo_key]:
            st.json(risultati[algo_key]["export"]["metrics"])

    if run_llm:
        st.header("Analisi Interpretativa LLM")
        for algo, out in risultati.items():
            if "llm_results" in out and out["llm_results"]:
                with st.expander(f"Report LLM - {algo}", expanded=not is_comparative):
                    for modello_llm, risposta in out["llm_results"].items():
                        st.markdown(f"### {modello_llm}")
                        st.write(risposta)
