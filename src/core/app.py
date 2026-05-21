import streamlit as st
from config.datasets_config import DATASETS
from selector import ALGORITHMS
from orchestrator import run_pipeline

st.set_page_config(page_title="ML Pipeline Dashboard", layout="centered")
st.title("Machine Learning Pipeline Orchestrator")

st.header("1. Selezione Dataset")
dataset_names = list(DATASETS.keys())

selected_dataset = st.selectbox("Scegli un dataset:", dataset_names, index=0)
dataset_cfg = DATASETS[selected_dataset]

st.info(f"**Task:** {dataset_cfg['task'].capitalize()}  \n**Descrizione:** {dataset_cfg['description']}")

st.header("2. Selezione Algoritmo")
task_type = dataset_cfg["task"]
disponibili_algos = ALGORITHMS.get(task_type, {})

if not disponibili_algos:
    st.error(f"Nessun algoritmo configurato per il task: {task_type}")
    st.stop()

algo_names = list(disponibili_algos.keys())
selected_algo = st.selectbox("Scegli l'algoritmo da addestrare:", algo_names, index=0)
algo_info = disponibili_algos[selected_algo]

st.caption(f"*Descrizione modello:* {algo_info['description']}")

st.header("3. Parametri e Opzioni")

with st.expander("Configurazioni di esecuzione", expanded=True):
    test_size = st.slider("Dimensione del Test Set (proporzione):", min_value=0.1, max_value=0.5, value=0.2, step=0.05)
    run_shap = st.checkbox("Esegui analisi SHAP interpretativa", value=False)
    run_llm = st.checkbox("Genera report finale tramite LLM", value=False)

config = {
    "dataset_name": selected_dataset,
    "dataset_cfg":  dataset_cfg,
    "algo_name":    selected_algo,
    "algo_info":    algo_info,
    "test_size":    test_size,
    "run_shap":     run_shap,
    "run_llm":      run_llm,
}

st.markdown("---")
    
if st.button("Avvia Pipeline", type="primary"):
    with st.spinner("Pipeline in corso di esecuzione... Controlla il terminale per i log dettagliati."):
        try:
            risultati = run_pipeline(config)
            
            st.success("Pipeline completata con successo!")
            
            if "export" in risultati and "metrics" in risultati["export"]:
                st.subheader("Metriche di Performance ottenute:")
                st.json(risultati["export"]["metrics"])
                
            if run_llm and "llm_results" in risultati:
                st.subheader("Analisi Interpretativa dell'LLM")
                for modello, risposta in risultati["llm_results"].items():
                    st.markdown(f"## :violet[Risposta da {modello}]")
                    st.write(risposta)
                    
        except Exception as e:
            st.error(f"Si è verificato un errore critico durante la pipeline: {e}")