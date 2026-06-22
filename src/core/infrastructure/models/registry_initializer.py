import logging
from src.core.domain.enums import Algorithm, TaskType
from src.core.domain.value_object import AlgorithmRegistry
from src.core.infrastructure.models.model_factory import ModelFactory

logger = logging.getLogger(__name__)
base_model_path = "src.core.models."

def initialize_model_registry() -> None:
    """Initialize the model registry with predefined algorithms."""
    
    logger.info("Initializing ModelFactory registry...")
    
    # Linear Regression
    ModelFactory.register(AlgorithmRegistry(
        algorithm=Algorithm.LINEAR_REGRESSION,
        task_type=TaskType.REGRESSION,
        module_path=base_model_path + "LR",
        class_name="LinearRegression",
        description="OLS Linear Regression (sklearn)",
        prompt=(
            "This model has very high intrinsic transparency and its parameters "
            "are directly interpretable. Explain the impact (magnitude) and direction "
            "(positive or negative sign) of the main coefficients. Describe how the "
            "unit increase of a factor causes a proportional variation in the final prediction, "
            "but warn that these are correlations and not absolute causal laws."
        ),
    ))
    
    # Decision Tree Regressor
    ModelFactory.register(AlgorithmRegistry(
        algorithm=Algorithm.DECISION_TREE_REGRESSOR,
        task_type=TaskType.REGRESSION,
        module_path=base_model_path + "DecTree",
        class_name="DecisionTreeR",
        description="Decision Tree for regression (sklearn)",
        prompt=(
            "This model possesses high local traceability based on structural "
            "explainability. Explain decisions as a sequence of 'if... then' logical rules "
            "(decision path) that faithfully reflect human reasoning. Use global "
            "feature importance to highlight the fundamental splitting criterion "
            "at the top of the tree."
        ),
        param_grid={
            'criterion': ['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
            'max_depth': [None, 5, 10, 20],
            'min_samples_split': [2, 10],
            'min_samples_leaf': [1, 4],
            'ccp_alpha': [0.0, 0.1]
        }
    ))
    
    # Random Forest Regressor
    ModelFactory.register(AlgorithmRegistry(
        algorithm=Algorithm.RANDOM_FOREST_REGRESSOR,
        task_type=TaskType.REGRESSION,
        module_path=base_model_path + "RandForest",
        class_name="RandomForestR",
        description="Random Forest for regression (sklearn)",
        prompt=(
            "This model is an 'Ensemble' with medium transparency, requiring the use of "
            "feature importance (post-hoc explainability) to be understood. Explain that the algorithm "
            "creates many parallel scenarios and makes decisions by majority. The main factors "
            "identified represent the arguments that convinced the majority, compensating "
            "for any errors of individuals."
        ),
        param_grid={
            'n_estimators': [100, 200],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 10],
            'min_samples_leaf': [1, 4],
            'max_features': ['sqrt', 'log2'],
            'ccp_alpha': [0.0, 0.1],
            'criterion': ['squared_error', 'absolute_error', 'friedman_mse', 'poisson'],
            'min_impurity_decrease': [0.0, 0.1]
        }
    ))
    
    # XGBoost Regressor
    ModelFactory.register(AlgorithmRegistry(
        algorithm=Algorithm.XGBOOST_REGRESSOR,
        task_type=TaskType.REGRESSION,
        module_path=base_model_path + "XGBoost",
        class_name="XGBoostR",
        description="XGBoost for regression",
        prompt=(
            "This model has low intrinsic transparency (opaque model) and relies on "
            "post-hoc explanations. Explain that the algorithm proceeds in successive steps, "
            "focusing progressively on the most difficult cases. Use feature importance "
            "to illustrate which variables were most useful in correcting errors during "
            "this learning process."
        ),
        param_grid={
            'n_estimators': [100, 300],
            'max_depth': [3, 10],
            'learning_rate': [0.01, 0.2],
            'subsample': [0.8, 1.0],
            'colsample_bytree': [0.6, 1.0],
            'gamma': [0, 0.2]
        }
    ))
    
    #Symbolic Regressor
    ModelFactory.register(AlgorithmRegistry(
        algorithm=Algorithm.SYMBOLIC_REGRESSOR,
        task_type=TaskType.REGRESSION,
        module_path=base_model_path + "SymbR",
        class_name="SymbolicRegressor",
        description="Symbolic Regressor (pysr)",
        
    ))
    # Logistic Regression
    ModelFactory.register(AlgorithmRegistry(
        algorithm=Algorithm.LOGISTIC_REGRESSION,
        task_type=TaskType.CLASSIFICATION,
        module_path=base_model_path + "LogR",
        class_name="LogisticRegression",
        description="Logistic Regression (sklearn)",
        prompt=(
            "This model offers a probabilistic type of explainability. Do not talk about logarithms, "
            "but explain how the increase of a specific variable multiplies the probabilities (odds ratio) "
            "of an event occurring. Comment on the model's certainty by remembering that probabilities "
            "very close to 0 or 100 indicate high confidence."
        ),
        param_grid={
            'C': [0.1, 1, 10],
            'penalty': ['l1', 'l2'],
            'solver': ['liblinear', 'saga']
        }
    ))
    
    # SVM
    ModelFactory.register(AlgorithmRegistry(
        algorithm=Algorithm.SVM,
        task_type=TaskType.CLASSIFICATION,
        module_path=base_model_path + "SVM",
        class_name="SVM",
        description="Support Vector Machine (sklearn.svm.SVC)",
        prompt=(
            "This is an opaque model with low transparency. Explain that the algorithm ignores "
            "obvious cases and searches for the optimal boundary line by focusing only on borderline "
            "instances, i.e., the most ambiguous ones (support vectors). Use the most important features "
            "to explain which 'coordinates' define this critical boundary."
        ),
        param_grid={
            'C': [0.1, 1, 10, 100],
            'gamma': ['scale', 'auto', 0.1, 0.01, 0.001, 0.0001],
            'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],
            'class_weight': [None, 'balanced'],
            'degree': [2, 4]
        }
    ))
    
    # Decision Tree Classifier
    ModelFactory.register(AlgorithmRegistry(
        algorithm=Algorithm.DECISION_TREE_CLASSIFIER,
        task_type=TaskType.CLASSIFICATION,
        module_path=base_model_path + "DecTree",
        class_name="DecisionTreeC",
        description="Decision Tree for classification (sklearn)",
        prompt=(
            "This model possesses high local traceability based on structural "
            "explainability. Explain decisions as a sequence of 'if... then' logical rules "
            "(decision path) that faithfully reflect human reasoning. Use global "
            "feature importance to highlight the fundamental splitting criterion "
            "at the top of the tree."
        ),
        param_grid={
            'criterion': ['gini', 'entropy', 'log_loss'],
            'max_depth': [None, 5, 20],
            'min_samples_split': [2, 10],
            'min_samples_leaf': [1, 4],
            'ccp_alpha': [0.0, 0.1]
        }
    ))
    
    # Random Forest Classifier
    ModelFactory.register(AlgorithmRegistry(
        algorithm=Algorithm.RANDOM_FOREST_CLASSIFIER,
        task_type=TaskType.CLASSIFICATION,
        module_path=base_model_path + "RandForest",
        class_name="RandomForestC",
        description="Random Forest for classification (sklearn)",
        prompt=(
            "This model is an 'Ensemble' with medium transparency, requiring the use of "
            "feature importance (post-hoc explainability) to be understood. Explain that the algorithm "
            "creates many parallel scenarios and makes decisions by majority. The main factors "
            "identified represent the arguments that convinced the majority, compensating "
            "for any errors of individuals."
        ),
        param_grid={
            'n_estimators': [100, 200],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 10],
            'min_samples_leaf': [1, 4],
            'max_features': ['sqrt', 'log2'],
            'ccp_alpha': [0.0, 0.1],
            'criterion': ['gini', 'entropy'],
            'min_impurity_decrease': [0.0, 0.1]
        }
    ))
    
    # XGBoost Classifier
    ModelFactory.register(AlgorithmRegistry(
        algorithm=Algorithm.XGBOOST_CLASSIFIER,
        task_type=TaskType.CLASSIFICATION,
        module_path=base_model_path + "XGBoost",
        class_name="XGBoostC",
        description="XGBoost for classification",
        prompt=(
            "This model has low intrinsic transparency (opaque model) and relies on "
            "post-hoc explanations. Explain that the algorithm proceeds in successive steps, "
            "focusing progressively on the most difficult cases. Use feature importance "
            "to illustrate which variables were most useful in correcting errors during "
            "this learning process."
        ),
        param_grid={
            'n_estimators': [100, 300],
            'max_depth': [3, 10],
            'learning_rate': [0.01, 0.2],
            'subsample': [0.8, 1.0],
            'colsample_bytree': [0.6, 1.0],
            'gamma': [0, 0.2]
        }
    ))
    
    logger.info(f"✓ Registry initialized with {len(ModelFactory.get_registry())} algorithms")