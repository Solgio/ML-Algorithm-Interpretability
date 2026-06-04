import os
import matplotlib.pyplot as plt
import pandas as pd
import shap
from src.core.infrastructure.explainers.base import Explainer
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
    
    def _extract_base_model(self):
        """Extract the underlying model if it's wrapped in a pipeline or ensemble."""
        from sklearn.pipeline import Pipeline
        if isinstance(self.model, Pipeline):
            return self.model.named_steps[list(self.model.named_steps.keys())[-1]]
        else:
            return self.model
        
    def _generate_plots(self, shap_values, x_sample: pd.DataFrame, dependence_variable: str) -> Dict[str, str]:
        """Generate SHAP plots and save them to disk, returning their paths."""
        plot_paths = {}
        plot_dir = self._ensure_plot_dir()
        
        try: # Plot 1: Summary Bar
            logging.info("Generando SHAP summary plot...")
            plt.figure(figsize=(10, 6))
            shap.summary_plot(shap_values, x_sample, plot_type="bar", show=False)
            summary_path = os.path.join(plot_dir, "shap_summary_bar.png")
            plt.savefig(summary_path, bbox_inches='tight', dpi=300)
            plt.close()
            plot_paths["shap_summary"] = summary_path
            logging.info(f"✓ Summary: {summary_path}")
        except Exception as e:
            logging.warning(f"Failed to generate SHAP summary plot: {e}")
            
        try: # Plot 2: Dependence
            logging.info(f"Generando dependence plot per {dependence_variable}...")
            plt.figure(figsize=(10, 6))
            shap.dependence_plot(dependence_variable, shap_values.values, x_sample, 
                               show=False)
            dep_path = os.path.join(plot_dir, f"shap_dependence_{dependence_variable}.png")
            plt.savefig(dep_path, bbox_inches='tight', dpi=300)
            plt.close()
            plot_paths["dependence_plot"] = dep_path
            logging.info(f"✓ Dependence: {dep_path}")
        except Exception as e:
            logging.warning(f"Failed to generate SHAP dependence plot: {e}")
            
        try: # Plot 3: Waterfall (primo campione)
            logging.info("Generando force plot...")
            plt.figure(figsize=(12, 6))
            shap.plots.waterfall(shap_values[0], show=False)
            force_path = os.path.join(plot_dir, "shap_force_plot_sample_0.png")
            plt.savefig(force_path, bbox_inches='tight', dpi=300)
            plt.close()
            plot_paths["force_plot"] = force_path
            logging.info(f"✓ Force: {force_path}")
        except Exception as e:
            logging.warning(f"Failed to generate SHAP force plot: {e}")

        return plot_paths