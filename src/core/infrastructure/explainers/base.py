
from abc import ABC, abstractmethod
import os
import logging
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

import pandas as pd


@dataclass
class ExplainerResult:
    """Value object for SHAP explanations and generated artifacts.

    Use this as the canonical return type from explainers. It groups the
    raw SHAP values, optional base/expected values, feature names and any
    persisted plot paths produced by the renderer.
    """

    shap_values: Any
    feature_names: List[str]
    base_value: Optional[float] = None
    plot_paths: Dict[str, str] = field(default_factory=dict)


class Explainer(ABC):
    """Abstract base class for model explainers."""
    def __init__(self, model, x_train: pd.DataFrame):
        self.model = model
        self.x_train = x_train
        self.plot_dir = None
    
    def explain(self, x_sample: pd.DataFrame, dependence_variable: str) -> ExplainerResult:
        """Generate SHAP explanations and associated plots for a given sample.

        Returns an `ExplainerResult` containing the raw SHAP output and any
        saved plot paths.
        """
        logging.info(f"Starting explanation for sample with dependence variable '{self.__class__.__name__}'")
        try:
            shap_values = self._compute_shap_values(x_sample)
            plot_paths = self._generate_plots(shap_values, x_sample, dependence_variable)
            feature_names = list(x_sample.columns) if hasattr(x_sample, 'columns') else []
            base_value = None
            # try to read expected/base value from shap object when available
            try:
                base_value = getattr(shap_values, 'base_values', None) or getattr(shap_values, 'base_value', None)
            except Exception:
                base_value = None

            return ExplainerResult(
                shap_values=shap_values,
                feature_names=feature_names,
                base_value=base_value,
                plot_paths=plot_paths or {},
            )
        except Exception as e:
            logging.exception(f"Error occurred while explaining sample: {e}")
            raise
    def _ensure_plot_dir(self) -> str:
        """Ensure the plot directory exists and return its path."""
        if self.plot_dir is None:
            raise ValueError("Plot directory not set for explainer.")
        os.makedirs(self.plot_dir, exist_ok=True)
        return self.plot_dir

    def _extract_base_model(self):
        """Extract the underlying estimator from a pipeline when needed."""
        from sklearn.pipeline import Pipeline

        if isinstance(self.model, Pipeline):
            return self.model.named_steps[list(self.model.named_steps.keys())[-1]]
        return self.model
    
    @abstractmethod
    def _compute_shap_values(self, x_sample: pd.DataFrame):
        """Compute SHAP values for the given sample. This method must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def _generate_plots(self, shap_values, x_sample: pd.DataFrame, dependence_variable: str) -> Dict[str, str]:
        """Generate plots for the given SHAP values. This method must be implemented by subclasses."""
        pass