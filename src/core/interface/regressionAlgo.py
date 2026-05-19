
from abc import abstractmethod
import json
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import shap
import sklearn

from .baseMLAlgo import BaseMLAlgo

class BaseRegressionAlgo(BaseMLAlgo):
    @abstractmethod
    def __init__(self, model_name: str, dataset: str):
        self.model_name = model_name
        super().__init__(model_name=model_name, task_type="regression", dataset=dataset)
        
    @abstractmethod
    def fit(self, X_train, y_train, X_test, y_test):
        pass

    def calculate_metrics(self) -> dict:
        y_pred = self.model.predict(self.X)
        r_squared = self.model.score(self.X, self.y)
        mae = sklearn.metrics.mean_absolute_error(self.y, y_pred)
        mean_squared_error = sklearn.metrics.mean_squared_error(self.y, y_pred)
        rmse = np.sqrt(mean_squared_error)
        
        n = self.X.shape[0]  # numero di istanze (n)
        p = self.X.shape[1]  # numero di feature (p)
        
        if n > p + 1:
            adjusted_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)
        else:
            adjusted_r_squared = float('nan')
            
        print(f"R-squared: {r_squared:.4f}\n")
        print(f"Mean Absolute Error: {mae:.4f}\n")
        print(f"Mean Squared Error: {mean_squared_error:.4f}\n")
        print(f"Root Mean Squared Error: {rmse:.4f}\n")
        return {
            "R_squared": r_squared,
            "Adjusted_R_squared": adjusted_r_squared,
            "MAE": mae,
            "MSE": mean_squared_error,
            "RMSE": rmse
        }
    
    def generate_plots(self, binary_features: list=[]) -> dict:
        dc=self.df.drop(columns=binary_features, errors='ignore')
        correlation_matrix = dc.corr(method='pearson')
        plt.figure(figsize=(16, 16))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Matrix')
        corr_path = os.path.join(self.PLOT_DIR, "correlation_matrix.png")
        plt.savefig(corr_path)
        plt.close()
        
        return {"correlation_matrix": corr_path}
        
    @abstractmethod
    def generate_algorithm_specific_plots(self) -> dict:
        pass
    
    def SHAP_analysis(self, x_sample, dependence_variable):
        try:
            explainer = shap.Explainer(self.model, x_sample)
            shap_values = explainer(x_sample)
            print("\nSHAP values calculated successfully!")
        except Exception as e:
            pred_fn = self.model.predict
            explainer = shap.Explainer(pred_fn, x_sample)
            shap_values = explainer(x_sample)
        shap.summary_plot(shap_values, x_sample, plot_type="bar", show=False)
        summary_path = os.path.join(self.PLOT_DIR, "shap_summary.png")
        plt.savefig(summary_path)
        plt.close()
        
        sample_ind = 20
        shap.partial_dependence_plot(
            dependence_variable,
            self.model.predict,
            x_sample,
            model_expected_value=True,
            feature_expected_value=True,
            ice=True,
            shap_values=shap_values[sample_ind : sample_ind + 1, :],
            show=False
        )
        pdp_path = os.path.join(self.PLOT_DIR, f"partial_dependence_{dependence_variable}_sample_{sample_ind}.png")
        plt.savefig(pdp_path)
        plt.close()
        #shap.plots.beeswarm(shap_values)
        
        shap.plots.heatmap(shap_values, show=False)
        heatmap_path = os.path.join(self.PLOT_DIR, "shap_heatmap.png")
        plt.savefig(heatmap_path)
        plt.close()
        
        return {
            "shap_summary": summary_path,
            "partial_dependence": pdp_path,
            "shap_heatmap": heatmap_path
        }
    
    def export_results(self) -> dict:
        metrics=self.calculate_metrics()
        
        if hasattr(self.model, "coef_"):
            weights = self.model.coef_
        elif hasattr(self.model, "feature_importances_"):
            weights = self.model.feature_importances_
        else:
            weights = [0] * len(self.X.columns)
            
        coef_df = pd.DataFrame({'Feature': self.X.columns, 'Peso/Coefficiente': weights})
        coef_csv_path = os.path.join(self.PLOT_DIR, 'coefficienti_pesi.csv')
        coef_df.to_csv(coef_csv_path, index=False)
        
        metriche = {
            "R_squared": metrics["R_squared"],
            "Adjusted_R_squared": metrics["Adjusted_R_squared"],
            "MAE": metrics["MAE"],
            "MSE": metrics["MSE"],
            "RMSE": metrics["RMSE"]
        }
        metriche_json_path = os.path.join(self.PLOT_DIR, 'metriche.json')
        with open(metriche_json_path, 'w') as f:
            json.dump(metriche, f)
        
        print(f"Dati esportati con successo in: {self.PLOT_DIR}")
        
        return {
            "metrics": metriche,
            "plot_dir": self.PLOT_DIR,
            "metrics_path": metriche_json_path,
            "coefficients_path": coef_csv_path
        }