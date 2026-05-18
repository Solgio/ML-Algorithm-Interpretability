import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import shap
import sklearn
from abc import ABC, abstractmethod
from sklearn.metrics import ConfusionMatrixDisplay
from .baseMLAlgo import BaseMLAlgo

class BaseClassificationAlgo(BaseMLAlgo):
    @abstractmethod
    def __init__(self, model_name: str, dataset: str):
        self.model_name = model_name
        super().__init__(model_name=model_name, task_type="classification", dataset=dataset)
    
    @abstractmethod
    def fit(self, X_train, y_train, X_test, y_test):
        pass

    def calculate_metrics(self) -> dict:
        y_pred = self.model.predict(self.X)
        accuracy = self.model.score(self.X, self.y)
        f1_score = sklearn.metrics.f1_score(self.y, y_pred, average='weighted')
        precision = sklearn.metrics.precision_score(self.y, y_pred, average='weighted')
        recall = sklearn.metrics.recall_score(self.y, y_pred, average='weighted')
        cm = sklearn.metrics.confusion_matrix(self.y, y_pred)
        
        auc = None
        if hasattr(self.model, "predict_proba"):
            y_proba = self.model.predict_proba(self.X)
            if len(self.model.classes_) == 2:
                auc = sklearn.metrics.roc_auc_score(self.y, y_proba[:, 1])
            else:
                auc = sklearn.metrics.roc_auc_score(self.y, y_proba, multi_class='ovr')
            print(f"AUC: {auc:.4f}")
        else:
            print("AUC: Non calcolabile (il modello non supporta predict_proba)")
            
        specificity = None
        if len(self.model.classes_) == 2:
            tn, fp, fn, tp = cm.ravel()
            specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
            print(f"Specificity: {specificity:.4f}")
            
        print(f"Accuracy: {accuracy:.4f}\n")
        print(f"F1 Score: {f1_score:.4f}\n")
        print(f"AUC: {auc:.4f}\n")
        print(f"Precision: {precision:.4f}\n")
        print(f"Recall: {recall:.4f}\n")
        print(f"Confusion Matrix:\n{cm}\n")
        
        metrics_dict = {
            "Accuracy": accuracy,
            "F1_Score": f1_score,
            "AUC": auc,
            "Precision": precision,
            "Recall": recall,
            "Confusion_Matrix": cm.tolist()
        }
        
        if specificity is not None:
            metrics_dict["Specificity"] = specificity
            
        return metrics_dict
    
    def generate_plots(self, binary_features: list=[]) -> dict:
        import numpy as np
        plot_paths = {}
        
        if hasattr(self.model, "predict_proba"):
            y_prob = self.model.predict_proba(self.X)
            if len(self.model.classes_) == 2:
                prob_x_axis = y_prob[:, 1]
                
                fpr, tpr, _ = sklearn.metrics.roc_curve(self.y, prob_x_axis)
                plt.figure()
                plt.plot(fpr, tpr, color='darkorange', lw=2)
                plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
                plt.title('ROC Curve')
                roc_path = os.path.join(self.PLOT_DIR, "roc_curve.png")
                plt.savefig(roc_path)
                plt.close()
                plot_paths["roc_curve"] = roc_path        
        else:
            print(f"Avviso: {self.model_name} non supporta predict_proba. ROC Curve saltata.")
    
        dc = self.df.drop(columns=binary_features, errors='ignore')
        
        dc_numeric = dc.select_dtypes(include=[np.number])
        
        plt.figure(figsize=(16, 16))
        correlation_matrix = dc_numeric.corr(method='pearson')
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Matrix')
        corr_path = os.path.join(self.PLOT_DIR, "correlation_matrix.png")
        plt.savefig(corr_path)
        plt.close()
        plot_paths["correlation_matrix"] = corr_path
        
        cm = sklearn.metrics.confusion_matrix(self.y, self.model.predict(self.X))
        plt.figure(figsize=(10, 6))
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=self.model.classes_)
        disp.plot(cmap=plt.cm.Blues, values_format='d', ax=plt.gca())
        plt.title("Confusion Matrix")
        cm_path = os.path.join(self.PLOT_DIR, "confusion_matrix.png")
        plt.savefig(cm_path)
        plt.close()
        plot_paths["confusion_matrix"] = cm_path

        return plot_paths
        
    @abstractmethod
    def generate_algorithm_specific_plots(self) -> dict:
        pass
    
    def SHAP_analysis(self, X_sample, dependence_variable):
        if hasattr(self.model, "predict_proba"):
            pred_fn = lambda x: self.model.predict_proba(x)[:, 1]
        elif hasattr(self.model, "decision_function"):
            pred_fn = self.model.decision_function(x)[:, 1] if len(self.model.classes_)>2 else self.model.decision_function(x)
        else:
            pred_fn = self.model.predict
        try:
            explainer = shap.Explainer(self.model, X_sample)
            shap_values = explainer(X_sample, check_additivity=False)
        except TypeError:
            explainer = shap.Explainer(pred_fn, X_sample)
            try:
                shap_values = explainer(X_sample)
            except TypeError:
                shap_values = explainer(X_sample)
            
        if len(shap_values.shape) == 3:
            shap_values = shap_values[:, :, 1]
        print("\nSHAP values calculated successfully!")
        
        shap.summary_plot(shap_values, X_sample, plot_type="bar", show=False)
        summary_path = os.path.join(self.PLOT_DIR, "shap_summary.png")
        plt.savefig(summary_path)
        plt.close()
        
        sample_ind = 20
        shap.partial_dependence_plot(
            dependence_variable,
            pred_fn,
            X_sample,
            model_expected_value=True,
            feature_expected_value=True,
            ice=False,
            shap_values=shap_values[sample_ind : sample_ind + 1, :],
            show=False
        )
        pdp_path = os.path.join(self.PLOT_DIR, f"partial_dependence_{dependence_variable}_sample_{sample_ind}.png")
        plt.savefig(pdp_path)
        plt.close()
        
        values_to_plot = shap_values.values if hasattr(shap_values, 'values') else shap_values
        
        shap.dependence_plot(
            dependence_variable,
            values_to_plot,
            X_sample,
            show=False
        )
        effect_plot_path = os.path.join(self.PLOT_DIR, f"effect_plot_{dependence_variable}.png")
        plt.savefig(effect_plot_path)
        plt.close()
        
        return {
            "shap_summary": summary_path,
            "partial_dependence": pdp_path,
            "effect_plot": effect_plot_path
        }
    

    def export_results(self) -> dict:
        metrics = self.calculate_metrics()
        
        if hasattr(self.model, "coef_"):
            if len(self.model.classes_) == 2:
                weights = self.model.coef_[0]
            else:
                weights = list(self.model.coef_.T)
        elif hasattr(self.model, "feature_importances_"):
            weights = self.model.feature_importances_
        else:
            weights = [0] * len(self.X.columns)
            
        coef_df = pd.DataFrame({'Feature': self.X.columns, 'Peso/Coefficiente': weights})
        coef_csv_path = os.path.join(self.PLOT_DIR, 'coefficienti_pesi.csv')
        coef_df.to_csv(coef_csv_path, index=False)
        
        metriche = {
            "Accuracy": metrics["Accuracy"],
            "F1_Score": metrics["F1_Score"],
            "AUC": metrics["AUC"],
            "Precision": metrics["Precision"],
            "Recall": metrics["Recall"],
            "Confusion_Matrix": metrics["Confusion_Matrix"]
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