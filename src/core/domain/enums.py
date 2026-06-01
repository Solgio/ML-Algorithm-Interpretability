
from enum import Enum

class Algorithm(Enum):
    """Enum for supported algorithms."""
    LINEAR_REGRESSION = "linear_regression"
    LOGISTIC_REGRESSION = "logistic_regression"
    DECISION_TREE_CLASSIFIER = "decision_tree_classifier"
    DECISION_TREE_REGRESSOR = "decision_tree_regressor"
    RANDOM_FOREST_CLASSIFIER = "random_forest_classifier"
    RANDOM_FOREST_REGRESSOR = "random_forest_regressor"
    SVM = "svm"
    XGBOOST_CLASSIFIER = "xgboost_classifier"
    XGBOOST_REGRESSOR = "xgboost_regressor"
    
    def __str__(self):
        """ User-friendly string representation of the algorithm. """
        return self.value.replace("_", " ").title()
    
class TaskType(Enum):
    """Enum for supported task types."""
    CLASSIFICATION = "classification"
    REGRESSION = "regression"
    
    def __str__(self):
        """ User-friendly string representation of the task type. """
        return self.value.title()