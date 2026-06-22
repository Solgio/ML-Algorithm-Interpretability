import logging
import pandas as pd
import numpy as np
import shap
from src.core.infrastructure.explainers.base import Explainer
from src.core.infrastructure.explainers.plot_renderer import SHAPPlotRenderer
from typing import Any, Dict



class SHAPKernelExplainer(Explainer):
    """SHAP explainer for models without native SHAP support. Less efficient but more general."""
    
    def _compute_shap_values(self, x_sample: pd.DataFrame):
        """Compute SHAP values using the KernelExplainer."""
        """Compute SHAP values using the KernelExplainer."""
        logging.info("Computing SHAP values using KernelExplainer...")

        def clean_data(df):
            if isinstance(df, pd.DataFrame):
                return df.astype(np.float64)
            return np.asarray(df, dtype=np.float64)
        
        x_sample_clean = clean_data(x_sample)
        x_train_clean = clean_data(self.x_train)

        pred_fn = self._create_prediction_function(self.model)

        background_sample = shap.sample(x_train_clean, min(30, len(x_train_clean)))
        explainer = shap.Explainer(pred_fn, background_sample)

        logging.info(f"SHAP explanation starting with {x_sample_clean.shape[1]} features")
        shap_values = explainer(x_sample_clean)

        return shap_values
        
    def _create_prediction_function(self, model: Any):
        """Create a prediction function based on the model's capabilities."""
        if hasattr(model, "predict_proba"):
            logging.info("Using 'predict_proba' for SHAP KernelExplainer")
            return lambda x: model.predict_proba(x)
        elif hasattr(model, "decision_function"):
            logging.info("Using 'decision_function' for SHAP KernelExplainer")
            return lambda x: model.decision_function(x)
        else:
            logging.debug("Using 'predict' for SHAP KernelExplainer")
            return lambda x: model.predict(x)
    
    def _generate_plots(self, shap_values, x_sample: pd.DataFrame, dependence_variable: str) -> Dict[str, str]:
        """Generate SHAP plots and save them to disk, returning their paths."""
        logging.info("Generating standard SHAP plots via shared renderer...")
        renderer = SHAPPlotRenderer(self.plot_dir)
        return renderer.render(shap_values, x_sample, dependence_variable)