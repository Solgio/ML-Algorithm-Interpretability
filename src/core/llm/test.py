import os
import base64
from pathlib import Path
import concurrent
import pandas as pd
import json
from openai import OpenAI
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL", "https://llm.padova.zucchettitest.it/"),
    api_key=os.getenv("OPENAI_API_KEY"),
    max_retries=0
)

def load_metrics(file_path):
    path = Path(file_path)
    if path.suffix == '.json':
        with open(path, 'r') as f:
            return json.dumps(json.load(f), indent=2)
    elif path.suffix == '.csv':
        df = pd.read_csv(path)
        return df.to_string(index=False)
    return "Nessuna metrica testuale disponibile."

def load_coefficients(file_path):
    path = Path(file_path)
    if path.suffix == '.json':
        with open(path, 'r') as f:
            return json.dumps(json.load(f), indent=2)
    elif path.suffix == '.csv':
        df = pd.read_csv(path)
        return df.to_string(index=False)
    return "Nessun coefficiente testuale disponibile."

def encode_image(image_path):
    logging.info(f"Start encoding image at path: {image_path}")
    """Codifica l'immagine in base64 gestendo i percorsi in modo sicuro."""
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"File non trovato: {image_path}")
        
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    
def fetch_model_response(model, role_sistem, prompt_text, base64_image):
    """Funzione helper per eseguire la singola chiamata API."""
    logging.info(f"Testing model with image support: {model}")
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt_text},
                        #{
                        #    "type": "image_url",
                        #    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                        #},
                    ],
                }
            ],
        )
        print(response)
        logging.info(f"API call successful for model: {model}-------------------------------------------------------------------------------------")
        return model, response.choices[0].message.content
    except Exception as e:
        logging.exception(f"Errore durante la chiamata API per {model}-------------------------------------------------------------------------------------: {e}")
        return model, f"Errore: {str(e)}"
    
def analyze_statistics(metrics_path, coefficients_path, image_path, algo_name, algo_type, dataset_description, algo_prompt):
    logging.info(f"Caricamento metriche da: {metrics_path}")
    raw_metrics = load_metrics(metrics_path)
    logging.info("Metriche caricate e formattate correttamente.")
    
    raw_coefficients = load_coefficients(coefficients_path)
    
    logging.info(f"Start analyzing statistics for image: {image_path}")
    base64_image = encode_image(image_path)
    logging.info("Image encoded successfully, preparing prompt for LLM.")

    model_list_img_supp = [
        "gemma4:e4b",
        "gemma3:1b",
        "qwen3.6:27b",
        "gemma3:27b",
        "gemma4:26b",
        "qwen3.5:2b",
    ]
    
    model_list_text = [
        "deepseek-r1:8b",
        "iodose/nuextract-v1.5:3.8b-q8_0",
        "deepseek-coder-v2:latest",
        "llama3.2:3b",
        "nomic-embed-text:latest",
        #"qwen3-embedding:0.6b",
        "devstral:24b",
        "NuExtract-2.0",
        "devstral-small-2:24b",
        "nomic-embed-text-v2-moe:latest",
        "gpt-oss:20b"
    ]
    
    model_list = model_list_img_supp + model_list_text

    role_sistem = "Sei un Data Translator e un consulente strategico. Il tuo compito è spiegare i risultati di un modello predittivo a un consiglio di amministrazione. L'obiettivo è generare fiducia nel modello e farne comprendere le logiche."

    prompt_text = (
        f"Contesto analisi:\n\n"
        f"ALGORITMO: {algo_name}\n"
        f"Tipo di algoritmo: {algo_type}\n"
        f"Descrizione del dataset: {dataset_description}\n"
        f"DATI NUMERICI:\n{raw_metrics}\n\n"
        f"COEFFICIENTI: \n{raw_coefficients}\n\n"
        f"ISTRUZIONI SPECIFICHE: {algo_prompt}\n"
        f"REGOLE FERREE DI SPIEGABILITÀ (Linee guida rigorose):\n"
        f"1. Semplicità e Brevità: Concentrati solo su un numero limitato di cause determinanti (massimo 3-5 feature). Ignora le variabili marginali o non causali.\n"
        f"2. Fedeltà alla Logica Umana: Usa un linguaggio umano e coerente con il dominio di business, adattando la spiegazione all'audience.\n"
        f"3. Causalità vs Correlazione: Chiarisci sempre che le feature individuate dal modello indicano correlazioni statistiche, ma non implicano necessariamente una causalità diretta.\n"
        f"4. Gestione Anomalie e Feature Support: Se noti valori estremi (outlier) o se la predizione sembra basarsi su dati insoliti, segnala che l'affidabilità (supporto) potrebbe essere bassa in quanto ci si allontana dai casi medi.\n"
        f"5. Spiegazione Contrastiva: Se i dati e l'immagine lo permettono, cerca di spiegare le differenze in modo contrastivo (es. 'perché l'istanza è positiva rispetto a quella negativa').\n\n"
        f"ISTRUZIONI GENERALI:\n"
        f"1. Riassumi l'affidabilità generale del modello in pochi passaggi, basandoti sui dati ma senza entrare nei dettagli tecnici.\n"
        f"2. Spiega in modo intuitivo i fattori (feature) principali che guidano le decisioni.\n"
        f"3. Analizza i dati e i grafici allegati per confermare se le decisioni del modello sono in linea con il buon senso aziendale."
        f"VINCOLI:\n"
        f"- Evita gergo tecnico eccessivo, punta a un linguaggio chiaro e accessibile.\n"
        f"- Non limitarti a ripetere i dati, ma fornisci un'interpretazione che li renda comprensibili e utili per decisioni strategiche."
        f"- Niente formulazioni matematiche esplicite."
    )
    
    results = {}
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = executor.map(
            lambda m: fetch_model_response(m, role_sistem, prompt_text, base64_image),
            model_list_text
        )
        
        for model_name, content in futures:
            results[model_name] = content

    return results

if __name__ == "__main__":
    IMAGE_PATH = Path(r"C:\Users\SOLLOR\Documents\ML-Algorithm-Interpretability\src\output\LR_Salary\correlation_matrix.png")
    METRICS_PATH = Path(r"C:\Users\SOLLOR\Documents\ML-Algorithm-Interpretability\src\output\LR_Salary\metriche.json")
    COEFFICIENTS_PATH = Path(r"C:\Users\SOLLOR\Documents\ML-Algorithm-Interpretability\src\output\LR_Salary\coefficienti.csv")
    
    risultati = analyze_statistics(
        METRICS_PATH, 
        COEFFICIENTS_PATH, 
        IMAGE_PATH, 
        algo_name="Linear Regression", 
        algo_type="Regressione", 
        dataset_description="Dataset con informazioni su studenti e i loro stipendi dopo la laurea.", 
        algo_prompt="Fornisci un'interpretazione dettagliata dei risultati della regressione lineare, spiegando l'importanza di ogni coefficiente e la qualità del modello."  
        )
    
    print("\n--- RISULTATI DEL TESTING ---")
    for modello, risposta in risultati.items():
        print(f"\n[{modello}]\n{risposta}\n{'-'*50}")