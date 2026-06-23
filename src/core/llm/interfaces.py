from abc import ABC, abstractmethod

class LLMService(ABC):
    """Abstract interface for LLM service providers."""
    
    @abstractmethod
    def generate_response(
        self, 
        model: str, 
        system_prompt: str, 
        user_prompt: str, 
        images: list[str] = None
    ) -> str:
        """Query the LLM provider for a response.
        
        Args:
            model (str): Name of the model to use.
            system_prompt (str): System prompt.
            user_prompt (str): User prompt text.
            images (list[str], optional): List of base64-encoded image strings. Defaults to None.
            
        Returns:
            str: Generated text response from the model.
        """
        pass


class OrchestrationStrategy(ABC):
    """Abstract interface for LLM orchestration strategies (e.g. Algorithm-wise or LLM-wise)."""
    
    @abstractmethod
    def execute(
        self, 
        tasks: list[dict], 
        models: list[str], 
        llm_service: LLMService
    ) -> dict:
        """Execute the LLM analysis requests using the selected orchestration strategy.
        
        Args:
            tasks (list[dict]): A list of task parameters (e.g., algorithm details, metrics path, coefficients path, image paths).
            models (list[str]): List of LLM models to query.
            llm_service (LLMService): Concrete LLM service implementation.
            
        Returns:
            dict: Analysis results mapping algorithms/models to their generated responses.
        """
        pass
