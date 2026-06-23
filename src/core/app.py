import os
import sys
import streamlit as st
import logging
import threading
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.core.config.datasets_config import DATASETS
from src.core.domain.enums import AnalysisType, Algorithm
from src.core.infrastructure.models.model_factory import ModelFactory
from src.core.orchestrator import run_pipeline
from src.core.infrastructure.models.registry_initializer import initialize_model_registry

initialize_model_registry()

class SmartStreamlitLogHandler(logging.Handler):
    """
    Overwrites a single status line for main-thread logs,
    and batches background-thread logs to be displayed at the end.
    """
    def __init__(self, status_container, batch_container):
        super().__init__()
        self.status_container = status_container
        self.batch_container = batch_container
        self.batch_logs = []
        
        self.script_thread_id = threading.get_ident()

    def emit(self, record):
        msg = self.format(record)
        
        if threading.get_ident() == self.script_thread_id:
            self.status_container.info(f"🔄 **Status:** {msg}")
        else:
            self.batch_logs.append(msg)
    
    def flush_batch(self):
        """Called at the end to render the LLM batch."""
        if self.batch_logs:
            self.batch_container.code("\n".join(self.batch_logs), language="log")
            self.batch_logs = []

st.set_page_config(page_title="ML Pipeline Dashboard", layout="wide")
st.title("Machine Learning Pipeline Orchestrator")

if "is_running" not in st.session_state:
    st.session_state["is_running"] = False

if "risultati_pipeline" not in st.session_state:
    st.session_state["risultati_pipeline"] = None

st.header("1. Initial Configuration")
col1, col2 = st.columns(2)

with col1:
    dataset_names = list(DATASETS.keys())
    selected_dataset = st.selectbox("Choose a dataset:", dataset_names, index=0)
    dataset_cfg = DATASETS[selected_dataset]
    task_type = dataset_cfg["task"]
    st.info(f"**Task:** {task_type}  \n**Description:** {dataset_cfg['description']}")

with col2:
    tipo_analisi = st.radio("Execution Type:", ["Single Model", "Comparative (All models)"])
    is_comparative = tipo_analisi == "Comparative (All models)"
    analysis_type = AnalysisType.COMPARATIVE if is_comparative else AnalysisType.SINGLE

st.header("2. Algorithm Selection")
disponibili_algos = ModelFactory.list_algorithms(task_type)

if not disponibili_algos:
    st.error(f"No algorithm configured for task: {task_type}")
    st.stop()

algorithms_to_run = []

if is_comparative:
    selected_comparative_algos = st.multiselect(
        "Choose algorithms to compare:", 
        options=disponibili_algos, 
        default=disponibili_algos 
    )
    
    if not selected_comparative_algos:
        st.warning("⚠ Select at least one algorithm to start the comparison.")
        st.stop()

    st.success(f"Will be trained and compared in sequence: **{', '.join(selected_comparative_algos)}**")
    
    for algo_name in selected_comparative_algos:
        algorithms_to_run.append(Algorithm(algo_name.lower().replace(" ", "_")))
        
else:
    selected_algo_name = st.selectbox("Choose algorithm to train:", disponibili_algos, index=0)
    algo_enum = Algorithm(selected_algo_name.lower().replace(" ", "_"))
    algorithms_to_run.append(algo_enum)
    st.caption(f"*Model description:* {ModelFactory.get_description(algo_enum, task_type)}")

st.header("3. Parameters and Options")
with st.expander("Execution Configurations", expanded=True):
    test_size = st.slider("Test Set size (proportion):", min_value=0.1, max_value=0.5, value=0.2, step=0.05)
    run_shap = st.checkbox("Execute interpretive SHAP analysis", value=False)
    run_llm = st.checkbox("Generate final report via LLM", value=False)

    user_prompt = None
    llm_execution_mode = "algorithm_wise"
    selected_llms = None
    if run_llm:
        user_prompt_input = st.text_input("Enter a custom prompt for the LLM analysis (or leave empty for default):")
        if user_prompt_input.strip():
            user_prompt = user_prompt_input.strip()
            
        from src.core.llm.LLMDataWarehouse import model_list_img_supp
        selected_llms = st.multiselect(
            "Select LLM models to run:",
            options=model_list_img_supp,
            default=model_list_img_supp,
            help="Select which models will evaluate the results."
        )
        
        if not selected_llms:
            st.warning("⚠ Please select at least one LLM model to generate reports.")
            
        llm_execution_mode = st.radio(
            "LLM Execution Mode:",
            options=["llm_wise", "algorithm_wise"],
            index=0,
            format_func=lambda x: "LLM-wise (Mounts each LLM once to evaluate all algorithms - RECOMMENDED)" if x == "llm_wise" else "Algorithm-wise (Evaluates all LLMs for one algorithm before moving to the next)",
            help="LLM-wise mode reduces GPU memory swapping overhead significantly when running multiple algorithms."
        )

config = {
    "analysis_type": analysis_type,
    "dataset_name": selected_dataset,
    "dataset_cfg":  dataset_cfg,
    "algorithms": algorithms_to_run,
    "test_size":    test_size,
    "run_shap":     run_shap,
    "run_llm":      run_llm and bool(selected_llms),
    "user_prompt":  user_prompt,
    "llm_execution_mode": llm_execution_mode,
    "selected_llms": selected_llms,
}

if analysis_type == AnalysisType.SINGLE:
    config["algo_enum"] = algorithms_to_run[0]
    config["algo_name"] = str(algorithms_to_run[0])
    config["algo_info"] = ModelFactory.get_all_info(algorithms_to_run[0], task_type)

st.markdown("---")

def lock_ui():
    st.session_state["is_running"] = True

col_azioni1, col_azioni2 = st.columns([1, 5])

with col_azioni1:
    avvia_pipeline = st.button("Start Pipeline", type="primary", on_click=lock_ui, disabled=st.session_state["is_running"])

with col_azioni2:
    if st.button("New Analysis / Reset", type="secondary"):
        st.session_state.clear()
        st.rerun()               


if avvia_pipeline:
    st.subheader("Execution Console")
    
    status_container = st.empty()
    batch_container = st.empty()
    smart_handler = SmartStreamlitLogHandler(status_container, batch_container)
    smart_handler.setFormatter(logging.Formatter("%(asctime)s  %(levelname)-8s  %(message)s", datefmt="%H:%M:%S"))
    root_logger = logging.getLogger()
    root_logger.addHandler(smart_handler)

    try:
        st.session_state["risultati_pipeline"] = run_pipeline(config)
        st.success("Pipeline finished successfully.")
        status_container.empty()
    except Exception as e:
        st.error(f"A critical error occurred: {e}")
    finally:
        smart_handler.flush_batch()
        root_logger.removeHandler(smart_handler)
        st.session_state["is_running"] = False
        st.rerun()

if st.session_state["risultati_pipeline"] is not None:
    risultati = st.session_state["risultati_pipeline"]
    
    st.header("Performance Metrics")
    
    if is_comparative:
        metrics_data = {}
        for algo, out in risultati.items():
            if "export" in out and "metrics" in out["export"]:
                metrics_data[algo] = out["export"]["metrics"]
        
        if metrics_data:
            df_metrics = pd.DataFrame(metrics_data).T
            st.dataframe(df_metrics, width='stretch')
    else:
        algo_key = str(algorithms_to_run[0])
        if algo_key in risultati and "export" in risultati[algo_key]:
            st.json(risultati[algo_key]["export"]["metrics"])

    if run_llm:
        st.header("Interpretive LLM Analysis")
        for algo, out in risultati.items():
            if "llm_results" in out and out["llm_results"]:
                with st.expander(f"Report LLM - {algo}", expanded=not is_comparative):
                    for modello_llm, risposta in out["llm_results"].items():
                        st.markdown(f"### {modello_llm}")
                        st.write(risposta)
