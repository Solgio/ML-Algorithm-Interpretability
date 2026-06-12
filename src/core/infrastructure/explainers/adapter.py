from typing import Dict, Iterable
import logging
import pandas as pd
from src.core.domain.enums import Algorithm, TaskType
from src.core.infrastructure.explainers.base import Explainer, ExplainerResult
from src.core.infrastructure.explainers.strategy import ExplainerStrategy, select_explainer_strategy
from src.core.infrastructure.explainers.strategies.shap_kernel_explainer import SHAPKernelExplainer
from src.core.infrastructure.explainers.strategies.shap_tree_explainer import SHAPTreeExplainer


class SHAPAnalyzerAdapter:
    """Adapter class to integrate SHAPAnalyzer with the Explainer interface."""
    _EXPLAINER_MAP = {
        ExplainerStrategy.TREE: SHAPTreeExplainer,
        ExplainerStrategy.KERNEL: SHAPKernelExplainer
    }
    _MODEL_ALIASES = {
        "LinearRegression": Algorithm.LINEAR_REGRESSION,
        "LogisticRegression": Algorithm.LOGISTIC_REGRESSION,
        "DecisionTreeClassifier": Algorithm.DECISION_TREE_CLASSIFIER,
        "DecisionTreeRegressor": Algorithm.DECISION_TREE_REGRESSOR,
        "RandomForestClassifier": Algorithm.RANDOM_FOREST_CLASSIFIER,
        "RandomForestRegressor": Algorithm.RANDOM_FOREST_REGRESSOR,
        "SVC": Algorithm.SVM,
        "SVR": Algorithm.SVM,
        "XGBClassifier": Algorithm.XGBOOST_CLASSIFIER,
        "XGBRegressor": Algorithm.XGBOOST_REGRESSOR,
        "XGBoostC": Algorithm.XGBOOST_CLASSIFIER,
        "XGBoostR": Algorithm.XGBOOST_REGRESSOR,
        "SymbolicRegressor": Algorithm.SYMBOLIC_REGRESSOR,
    }
    
    def __init__(self, model, x_train: pd.DataFrame, plot_dir: str, task_type: TaskType):
        self.model=model
        self.x_train = x_train
        self.plot_dir = plot_dir
        self.task_type= task_type
      
    def explain(self, x_sample: pd.DataFrame, dependence_variable: str) -> ExplainerResult:
        """Generate SHAP explanations and associated plots for a given sample."""
        logging.info(f"Starting explanation for sample with dependence variable '{dependence_variable}'")
        try: 
            model_type = self._extract_model_type()
            strategy = select_explainer_strategy(algorithm=model_type, task_type=self.task_type)
            explainer = self._create_explainer(strategy)
            # input validation: ensure x_sample is a DataFrame and not huge
            if not hasattr(x_sample, 'shape') or not hasattr(x_sample, 'columns'):
                raise TypeError("x_sample must be a pandas DataFrame")
            max_rows = 2000
            if len(x_sample) > max_rows:
                logging.warning(f"x_sample too large ({len(x_sample)} rows); truncating to {max_rows}")
                x_sample = x_sample.iloc[:max_rows]
                
            result = explainer.explain(x_sample, dependence_variable)
            logging.info(f"Explanation completed successfully with strategy '{strategy}'")
            return result
        except Exception as e:
            logging.exception(f"Error occurred while explaining sample: {e}")
            raise
        
    def _extract_model_type(self) -> Algorithm:
        """Extract the model type from the model's class name."""
        from sklearn.pipeline import Pipeline
        
        if isinstance(self.model, Pipeline):
            base_model=self.model.named_steps[list(self.model.named_steps.keys())[-1]]
        else:
            base_model=self.model
        candidate_names = self._candidate_model_class_names(base_model)

        for candidate_name in candidate_names:
            if candidate_name in self._MODEL_ALIASES:
                return self._MODEL_ALIASES[candidate_name]

        normalized_candidates = [candidate.lower() for candidate in candidate_names]
        for candidate_name in normalized_candidates:
            for alias_name, algorithm in self._MODEL_ALIASES.items():
                alias_lower = alias_name.lower()
                if alias_lower in candidate_name or candidate_name in alias_lower:
                    return algorithm

        raise ValueError(
            f"Impossible to dynamically map model '{type(base_model).__name__}' to a known algorithm. "
            f"Register an explicit alias in SHAPAnalyzerAdapter._MODEL_ALIASES."
        )

    def _candidate_model_class_names(self, model: object) -> Iterable[str]:
        """Return all class-name candidates that may identify the underlying estimator."""
        names = [type(model).__name__]

        if hasattr(model, "model") and model.model is not None:
            names.append(type(model.model).__name__)

        if hasattr(model, "estimator") and model.estimator is not None:
            names.append(type(model.estimator).__name__)

        return names
        
        
         
    def _create_explainer(self, strategy: ExplainerStrategy) -> Explainer:
        """Factory method to create the appropriate explainer based on the selected strategy."""
        if strategy not in self._EXPLAINER_MAP:
            raise ValueError(f"Unsupported explainer strategy: {strategy}")
        explainer_class = self._EXPLAINER_MAP[strategy]
        logging.info(f"Creating explainer of type '{explainer_class.__name__}' for strategy '{strategy}'")
        
        explainer= explainer_class(model=self.model, x_train=self.x_train)
        explainer.plot_dir=self.plot_dir
        return explainer