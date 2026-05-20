import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import config.datasets_config as data
from sklearn.preprocessing import StandardScaler
from interface.classificationAlgo import BaseClassificationAlgo
from sklearn.linear_model import LogisticRegression as SklearnLogisticRegression
        
class LogisticRegression(BaseClassificationAlgo):
    def __init__(self, dataset: str, param_grid: dict = None):
        super().__init__(model_name="Logistic Regression", dataset=dataset, param_grid=param_grid)
        self.scaler = StandardScaler()

    def fit(self, X_train, y_train, X_test, y_test):
        x_train_scaled = self.scaler.fit_transform(X_train)
        x_test_scaled = self.scaler.transform(X_test)
        
        self.model = SklearnLogisticRegression()
        self.model.fit(pd.DataFrame(x_train_scaled, columns=X_train.columns), y_train)
        
        self.X = pd.DataFrame(x_test_scaled, columns=X_test.columns)
        self.y = y_test
    
    def generate_algorithm_specific_plots(self) -> dict:
        import numpy as np
        
        z = self.model.decision_function(self.X)
        probabilities = self.model.predict_proba(self.X)[:, 1]
        
        sorted_indices = np.argsort(z)
        z_sorted = z[sorted_indices]
        prob_sorted = probabilities[sorted_indices]
        
        plot_paths = {}
        
        is_binary = len(self.model.classes_) == 2
        
        if is_binary:
            plt.figure(figsize=(10, 6))
            plt.scatter(z, self.y, alpha=0.4, label='Valori Reali (0 = Not Placed, 1 = Placed)', color='orange', marker='o')
            plt.plot(z_sorted, prob_sorted, color='blue', linewidth=3, label='Curva Sigmoide (Probabilità)')
            plt.xlabel("Log-Odds / Decision Function ($z$)")
            plt.ylabel("Probabilità (placed)")
            plt.title("Regressione Logistica: Curva Sigmoide")
            plt.legend()
            plt.grid(True, alpha=0.3)
            
            sigmoid_plot = os.path.join(self.PLOT_DIR, "logistic_sigmoid_plot.png")
            plot_paths["sigmoid_plot"] = sigmoid_plot
            plt.savefig(sigmoid_plot)
            plt.close()
            
            coefs = self.model.coef_[0]
            plt.figure(figsize=(10, 6))
            odds_ratios = np.exp(coefs)

            feature_names = self.X.columns
            sorted_idx = np.argsort(np.abs(coefs))

            plt.barh(range(len(sorted_idx)), coefs[sorted_idx], color='purple')
            plt.yticks(range(len(sorted_idx)), [feature_names[i] for i in sorted_idx])
            plt.title('Logistic Regression: Coefficienti (Log-Odds)')
            
            print("\n--- Analisi Odds Ratio ---")
            for i in sorted_idx[::-1]:
                print(f"{feature_names[i]}: Coefficiente = {coefs[i]:.4f} -> Odds Ratio = {odds_ratios[i]:.4f}")

        else:
            print("Avviso: Curva sigmoide saltata (non supportata visivamente per il multi-classe).")
            
            plt.figure(figsize=(12, 8))
            sns.heatmap(self.model.coef_, xticklabels=self.X.columns, yticklabels=self.model.classes_, cmap='coolwarm', center=0)
            plt.title('Logistic Regression: Coefficienti per Classe (Log-Odds)')
            plt.xlabel('Features')
            plt.ylabel('Classi')
            
        weight_path = os.path.join(self.PLOT_DIR, "logistic_weight_plot.png")
        plt.savefig(weight_path, bbox_inches='tight')
        plt.close()
        plot_paths["weight_plot"] = weight_path
        
        return plot_paths

if __name__ == "__main__":
    default_dataset = "Student Salary Dataset"
    logr_model = LogisticRegression(dataset=default_dataset)
    dataset_path = data.DATASETS[default_dataset]["path"]
    drop_columns = data.DATASETS[default_dataset]["drop_columns"]
    objective_column = data.DATASETS[default_dataset]["objective_column"]

    logr_model.import_data(dataset_path, drop_columns, objective_column)
    logr_model.fit(logr_model.X, logr_model.y, None, None)
    logr_model.calculate_metrics()
    logr_model.generate_plots()
    logr_model.generate_algorithm_specific_plots()
    logr_model.export_results()