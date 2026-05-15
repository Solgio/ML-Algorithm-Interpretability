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
        
        self.X = pd.DataFrame(X_train_scaled, columns=X_train.columns)
        self.y = y_train
        
        self.model = SklearnLogisticRegression()
        self.model.fit(self.X, self.y)
    
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
        
        plot_path = os.path.join(self.PLOT_DIR, "logistic_sigmoid_plot.png")
        plt.savefig(plot_path)
        plt.close()
        
        print(f"Sigmoid plot saved at: {plot_path}")
        return {"sigmoid_plot": plot_path}

if __name__ == "__main__":
    lr_model = LogisticRegression(dataset="Student Placed-Not Placed Dataset")
    dataset_path = data.DATASETS["Student Placed-Not Placed Dataset"]["path"]
    drop_columns = data.DATASETS["Student Placed-Not Placed Dataset"]["drop_columns"]
    objective_column = data.DATASETS["Student Placed-Not Placed Dataset"]["objective_column"]

    lr_model.import_data(dataset_path, drop_columns, objective_column)