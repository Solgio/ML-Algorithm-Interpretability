import os
import base64
from pathlib import Path
import concurrent
import pandas as pd
import json
from openai import OpenAI
from dotenv import load_dotenv
import logging
from src.core.llm.LLMDataWarehouse import role_sistem, general_prompt, model_list_img_supp, model_list_text

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
    return "No textual metrics available."

def load_coefficients(file_path):
    path = Path(file_path)
    if path.suffix == '.json':
        with open(path, 'r') as f:
            return json.dumps(json.load(f), indent=2)
    elif path.suffix == '.csv':
        df = pd.read_csv(path)
        return df.to_string(index=False)
    return "No textual coefficients available."

def encode_image(image_path):
    encoded_images = []
    
    for img_path in image_path:
        logging.info(f"Start encoding image at path: {img_path}")
        """Encode the image in base64, handling paths safely."""
        path = Path(img_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {img_path}")
        with open(path, "rb") as image_file:
            encoded_images.append(base64.b64encode(image_file.read()).decode("utf-8"))
    return encoded_images
    
def fetch_model_response(model, role_sistem, prompt_text, base64_image):
    """Helper function to perform a single API call."""
    logging.info(f"Testing model with image support: {model}")
    message_content = [{
        "type": "text",
        "text": prompt_text
    }]
    
    for img in base64_image:
        message_content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{img}"}
        })
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": role_sistem
                },
                {
                    "role": "user",
                    "content": message_content
                }
            ],
        )
        print(response)
        logging.info(f"API call successful for model: {model}-------------------------------------------------------------------------------------")
        return model, response.choices[0].message.content
    
    except Exception as e:
        logging.exception(f"Error during API call for {model}-------------------------------------------------------------------------------------: {e}")
        return model, f"Error: {str(e)}"
    
def analyze_statistics(metrics_path, coefficients_path, image_path, algo_name, algo_type, dataset_description, user_prompt, algo_prompt):
    logging.info(f"Loading metrics from: {metrics_path}")
    raw_metrics = load_metrics(metrics_path)
    logging.info("Metrics loaded and formatted correctly.")
    
    raw_coefficients = load_coefficients(coefficients_path)
    
    logging.info(f"Start analyzing statistics for image: {image_path}")
    base64_images = encode_image(image_path)
    logging.info("Image encoded successfully, preparing prompt for LLM.")

    prompt_text = (
        f"Analysis context:\n\n"
        f"# ALGORITHM: {algo_name}\n"
        f"## Algorithm type: {algo_type}\n"
        f"## Dataset description: {dataset_description}\n"
        f"## User expectations: {user_prompt}\n\n"
        f"# NUMERICAL DATA:\n{raw_metrics}\n\n"
        f"# COEFFICIENTS: \n{raw_coefficients}\n\n"
        f"# SPECIFIC INSTRUCTIONS: {algo_prompt}\n"
        f"{general_prompt}\n"
    )
    
    results = {}
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        futures = {
            executor.submit(fetch_model_response, m, role_sistem, prompt_text, base64_images): m 
            for m in model_list_img_supp #+ model_list_text
        }
        
        for future in concurrent.futures.as_completed(futures):
            model_name = futures[future]
            try:
                model_name, content = future.result()
                results[model_name] = content
            except Exception as e:
                logging.exception(f"Exception for model {model_name}: {e}")
                results[model_name] = f"Error: {str(e)}"

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
        algo_type="Regression", 
        dataset_description="Dataset with information about students and their salaries after graduation.", 
        user_prompt="I expect the model to identify cgpa as the most important variable.",
        algo_prompt="Provide a detailed interpretation of the linear regression results, explaining the importance of each coefficient and the model quality."  
        )
    
    print("\n--- TESTING RESULTS ---")
    for modello, risposta in risultati.items():
        print(f"\n[{modello}]\n{risposta}\n{'-'*50}")