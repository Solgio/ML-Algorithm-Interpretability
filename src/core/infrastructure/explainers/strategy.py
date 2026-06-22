

import logging
from enum import Enum
from typing import Dict, Optional, Set

from src.core.domain.enums import TaskType, Algorithm


class ExplainerStrategy(Enum):
    """Enum for supported explainer strategies."""
    TREE = "tree"
    KERNEL = "kernel"
    
    def __str__(self):
        """ User-friendly string representation of the explainer strategy. """
        return self.value


_ALGORITHM_STRATEGY_REGISTRY: Dict[Algorithm, ExplainerStrategy] = {}
_ALGORITHM_TASK_CONSTRAINTS: Dict[Algorithm, Set[TaskType]] = {}


def register_explainer_strategy(
    algorithm: Algorithm,
    strategy: ExplainerStrategy,
    allowed_tasks: Optional[Set[TaskType]] = None,
) -> None:
    """Register the explainer strategy for an algorithm."""
    _ALGORITHM_STRATEGY_REGISTRY[algorithm] = strategy
    if allowed_tasks is not None:
        _ALGORITHM_TASK_CONSTRAINTS[algorithm] = set(allowed_tasks)


def _register_default_strategies() -> None:
    tree_algorithms = {
        Algorithm.DECISION_TREE_CLASSIFIER,
        Algorithm.DECISION_TREE_REGRESSOR,
        Algorithm.RANDOM_FOREST_CLASSIFIER,
        Algorithm.RANDOM_FOREST_REGRESSOR,
        Algorithm.XGBOOST_REGRESSOR,
        Algorithm.XGBOOST_CLASSIFIER,
    }

    kernel_classification_algorithms = {
        Algorithm.LOGISTIC_REGRESSION,
        Algorithm.SVM,
    }

    kernel_regression_algorithms = {
        Algorithm.LINEAR_REGRESSION,
        Algorithm.SYMBOLIC_REGRESSOR,
    }

    for algorithm in tree_algorithms:
        register_explainer_strategy(algorithm, ExplainerStrategy.TREE)

    for algorithm in kernel_classification_algorithms:
        register_explainer_strategy(
            algorithm,
            ExplainerStrategy.KERNEL,
            allowed_tasks={TaskType.CLASSIFICATION},
        )

    for algorithm in kernel_regression_algorithms:
        register_explainer_strategy(
            algorithm,
            ExplainerStrategy.KERNEL,
            allowed_tasks={TaskType.REGRESSION},
        )


_register_default_strategies()
    
def select_explainer_strategy(algorithm: Algorithm, task_type: TaskType) -> ExplainerStrategy:
    """Select the appropriate explainer strategy for the given algorithm and task."""
    if algorithm not in _ALGORITHM_STRATEGY_REGISTRY:
        raise ValueError(f"No explainer strategy registered for {algorithm}")

    allowed_tasks = _ALGORITHM_TASK_CONSTRAINTS.get(algorithm)
    if allowed_tasks is not None and task_type not in allowed_tasks:
        allowed_task_names = ", ".join(sorted(task.value for task in allowed_tasks))
        raise ValueError(
            f"{algorithm} is supported only for {allowed_task_names}, not for {task_type.value}"
        )

    strategy = _ALGORITHM_STRATEGY_REGISTRY[algorithm]
    logging.info("Selected SHAP strategy '%s' for algorithm '%s'", strategy, algorithm)
    return strategy