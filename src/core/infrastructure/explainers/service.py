import os
import shap
import matplotlib.pyplot as plt
import numpy as np
import logging
from typing import List, Dict
from src.core.infrastructure.explainers.factory import ExplainerFactory
from src.core.domain.enums import Algorithm, TaskType
from src.core.infrastructure.explainers.base import Explainer


class ExplainerService:
    """Service class responsible for managing explainers."""
    
    def __init__(self, output_dir:str="../output/explanations"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        ExplainerFactory.initialize()
    
    def explain_model(self, model: any, X: np.ndarray, feature_names: List[str], algorithm: Algorithm, task_type: TaskType, **kwargs) -> Explainer:
        """Generate explanations for a given model and dataset."""
        try:
            explainer = ExplainerFactory.create(algorithm, task_type)
            result = explainer.explain(model, X, feature_names, **kwargs)
            plot_paths = self._generate_plots(result)
            result.plot_paths.update(plot_paths)
            return result
        except Exception as e:
            logging.exception(f"Error occurred while explaining model: {e}")
            raise
        
    def _generate_plots(self, result:dict) -> Dict[str, str]:
        """Generate SHAP plots and save them to disk, returning their paths."""
        plot_paths = {}
        try:
            # Plot 1: Summary plot (bar)
            logging.debug("Generating summary plot...")
            plt.figure(figsize=(10, 6))
            shap.summary_plot(result.shap_values, result.feature_names, plot_type="bar", show=False)
            summary_path = os.path.join(self.output_dir, "shap_summary_bar.png")
            plt.savefig(summary_path, bbox_inches='tight', dpi=100)
            plt.close()
            plot_paths["summary_bar"] = summary_path
            logging.debug(f"✓ Summary bar plot saved: {summary_path}")
        
        except Exception as e:
            logging.warning(f"Summary bar plot failed: {e}")
        
        try:
            # Plot 2: Summary plot (beeswarm)
            logging.debug("Generating beeswarm plot...")
            plt.figure(figsize=(10, 6))
            shap.summary_plot(result.shap_values, result.feature_names, plot_type="beeswarm", show=False)
            beeswarm_path = os.path.join(self.output_dir, "shap_summary_beeswarm.png")
            plt.savefig(beeswarm_path, bbox_inches='tight', dpi=100)
            plt.close()
            plot_paths["summary_beeswarm"] = beeswarm_path
            logging.debug(f"✓ Beeswarm plot saved: {beeswarm_path}")
        
        except Exception as e:
            logging.warning(f"Beeswarm plot failed: {e}")
        
        return plot_paths