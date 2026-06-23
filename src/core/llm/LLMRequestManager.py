import os
import logging
from pathlib import Path
from dotenv import load_dotenv

from src.core.llm.LLMDataWarehouse import model_list_img_supp
from src.core.llm.services import OpenAILLMService
from src.core.llm.strategies import AlgorithmWiseStrategy, LLMWiseStrategy
from src.core.llm.orchestrator_context import LLMOrchestrator

logger = logging.getLogger("LLM_Facade")
env_path = Path(__file__).resolve().parents[2] / '.env' 
load_dotenv(dotenv_path=env_path)

def analyze_statistics(
    metrics_path, 
    coefficients_path, 
    image_path, 
    algo_name, 
    algo_type, 
    dataset_description, 
    user_prompt, 
    algo_prompt, 
    model_list=None
):
    """Facade for legacy Algorithm-wise requests."""
    # Convert image path to list if it's not a list, for safety
    if isinstance(image_path, (str, Path)):
        image_paths = [image_path]
    elif image_path is None:
        image_paths = []
    else:
        image_paths = list(image_path)

    task = {
        "algo_name": algo_name,
        "algo_type": algo_type,
        "dataset_description": dataset_description,
        "user_prompt": user_prompt,
        "algo_prompt": algo_prompt,
        "metrics_path": metrics_path,
        "coefficients_path": coefficients_path or metrics_path,
        "image_paths": image_paths
    }
    
    models = model_list if model_list is not None else model_list_img_supp
    
    # Instantiate service and orchestrator lazily to avoid module-level initialization side-effects
    llm_service = OpenAILLMService()
    orchestrator = LLMOrchestrator(AlgorithmWiseStrategy(), llm_service)
    results = orchestrator.run([task], models)
    
    # Legacy output format expects {model_name: response} for the single algorithm
    return results.get(algo_name, {})


def analyze_statistics_llm_wise(tasks, model_list=None):
    """Facade for LLM-wise requests."""
    models = model_list if model_list is not None else model_list_img_supp
    
    # Normalize tasks: convert image_paths to list if it isn't already
    normalized_tasks = []
    for task in tasks:
        t = task.copy()
        if "image_paths" in t:
            if isinstance(t["image_paths"], (str, Path)):
                t["image_paths"] = [t["image_paths"]]
            elif t["image_paths"] is None:
                t["image_paths"] = []
            else:
                t["image_paths"] = list(t["image_paths"])
        else:
            t["image_paths"] = []
        normalized_tasks.append(t)
        
    # Instantiate service and orchestrator lazily
    llm_service = OpenAILLMService()
    orchestrator = LLMOrchestrator(LLMWiseStrategy(), llm_service)
    return orchestrator.run(normalized_tasks, models)


if __name__ == "__main__":
    IMAGE_PATH = Path(r"src/output/LR_Salary/correlation_matrix.png")
    METRICS_PATH = Path(r"src/output/LR_Salary/metriche.json")
    COEFFICIENTS_PATH = Path(r"src/output/LR_Salary/coefficienti.csv")
    
    # To run test, ensure files exist. Facade runs new SOLID classes behind the scenes
    risultati = analyze_statistics(
        METRICS_PATH, 
        COEFFICIENTS_PATH, 
        [IMAGE_PATH] if IMAGE_PATH.exists() else [], 
        algo_name="Linear Regression", 
        algo_type="Regression", 
        dataset_description="Dataset with information about students and their salaries after graduation.", 
        user_prompt="I expect the model to identify cgpa as the most important variable.",
        algo_prompt="Provide a detailed interpretation of the linear regression results, explaining the importance of each coefficient and the model quality."  
    )
    
    print("\n--- TESTING RESULTS ---")
    for modello, risposta in risultati.items():
        print(f"\n[{modello}]\n{risposta}\n{'-'*50}")