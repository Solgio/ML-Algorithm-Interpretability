
from abc import ABC, abstractmethod
import os
import pandas as pd
import numpy as np
import logging
from typing import Any, Dict, List, Optional
from dataclasses import dataclass


#@dataclass
#class ExplainerResult:
#    """Value object for SHAP results."""
#    shap_values: np.ndarray
#    base_value: float
#    feature_names: list
#    model_expected_value: Optional[float] = None
#    plot_paths:Dict[str, str] = None
#    
#    def __post_init__(self):
#        if self.plot_paths is None:
#            self.plot_paths = {}
#            
#    def __repr__(self):
#        return (f"ExplainerResult("
#                f"shap_values shape={self.shap_values.shape}, "
#                f"base_value={self.base_value}, "
#                f"features={self.feature_names}, "
#                f"plots={self.plot_paths})")
        
class Explainer(ABC):
    """Abstract base class for model explainers."""
    def __init__(self, model, x_train: pd.DataFrame):
        self.model = model
        self.x_train = x_train
        self.plot_dir = None
    
    def explain(self, x_sample: pd.DataFrame, dependence_variable: str) -> Dict[str, str]:
        """Generate SHAP explanations and associated plots for a given sample."""
        logging.info(f"Starting explanation for sample with dependence variable '{self.__class__.__name__}'")
        try: 
            shap_values = self._compute_shap_values(x_sample)
            plot_paths = self._generate_plots(shap_values, x_sample, dependence_variable)
            return plot_paths
        except Exception as e:
            logging.exception(f"Error occurred while explaining sample: {e}")
            raise
    def _ensure_plot_dir(self) -> str:
        """Ensure the plot directory exists and return its path."""
        if self.plot_dir is None:
            raise ValueError("Plot directory not set for explainer.")
        os.makedirs(self.plot_dir, exist_ok=True)
        return self.plot_dir
    
    @abstractmethod
    def _compute_shap_values(self, x_sample: pd.DataFrame):
        """Compute SHAP values for the given sample. This method must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def _generate_plots(self, shap_values, x_sample: pd.DataFrame, dependence_variable: str) -> Dict[str, str]:
        """Generate plots for the given SHAP values. This method must be implemented by subclasses."""
        pass