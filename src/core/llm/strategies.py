import logging
from src.core.llm.interfaces import OrchestrationStrategy, LLMService
from src.core.llm.services import DataPreparationService, PromptBuilder
from src.core.llm.LLMDataWarehouse import role_sistem, general_prompt

logger = logging.getLogger("LLM_Strategies")

class AlgorithmWiseStrategy(OrchestrationStrategy):
    """Executes requests algorithm-wise: for each algorithm, runs all models sequentially."""
    
    def execute(
        self, 
        tasks: list[dict], 
        models: list[str], 
        llm_service: LLMService
    ) -> dict:
        results = {}
        
        for task in tasks:
            algo_name = task["algo_name"]
            results[algo_name] = {}
            
            logger.info(f"Processing algorithm-wise analysis for algorithm: {algo_name}")
            
            # Prepare task data once
            raw_metrics = DataPreparationService.load_metrics(task["metrics_path"])
            raw_coefficients = DataPreparationService.load_coefficients(task["coefficients_path"])
            base64_images = DataPreparationService.encode_images(task["image_paths"])
            
            prompt_text = PromptBuilder.build_prompt(
                algo_name=algo_name,
                algo_type=task["algo_type"],
                dataset_description=task["dataset_description"],
                user_prompt=task["user_prompt"],
                algo_prompt=task["algo_prompt"],
                raw_metrics=raw_metrics,
                raw_coefficients=raw_coefficients,
                general_prompt=general_prompt
            )
            
            # Loop through models
            for model in models:
                response = llm_service.generate_response(
                    model=model,
                    system_prompt=role_sistem,
                    user_prompt=prompt_text,
                    images=base64_images
                )
                results[algo_name][model] = response
                
        return results


class LLMWiseStrategy(OrchestrationStrategy):
    """Executes requests LLM-wise: for each LLM model, runs all algorithms sequentially."""
    
    def execute(
        self, 
        tasks: list[dict], 
        models: list[str], 
        llm_service: LLMService
    ) -> dict:
        results = {}
        
        # Prepare all task data upfront to avoid re-reading files for each model
        prepared_tasks = []
        for task in tasks:
            algo_name = task["algo_name"]
            results[algo_name] = {}
            
            raw_metrics = DataPreparationService.load_metrics(task["metrics_path"])
            raw_coefficients = DataPreparationService.load_coefficients(task["coefficients_path"])
            base64_images = DataPreparationService.encode_images(task["image_paths"])
            
            prompt_text = PromptBuilder.build_prompt(
                algo_name=algo_name,
                algo_type=task["algo_type"],
                dataset_description=task["dataset_description"],
                user_prompt=task["user_prompt"],
                algo_prompt=task["algo_prompt"],
                raw_metrics=raw_metrics,
                raw_coefficients=raw_coefficients,
                general_prompt=general_prompt
            )
            
            prepared_tasks.append({
                "algo_name": algo_name,
                "prompt_text": prompt_text,
                "images": base64_images
            })
            
        # Loop outer: models (loads each model once)
        for model in models:
            logger.info(f"=== Starting batch for model: {model} ===")
            # Loop inner: tasks (evaluates all algorithms)
            for prep in prepared_tasks:
                algo_name = prep["algo_name"]
                response = llm_service.generate_response(
                    model=model,
                    system_prompt=role_sistem,
                    user_prompt=prep["prompt_text"],
                    images=prep["images"]
                )
                results[algo_name][model] = response
                
        return results
