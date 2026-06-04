import os
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shap
from src.core.infrastructure.explainers.base import Explainer
from typing import Any, Dict



class SHAPKernelExplainer(Explainer):
    """SHAP explainer for models without native SHAP support. Less efficient but more general."""
    
    def _compute_shap_values(self, x_sample: pd.DataFrame):
        """Compute SHAP values using the KernelExplainer."""
        logging.info("Computing SHAP values using KernelExplainer...")
        model_to_explain = self._extract_base_model()
        pred_fn = self._create_prediction_function(model_to_explain)
        background_sample = shap.sample(self.x_train, min(30, len(self.x_train)))
        explainer = shap.Explainer(pred_fn, background_sample)
        shap_values = explainer(x_sample)
        return shap_values
    
    def _extract_base_model(self):
        """Extract the underlying model if it's wrapped in a pipeline or ensemble."""
        from sklearn.pipeline import Pipeline
        if isinstance(self.model, Pipeline):
            return self.model.named_steps[list(self.model.named_steps.keys())[-1]]
        else:
            return self.model
        
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
        plot_paths = {}
        plot_dir = self._ensure_plot_dir()
        
        try: # Plot 1: Summary Bar
            logging.info("Generando SHAP summary plot...")
            plt.figure(figsize=(10, 6))
            
            shap_vals = shap_values.values if hasattr(shap_values, 'values') else shap_values
            if len(shap_vals.shape) == 3:
                shap.summary_plot(shap_vals[:, :, 1], x_sample, plot_type="bar", 
                                show=False)
            else:
                shap.summary_plot(shap_vals, x_sample, plot_type="bar", show=False)
            
            summary_path = os.path.join(plot_dir, "shap_summary_bar.png")
            plt.savefig(summary_path, bbox_inches='tight', dpi=300)
            plt.close()
            plot_paths["shap_summary"] = summary_path
            logging.info(f"✓ Summary: {summary_path}")
        except Exception as e:
            logging.warning(f"Failed to generate SHAP summary plot: {e}")
            
        try: # Plot 2: Dependence
            logging.info(f"Generando dependence plot...")
            plt.figure(figsize=(10, 6))
            
            if len(shap_vals.shape) == 3:
                shap_vals_2d = shap_vals[:, :, 1]
            else:
                shap_vals_2d = shap_vals
            
            shap.dependence_plot(dependence_variable, shap_vals_2d, x_sample, 
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
            
            if len(shap_values.shape) == 3:
                shap.plots.waterfall(shap_values[0, :, 1], show=False)
            else:
                shap.plots.waterfall(shap_values[0], show=False)
            
            force_path = os.path.join(plot_dir, "shap_force_plot_sample_0.png")
            plt.savefig(force_path, bbox_inches='tight', dpi=300)
            plt.close()
            plot_paths["force_plot"] = force_path
            logging.info(f"✓ Force: {force_path}")
        except Exception as e:
            logging.warning(f"Failed to generate SHAP force plot: {e}")
        
        return plot_paths