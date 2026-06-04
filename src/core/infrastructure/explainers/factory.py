
import logging

from shap import Explainer

from src.core.domain.enums import Algorithm, TaskType
from src.core.infrastructure.explainers.strategies.shap_tree_explainer import SHAPTreeExplainer
from src.core.infrastructure.explainers.strategies.shap_kernel_explainer import SHAPKernelExplainer
from src.core.infrastructure.explainers.registry import ExplainerRegistry

class ExplainerFactory:
    """Factory class to create explainer instances based on registered explainers."""
    
    @classmethod
    def initiate(cls)-> None:
        """Initialize the factory by importing all explainer modules to ensure they are registered."""
        
        tree_algorithms = [
            Algorithm.DECISION_TREE_CLASSIFIER,
            Algorithm.DECISION_TREE_REGRESSOR,
            Algorithm.RANDOM_FOREST_CLASSIFIER, 
            Algorithm.RANDOM_FOREST_REGRESSOR,
            Algorithm.XGBOOST_REGRESSOR,
            Algorithm.XGBOOST_CLASSIFIER,
        ]
        for algo in tree_algorithms:
            task = TaskType.CLASSIFICATION if "CLASSIFIER" in algo.value else TaskType.REGRESSION
            ExplainerRegistry.register(algo, task, SHAPTreeExplainer)
            
        kernel_algorithms = [
            Algorithm.LINEAR_REGRESSION,
            Algorithm.LOGISTIC_REGRESSION,
            Algorithm.SVM,
            Algorithm.SYMBOLIC_REGRESSOR
        ]
        for algo in kernel_algorithms:
            task = TaskType.CLASSIFICATION if "CLASSIFIER" in algo.value else TaskType.REGRESSION
            ExplainerRegistry.register(algo, task, SHAPKernelExplainer)
            
        logging.info("ExplainerFactory initialized with registered explainers for tree-based and kernel-based algorithms.")
        
    @classmethod
    def create(cls, algorithm: Algorithm, task_type: TaskType, shap_lib=None) -> Explainer:
        """Create an explainer instance based on the registered explainers."""
        explainer_class = ExplainerRegistry.get(algorithm, task_type)
        if explainer_class is None:
            available = ExplainerRegistry.list_registered()
            raise ValueError(
                f"No explainer registered for {algorithm} ({task_type})\n"
                f"Available: {available}"
            )
        
        logging.info(f"Creating {explainer_class.__name__} for {algorithm}")
        
        if shap_lib is not None:
            return explainer_class(shap_lib=shap_lib)
        else:
            return explainer_class()
        
    @classmethod
    def list_algorithms(cls)->dict:
        """List all registered explainers with their descriptions."""
        return ExplainerRegistry.list_registered()
    
        