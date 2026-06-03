
import importlib
import logging
from typing import Dict, List, Optional, Tuple
from domain.enums import Algorithm, TaskType
from domain.value_object import AlgorithmRegistry
from infrastructure.models.exceptions import ModelRegistrationError, ModelCreationError, ModelNotFoundError

class ModelFactory:
    """Factory class for creating model instances."""
    
    _registry: Dict[Tuple[Algorithm, TaskType], AlgorithmRegistry] = {}
    
    @classmethod
    def register(cls,registry_entry: AlgorithmRegistry):
        """Register a new algorithm in the factory."""
        try:
            registry_entry.validate()
        except ValueError as e:
            raise ModelRegistrationError(registry_entry.algorithm, registry_entry.task_type, str(e))
        key = (registry_entry.algorithm, registry_entry.task_type)
        if key in cls._registry:
            logging.warning(f"Overwriting existing registry entry for {registry_entry.algorithm} ({registry_entry.task_type})")
        cls._registry[key] = registry_entry
        logging.info(f"Registered algorithm: {registry_entry.algorithm} for task: {registry_entry.task_type}")
        
    
    @classmethod
    def create(cls, algorithm: Algorithm, task_type: TaskType, dataset: str, dataset_path: str, param_grid: Optional[Dict] = None):
        """Create an instance of the specified algorithm for the given task type."""
        if not isinstance(algorithm, Algorithm):
            raise TypeError(f"algorithm must be an instance of Algorithm enum, got {type(algorithm)}")
        if not isinstance(task_type, TaskType):
            raise TypeError(f"task_type must be an instance of TaskType enum, got {type(task_type)}")
        
        key = (algorithm, task_type)
        if key not in cls._registry:
            available_algorithms = [f"{alg} ({tt})" for (alg, tt) in cls._registry.keys()]
            raise ModelNotFoundError(algorithm, task_type, available_algorithms)
        
        registry_entry = cls._registry[key]
        logging.info(f"Model creation: {algorithm} for task: {task_type} using module: {registry_entry.module_path}")
        try:
            module=importlib.import_module(registry_entry.module_path)
            
        except ModuleNotFoundError as e:
            raise ModelCreationError(str(algorithm), f"module import failed for {registry_entry.module_path}", e)
        except Exception as e:
            raise ModelCreationError(str(algorithm), f"unexpected error during module import: {registry_entry.module_path}", e)
        
        try:
            model_class = getattr(module, registry_entry.class_name)
        except AttributeError as e:
            raise ModelCreationError(str(algorithm), f"class '{registry_entry.class_name}' not found in module '{registry_entry.module_path}'", e)
        except Exception as e:
            raise ModelCreationError(str(algorithm), f"unexpected error during class retrieval: {registry_entry.class_name} from {registry_entry.module_path}", e)
        
        try:
            model_instance = model_class(
                dataset=dataset,
                dataset_path=dataset_path,
                param_grid=registry_entry.param_grid
            )
            logging.info(f"Successfully created model instance for {algorithm} ({task_type})")
            return model_instance
        except TypeError as e:
            raise ModelCreationError(str(algorithm), f"TypeError occurred while creating model instance: {e}", e)
        except Exception as e:
            raise ModelCreationError(str(algorithm), f"Unexpected error occurred while creating model instance: {e}", e)
        
    @classmethod
    def list_algorithms(cls, task_type: Optional[TaskType]=None) -> List[str]:
        """List all registered algorithms, optionally filtered by task type."""
        if task_type is None:
            algos = set()
            for algo, _ in cls._registry.keys():
                algos.add(str(algo))
            return sorted(list(algos))
        else:
            algos = []
            for algo, task in cls._registry.keys():
                if task == task_type:
                    algos.append(str(algo))
            return algos
        
    @classmethod
    def get_registry(cls) -> Dict:
        """Get the entire registry of algorithms."""
        return {
            f"{k[0].value}_{k[1].value}": {
                "algorithm": str(k[0]),
                "task_type": str(k[1]),
                "module": v.module_path,
                "class": v.class_name,
                "description": v.description,
            }
            for k, v in cls._registry.items()
        }
        
    @classmethod
    def is_registered(cls, algorithm: Algorithm, task_type: TaskType) -> bool:
        """Check if a given algorithm and task type combination is registered."""
        return (algorithm, task_type) in cls._registry
    
    @classmethod
    def get_description(cls, algorithm: Algorithm, task_type: TaskType) -> str:
        """Get the description of a registered algorithm."""
        key = (algorithm, task_type)
        if key not in cls._registry:
            return "Algoritmo non registrato"
        return cls._registry[key].description
    
    @classmethod
    def get_param_grid(cls, algorithm: Algorithm, task_type: TaskType) -> Optional[Dict]:
        """Get the hyperparameter grid for a registered algorithm, if any."""
        key = (algorithm, task_type)
        if key not in cls._registry:
            return None
        return cls._registry[key].param_grid
    
    @classmethod
    def get_prompt(cls, algorithm: Algorithm, task_type: TaskType) -> Optional[str]:
        """Get the prompt associated with a registered algorithm, if any."""
        key = (algorithm, task_type)
        if key not in cls._registry:
            return None
        return cls._registry[key].prompt
    
    @classmethod
    def get_all_info(cls, algorithm: Algorithm, task_type: TaskType) -> Dict:
        """Get the full registry entry for a given algorithm and task type."""
        key = (algorithm, task_type)
        if key not in cls._registry:
            raise ModelNotFoundError(str(algorithm), str(task_type))

        registry_entry = cls._registry[key]
        return {
            "algorithm": str(registry_entry.algorithm),
            "task_type": str(registry_entry.task_type),
            "description": registry_entry.description,
            "prompt": registry_entry.prompt,
            "param_grid": registry_entry.param_grid,
            "module": registry_entry.module_path,
            "class": registry_entry.class_name,
        }
        
    @classmethod
    def clear(cls):
        """Clear the entire registry (useful for testing)."""
        cls._registry.clear()
        logging.info("Cleared the model registry.")