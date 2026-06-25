
from abc import abstractmethod
import json
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import shap
import sklearn

from src.core.interface.baseMLAlgo import BaseMLAlgo

class BaseRegressionAlgo(BaseMLAlgo):
    @abstractmethod
    def __init__(self, model_name: str, dataset: str, dataset_path: str, param_grid: dict=None):
        self.model_name = model_name
        super().__init__(model_name=model_name, task_type="regression", dataset=dataset, dataset_path=dataset_path, param_grid=param_grid)
        
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
        dc_numeric = dc.select_dtypes(include=[np.number])
        correlation_matrix = dc_numeric.corr(method='pearson')
        g = sns.clustermap(dc_numeric.corr(), 
                   cmap='coolwarm', 
                   annot=False, 
                   figsize=(20, 20), 
                   dendrogram_ratio=0.1)
        g.figure.suptitle('Clustered Correlation Matrix')
        corr_path = os.path.join(self.PLOT_DIR, "clustered_correlation_matrix.png")
        g.savefig(corr_path)
        plt.close()
        
        return {"correlation_matrix": corr_path}
        
    @abstractmethod
    def generate_algorithm_specific_plots(self) -> dict:
        pass
    
    
    def export_results(self) -> dict:
        metrics=self.calculate_metrics()
        
        if hasattr(self.model, "coef_"):
            weights = self.model.coef_
        elif hasattr(self.model, "feature_importances_"):
            weights = self.model.feature_importances_
        else:
            weights = [0] * len(self.X.columns)
            
        coef_df = pd.DataFrame({'Feature': self.X.columns, 'Weight/Coefficient': weights})
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
        
        print(f"Data successfully exported to: {self.PLOT_DIR}")
        
        return {
            "metrics": metriche,
            "plot_dir": self.PLOT_DIR,
            "metrics_path": metriche_json_path,
            "coefficients_path": coef_csv_path
        }