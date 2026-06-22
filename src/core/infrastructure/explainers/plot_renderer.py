import os
import re
from typing import Dict

import matplotlib.pyplot as plt
import pandas as pd
import shap


class SHAPPlotRenderer:
    """Render and persist the standard SHAP plots for a computed explanation."""

    def __init__(self, plot_dir: str):
        self.plot_dir = plot_dir

    def render(self, shap_values, x_sample: pd.DataFrame, dependence_variable: str) -> Dict[str, str]:
        """Generate the standard SHAP plot set and return their file paths."""
        plot_paths: Dict[str, str] = {}
        shap_values_array = self._to_array(shap_values)

        plot_paths.update(self._render_summary_bar(shap_values_array, x_sample))
        plot_paths.update(self._render_dependence(shap_values_array, x_sample, dependence_variable))
        plot_paths.update(self._render_waterfall(shap_values))
        return plot_paths

    def _render_summary_bar(self, shap_values_array, x_sample: pd.DataFrame) -> Dict[str, str]:
        try:
            plt.figure(figsize=(10, 6))
            shap.summary_plot(shap_values_array, x_sample, plot_type="bar", show=False)
            return {"shap_summary": self._save_plot("shap_summary_bar.png")}
        except Exception:
            return {}

    def _render_dependence(self, shap_values_array, x_sample: pd.DataFrame, dependence_variable: str) -> Dict[str, str]:
        try:
            plt.figure(figsize=(10, 6))
            shap.dependence_plot(dependence_variable, shap_values_array, x_sample, show=False)
            safe_name = self._safe_filename(f"shap_dependence_{dependence_variable}.png")
            return {"dependence_plot": self._save_plot(safe_name)}
        except Exception:
            return {}

    def _render_waterfall(self, shap_values) -> Dict[str, str]:
        try:
            plt.figure(figsize=(12, 6))
            shap.plots.waterfall(self._waterfall_item(shap_values), show=False)
            return {"force_plot": self._save_plot("shap_force_plot_sample_0.png")}
        except Exception:
            return {}

    def _waterfall_item(self, shap_values):
        if hasattr(shap_values, "shape") and len(shap_values.shape) == 3:
            return shap_values[0, :, 1]
        return shap_values[0]

    def _to_array(self, shap_values):
        values = shap_values.values if hasattr(shap_values, "values") else shap_values
        if hasattr(values, "shape") and len(values.shape) == 3:
            return values[:, :, 1]
        return values

    def _save_plot(self, filename: str, dpi: int = 300) -> str:
        # sanitize filename and ensure path stays within plot_dir
        safe_filename = self._safe_filename(filename)
        os.makedirs(self.plot_dir, mode=0o750, exist_ok=True)
        path = os.path.join(self.plot_dir, safe_filename)
        # ensure no path traversal
        plot_dir_abs = os.path.abspath(self.plot_dir)
        path_abs = os.path.abspath(path)
        if not (path_abs == plot_dir_abs or path_abs.startswith(plot_dir_abs + os.sep)):
            raise ValueError("Attempted to write outside the plot directory")
        try:
            plt.savefig(path, bbox_inches='tight', dpi=dpi)
        finally:
            try:
                plt.close()
            except Exception:
                pass
        try:
            os.chmod(path, 0o640)
        except Exception:
            # best-effort; on some filesystems/chroots chmod may fail
            pass
        return path

    def _safe_filename(self, filename: str) -> str:
        # only allow a limited charset in filenames; replace others with '_'
        name = os.path.basename(filename)
        safe = re.sub(r'[^A-Za-z0-9_.-]', '_', name)
        # avoid empty names
        return safe or "plot.png"