import os
import sklearn.svm
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import config.datasets_config as data
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.inspection import DecisionBoundaryDisplay
from interface.classificationAlgo import BaseClassificationAlgo
        
class SVM(BaseClassificationAlgo):
    def __init__(self, dataset: str):
        super().__init__(model_name="SVM", dataset=dataset)
        self.scaler = StandardScaler()

    def fit(self, X_train, y_train, X_test, y_test):
        x_train_scaled = self.scaler.fit_transform(X_train)
        x_test_scaled = self.scaler.transform(X_test)
        
        self.model = sklearn.svm.SVC(kernel='sigmoid', C=1.0, gamma='scale', probability=True, random_state=42)
        self.model.fit(pd.DataFrame(x_train_scaled, columns=X_train.columns), y_train)
        
        self.X = pd.DataFrame(x_test_scaled, columns=X_test.columns)
        self.y = y_test
    
    def generate_algorithm_specific_plots(self) -> dict:
        plot_paths = {}
        
        plt.figure(figsize=(10, 6))
        
        if self.X.shape[1] > 2:
            pca = PCA(n_components=2, random_state=42)
            x_vis = pca.fit_transform(self.X)
            
            model_vis = sklearn.svm.SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
            model_vis.fit(x_vis, self.y)
            title = "SVM Decision Boundary (Proiezione 2D via PCA)"
        else:
            x_vis = self.X.values
            model_vis = self.model
            title = "SVM Decision Boundary"

        ax = plt.gca()
        DecisionBoundaryDisplay.from_estimator(
            model_vis,
            x_vis,
            response_method="predict",
            cmap=plt.cm.coolwarm,
            alpha=0.6,
            ax=ax
        )
        y_numeric = pd.Categorical(self.y).codes
        
        scatter = ax.scatter(
            x_vis[:, 0], 
            x_vis[:, 1], 
            c=y_numeric, 
            edgecolors='k', 
            cmap=plt.cm.coolwarm,
            s=50
        )
        support_vectors = model_vis.support_vectors_
        ax.scatter(
            support_vectors[:, 0],
            support_vectors[:, 1],
            s=100, linewidth=1.5, facecolors='none', edgecolors='k',
            label='Support Vectors'
        )
        plt.legend()
        
        plt.title(title)
        plt.xlabel("Componente 1" if self.X.shape[1] > 2 else self.X.columns[0])
        plt.ylabel("Componente 2" if self.X.shape[1] > 2 else self.X.columns[1])
        
        plot_paths["SVM decision function"] = os.path.join(self.PLOT_DIR, "svm_decision_function.png")
        plt.savefig(plot_paths["SVM decision function"], bbox_inches="tight")
        plt.close()
        
        return plot_paths

if __name__ == "__main__":
    default_dataset = "Student Placed-Not Placed Dataset"
    svm_model = SVM(dataset=default_dataset)
    dataset_path = data.DATASETS[default_dataset]["path"]
    drop_columns = data.DATASETS[default_dataset]["drop_columns"]
    objective_column = data.DATASETS[default_dataset]["objective_column"]

    svm_model.import_data(dataset_path, drop_columns, objective_column)
    svm_model.fit(svm_model.X, svm_model.y, None, None)
    svm_model.calculate_metrics()
    svm_model.generate_plots()
    svm_model.generate_algorithm_specific_plots()
    svm_model.export_results()