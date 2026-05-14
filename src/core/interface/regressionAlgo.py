
from abc import abstractmethod
import json
import os
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
        r_squared = self.model.score(self.X, self.y)
        mae = sklearn.metrics.mean_absolute_error(self.y, self.model.predict(self.X))
        root_mean_squared_error = sklearn.metrics.mean_squared_error(self.y, self.model.predict(self.X))
        print(f"R-squared: {r_squared:.4f}\n")
        print(f"Mean Absolute Error: {mae:.4f}\n")
        print(f"Root Mean Squared Error: {root_mean_squared_error:.4f}\n")
        return {
            "R_squared": r_squared,
            "MAE": mae,
            "RMSE": root_mean_squared_error
        }
    
    def generate_plots(self, binary_features: list=[]) -> dict:
        dc=self.df.drop(columns=binary_features, errors='ignore')
        correlation_matrix = dc.corr(method='pearson')
        plt.figure(figsize=(16, 16))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Matrix')
        corr_path = os.path.join(self.PLOT_DIR, "correlation_matrix.png")
        plt.savefig(corr_path)
        return {"correlation_matrix": corr_path}
        
    
    def SHAP_analysis(self, X_sample, dependence_variable):
        
        explainer = shap.Explainer(self.model, X_sample)
        shap_values = explainer(X_sample)
        print("\nSHAP values calculated successfully!")
        
        shap.summary_plot(shap_values, X_sample, plot_type="bar", show=False)
        summary_path = os.path.join(self.PLOT_DIR, "shap_summary.png")
        plt.savefig(summary_path)
        
        sample_ind = 20
        shap.partial_dependence_plot(
            dependence_variable,
            self.model.predict,
            X_sample,
            model_expected_value=True,
            feature_expected_value=True,
            ice=False,
            shap_values=shap_values[sample_ind : sample_ind + 1, :],
            show=False
        )
        pdp_path = os.path.join(self.PLOT_DIR, f"partial_dependence_{dependence_variable}_sample_{sample_ind}.png")
        plt.savefig(pdp_path)

        #shap.plots.beeswarm(shap_values)
        
        shap.plots.heatmap(shap_values, show=False)
        heatmap_path = os.path.join(self.PLOT_DIR, "shap_heatmap.png")
        plt.savefig(heatmap_path)
        
        return {
            "shap_summary": summary_path,
            "partial_dependence": pdp_path,
            "shap_heatmap": heatmap_path
        }
    
    def export_results(self) -> dict:
        metrics=self.calculate_metrics()
        coef_df = pd.DataFrame({'Feature': self.X.columns, 'Coefficiente': self.model.coef_})
        coef_csv_path = os.path.join(self.PLOT_DIR, 'coefficienti.csv')
        coef_df.to_csv(coef_csv_path, index=False)
        
        metriche = {
            "R_squared": metrics["R_squared"],
            "MAE": metrics["MAE"],
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