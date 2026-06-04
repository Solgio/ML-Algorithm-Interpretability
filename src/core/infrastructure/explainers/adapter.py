from typing import Dict
import logging
import pandas as pd
from src.core.infrastructure.models.model_factory import ModelFactory
from src.core.domain.enums import Algorithm, TaskType
from src.core.infrastructure.explainers.base import Explainer
from src.core.infrastructure.explainers.strategy import ExplainerStrategy, select_explainer_strategy
from src.core.infrastructure.explainers.strategies.shap_kernel_explainer import SHAPKernelExplainer
from src.core.infrastructure.explainers.strategies.shap_tree_explainer import SHAPTreeExplainer


class SHAPAnalyzerAdapter:
    """Adapter class to integrate SHAPAnalyzer with the Explainer interface."""
    _EXPLAINER_MAP = {
        ExplainerStrategy.TREE: SHAPTreeExplainer,
        ExplainerStrategy.KERNEL: SHAPKernelExplainer
    }
    
    def __init__(self, model, x_train: pd.DataFrame, plot_dir: str, task_type: TaskType):
        self.model=model
        self.x_train = x_train
        self.plot_dir = plot_dir
        self.task_type= task_type
      
    def explain(self, x_sample: pd.DataFrame, dependence_variable: str) -> Dict[str, str]:
        """Generate SHAP explanations and associated plots for a given sample."""
        logging.info(f"Starting explanation for sample with dependence variable '{dependence_variable}'")
        try: 
            model_type = self._extract_model_type()
            strategy = select_explainer_strategy(algorithm=model_type, task_type=self.task_type)
            explainer = self._create_explainer(strategy)
            plot_paths = explainer.explain(x_sample, dependence_variable)
            logging.info(f"Explanation completed successfully with strategy '{strategy}'")
            return plot_paths        
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
        current_class_name = type(base_model).__name__
        underlying_class_name = None
        if hasattr(base_model, 'model'):
            underlying_class_name = type(base_model.model).__name__
        
        for registry in ModelFactory._registry.values():
            if registry.class_name == current_class_name or (underlying_class_name and registry.class_name in underlying_class_name):
                return registry.algorithm
                
        for registry in ModelFactory._registry.values():
            reg_lower = registry.class_name.lower()
            curr_lower = current_class_name.lower()
            if reg_lower in curr_lower or curr_lower in reg_lower:
                return registry.algorithm

        raise ValueError(
            f"Impossibile mappare dinamicamente il modello '{current_class_name}' a un algoritmo noto. "
            f"Verifica la corrispondenza del 'class_name' nel registry_initializer."
        )
        
        
         
    def _create_explainer(self, strategy: ExplainerStrategy) -> Explainer:
        """Factory method to create the appropriate explainer based on the selected strategy."""
        if strategy not in self._EXPLAINER_MAP:
            raise ValueError(f"Unsupported explainer strategy: {strategy}")
        explainer_class = self._EXPLAINER_MAP[strategy]
        logging.info(f"Creating explainer of type '{explainer_class.__name__}' for strategy '{strategy}'")
        
        explainer= explainer_class(model=self.model, x_train=self.x_train)
        explainer.plot_dir=self.plot_dir
        return explainer