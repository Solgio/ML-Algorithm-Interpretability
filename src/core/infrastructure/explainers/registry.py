import importlib
import logging
from typing import Dict, Optional, Tuple, Type
from src.core.infrastructure.models.exceptions import ModelCreationError
from src.core.domain.enums import Algorithm, TaskType
from src.core.infrastructure.explainers.base import Explainer

class ExplainerRegistry:
    """Registry for explainers, allowing dynamic registration and retrieval of explainer classes based on algorithm types."""
    _registry: Dict[Tuple[Algorithm, TaskType], Explainer] = {}
    
    @classmethod
    def register(cls, algorithm: Algorithm, task_type: TaskType, module_path: str, explainer_class: str, description: str):
        """Register a new explainer class for a specific algorithm and task type."""
        key = (algorithm, task_type)
        if key in cls._registry:
            logging.warning(f"Overwriting existing explainer registration for {algorithm} ({task_type})")
        cls._registry[key] = explainer_class
        logging.info(f"Registered explainer for {algorithm} ({task_type}): {description}")
    
    @classmethod
    def get(cls, algorithm: Algorithm, task_type: TaskType) -> Optional[Type[Explainer]]:
        """Retrieve an explainer instance based on the algorithm and task type."""
        registry_entry = cls._registry.get((algorithm, task_type))
        if registry_entry is None:
            raise ValueError(f"No explainer registered for {algorithm} ({task_type})")
        
        try:
            return cls._registry[(algorithm, task_type)]
        except ModuleNotFoundError as e:
            raise ModelCreationError(str(algorithm), f"module '{registry_entry.module_path}' not found", e)
        except Exception as e:
            raise ModelCreationError(str(algorithm), f"unexpected error during module import: {registry_entry.module_path}", e)
    
    @classmethod
    def list_registered(cls)-> Dict[str, str]:
        """List all registered explainers with their descriptions."""
        return {
                f"{k[0]}_{k[1]}": v.__name__
                for k, v in cls._registry.items()
            }
        
    @classmethod
    def clear(cls):
        """Clear all registered explainers (useful for testing)."""
        cls._registry.clear()