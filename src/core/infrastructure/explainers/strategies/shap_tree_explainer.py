import matplotlib.pyplot as plt
import pandas as pd
import shap
from src.core.infrastructure.explainers.base import Explainer
from src.core.infrastructure.explainers.plot_renderer import SHAPPlotRenderer
from typing import Dict
import logging

class SHAPTreeExplainer(Explainer):
    """SHAP explainer optimized for tree-based models."""
    
    def _compute_shap_values(self, x_sample: pd.DataFrame):
        """Compute SHAP values using the TreeExplainer."""
        logging.info("Computing SHAP values using TreeExplainer...")
        model_to_explain = self._extract_base_model()
        explainer = shap.TreeExplainer(model_to_explain)
        logging.info("Calculating SHAP values...")
        shap_values = explainer(x_sample)
        return shap_values
        
    def _generate_plots(self, shap_values, x_sample: pd.DataFrame, dependence_variable: str) -> Dict[str, str]:
        """Generate SHAP plots and save them to disk, returning their paths."""
        logging.info("Generating standard SHAP plots via shared renderer...")
        renderer = SHAPPlotRenderer(self.plot_dir)
        return renderer.render(shap_values, x_sample, dependence_variable)