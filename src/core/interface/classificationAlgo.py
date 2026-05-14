import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import shap
import sklearn
from abc import ABC, abstractmethod
from .baseMLAlgo import BaseMLAlgo

class ClassificationAlgo(BaseMLAlgo):
    @abstractmethod
    def __init__(self, model_name: str, dataset: str):
        self.model_name = model_name
        super().__init__(model_name=model_name, task_type="classification", dataset=dataset)
    
    @abstractmethod
    def fit(self, X_train, y_train, X_test, y_test):
        pass

    def calculate_metrics(self) -> dict:
        accuracy = self.model.score(self.X, self.y)
        f1_score = sklearn.metrics.f1_score(self.y, self.model.predict(self.X), average='weighted')
        auc = sklearn.metrics.roc_auc_score(self.y, self.model.predict_proba(self.X), multi_class='ovr')
        print(f"Accuracy: {accuracy:.4f}\n")
        print(f"F1 Score: {f1_score:.4f}\n")
        print(f"AUC: {auc:.4f}\n")
        return {
            "Accuracy": accuracy,
            "F1_Score": f1_score,
            "AUC": auc
        }
    
    def generate_plots(self) -> dict:
        roc_curve = sklearn.metrics.roc_curve(self.y, self.model.predict_proba(self.X)[:, 1])
        residual_plot = sns.residplot(x=self.model.predict(self.X), y=self.y - self.model.predict(self.X), lowess=True)
        return {
            "roc_curve": roc_curve,
            "residual_plot": residual_plot
        }
    
    def SHAP_analysis(self, X_sample):
        explainer = shap.Explainer(self.model, X_sample)
        shap_values = explainer(X_sample)
        print("\nSHAP values calculated successfully!")
        
        shap.summary_plot(shap_values, X_sample, plot_type="bar", show=False)
        summary_path = os.path.join(self.PLOT_DIR, "shap_summary.png")
        plt.savefig(summary_path)
        
        return {
            "shap_summary": summary_path,
        }
    
    def export_results(self) -> dict:
        metrics=self.calculate_metrics()
        coef_df = pd.DataFrame({'Feature': self.X.columns, 'Coefficiente': self.model.coef_})
        coef_csv_path = os.path.join(self.PLOT_DIR, 'coefficienti.csv')
        coef_df.to_csv(coef_csv_path, index=False)
        
        metriche = {
            "Accuracy": metrics["Accuracy"],
            "F1_Score": metrics["F1_Score"],
            "AUC": metrics["AUC"]
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