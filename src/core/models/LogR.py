import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import config.datasets_config as data
from sklearn.preprocessing import StandardScaler
from interface.classificationAlgo import BaseClassificationAlgo
from sklearn.linear_model import LogisticRegression as SklearnLogisticRegression
        
class LogisticRegression(BaseClassificationAlgo):
    def __init__(self, dataset: str):
        super().__init__(model_name="Logistic Regression", dataset=dataset)
        self.scaler = StandardScaler()

    def fit(self, X_train, y_train, X_test, y_test):
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        self.model = SklearnLogisticRegression()
        self.model.fit(pd.DataFrame(X_train_scaled, columns=X_train.columns), y_train)
        
        self.X = pd.DataFrame(X_test_scaled, columns=X_test.columns)
        self.y = y_test
    
    def generate_algorithm_specific_plots(self) -> dict:
        import numpy as np
        
        z = self.model.decision_function(self.X)
        probabilities = self.model.predict_proba(self.X)[:, 1]
        
        sorted_indices = np.argsort(z)
        z_sorted = z[sorted_indices]
        prob_sorted = probabilities[sorted_indices]
        
        plt.figure(figsize=(10, 6))
        plt.scatter(z, self.y, alpha=0.4, label='Valori Reali (0 = Not Placed, 1 = Placed)', color='orange', marker='o')
        plt.plot(z_sorted, prob_sorted, color='blue', linewidth=3, label='Curva Sigmoide (Probabilità)')
        plt.xlabel("Log-Odds / Decision Function ($z$)")
        plt.ylabel("Probabilità (placed)")
        plt.title("Regressione Logistica: Curva Sigmoide")
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plot_paths = {}
        sigmoid_plot = os.path.join(self.PLOT_DIR, "logistic_sigmoid_plot.png")
        plot_paths["sigmoid_plot"] = sigmoid_plot
        plt.savefig(sigmoid_plot)
        plt.close()
        plt.figure(figsize=(10, 6))
        coefs = self.model.coef_[0]
        odds_ratios = np.exp(coefs)
        
        feature_names = self.X.columns
        sorted_idx = np.argsort(np.abs(coefs))
        
        plt.barh(range(len(sorted_idx)), coefs[sorted_idx], color='purple')
        plt.yticks(range(len(sorted_idx)), [feature_names[i] for i in sorted_idx])
        plt.title('Logistic Regression: Coefficienti (Log-Odds)')
        
        print("\n--- Analisi Odds Ratio ---")
        for i in sorted_idx[::-1]:
            print(f"{feature_names[i]}: Coefficiente = {coefs[i]:.4f} -> Odds Ratio = {odds_ratios[i]:.4f}")
            
        weight_path = os.path.join(self.PLOT_DIR, "logistic_weight_plot.png")
        plt.savefig(weight_path, bbox_inches='tight')
        plt.close()
        plot_paths["weight_plot"] = weight_path
    
        return {"sigmoid_plot": sigmoid_plot, "weight_plot": weight_path}

if __name__ == "__main__":
    lr_model = LogisticRegression(dataset="Student Placed-Not Placed Dataset")
    dataset_path = data.DATASETS["Student Placed-Not Placed Dataset"]["path"]
    drop_columns = data.DATASETS["Student Placed-Not Placed Dataset"]["drop_columns"]
    objective_column = data.DATASETS["Student Placed-Not Placed Dataset"]["objective_column"]

    lr_model.import_data(dataset_path, drop_columns, objective_column)