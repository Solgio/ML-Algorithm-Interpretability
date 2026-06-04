

from enum import Enum
import logging
from src.core.domain.enums import TaskType, Algorithm


class ExplainerStrategy(Enum):
    """Enum for supported explainer strategies."""
    TREE = "tree"
    KERNEL = "kernel"
    
    def __str__(self):
        """ User-friendly string representation of the explainer strategy. """
        return self.value
    
def select_explainer_strategy(algorithm: Algorithm, task_type: TaskType) -> ExplainerStrategy:
    """Select the appropriate explainer strategy based on the model class name and task type."""
    tree_based_models = {
            Algorithm.DECISION_TREE_CLASSIFIER,
            Algorithm.DECISION_TREE_REGRESSOR,
            Algorithm.RANDOM_FOREST_CLASSIFIER, 
            Algorithm.RANDOM_FOREST_REGRESSOR,
            Algorithm.XGBOOST_REGRESSOR,
            Algorithm.XGBOOST_CLASSIFIER,
        }
    
    kernel_classif_only = { 
            Algorithm.LOGISTIC_REGRESSION,
            Algorithm.SVM
        }
    
    kernel_regr_only = {
            Algorithm.LINEAR_REGRESSION,
            Algorithm.SYMBOLIC_REGRESSOR
        }
    
    if algorithm in tree_based_models:
        return ExplainerStrategy.TREE
    elif algorithm in kernel_classif_only:
        if task_type != TaskType.CLASSIFICATION:
            raise ValueError(
                f"{algorithm} è supportato solo per Classification, "
                f"non per {task_type.value}"
            )
        logging.info(f"KernelExplainer (classification-only kernel model)")
        return ExplainerStrategy.KERNEL
    
    elif algorithm in kernel_regr_only:
        if task_type != TaskType.REGRESSION:
            raise ValueError(
                f"{algorithm} è supportato solo per Regression, "
                f"non per {task_type.value}"
            )
        logging.info(f"KernelExplainer (regression-only kernel model)")
        return ExplainerStrategy.KERNEL
    
    else:
        logging.warning(f"Model class '{algorithm}' non riconosciuto tra quelli supportati, "
                        f"assegnando per default KernelExplainer")
        return ExplainerStrategy.KERNEL