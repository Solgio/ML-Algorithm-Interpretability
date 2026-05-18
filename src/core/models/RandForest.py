import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from config.datasets_config import DATASETS as data
from interface.classificationAlgo import BaseClassificationAlgo
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor 

from interface.regressionAlgo import BaseRegressionAlgo

class RandomForestC(BaseClassificationAlgo):
    def __init__(self, dataset: str):
        super().__init__(dataset=dataset, model_name="Random Forest C")

    def fit(self, X_train, y_train, X_test, y_test):
        
        self.model = RandomForestClassifier(
            random_state=42, 
            oob_score=True,
            min_samples_leaf=1,
            max_features="sqrt")
        self.model.fit(X_train, y_train)
        
        self.X = X_test
        self.y = y_test
        
    def generate_algorithm_specific_plots(self) -> dict:
        
        plot_paths = {}
        
        plt.figure(figsize=(24, 12)) 
        feature_names = self.X.columns.tolist() if hasattr(self.X, 'columns') else None
        class_names = [str(c) for c in self.model.classes_] if hasattr(self.model, 'classes_') else None
        
        single_tree = self.model.estimators_[0]
        
        plot_tree(
            single_tree,
            feature_names=feature_names,
            class_names=class_names,
            filled=True,     
            rounded=True,    
            max_depth=3,     
            fontsize=10
        )        
        plt.title("Struttura di un Albero (Estratto dalla Random Forest - Primi 3 livelli)")
        tree_path = os.path.join(self.PLOT_DIR, "rf_single_tree_structure.png")
        plt.savefig(tree_path, bbox_inches='tight') 
        plt.close()
        plot_paths["single_tree_structure"] = tree_path
        
        plt.figure(figsize=(10, 6))
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1]
        
        top_n = min(15, self.X.shape[1])
        
        plt.bar(range(top_n), importances[indices][:top_n], align="center", color="teal")
        plt.xticks(range(top_n), [feature_names[i] for i in indices][:top_n], rotation=45, ha='right')
        plt.title("Random Forest: Feature Importance (Impurità Media)")
        plt.ylabel("Importanza Relativa")
        plt.tight_layout()
        
        imp_path = os.path.join(self.PLOT_DIR, "rf_feature_importance.png")
        plt.savefig(imp_path)
        plt.close()
        plot_paths["feature_importance"] = imp_path

        print(f"Plot salvati in: {self.PLOT_DIR}")
        return plot_paths
    
class RandomForestR(BaseRegressionAlgo):
    def __init__(self, dataset: str):
        super().__init__(dataset=dataset, model_name="Random Forest R")

    def fit(self, X_train, y_train, X_test, y_test):
        
        self.model = RandomForestRegressor(
            random_state=42,
            oob_score=True,
            min_samples_leaf=1,
            max_features="sqrt"
        )
        self.model.fit(X_train, y_train)
        
        self.X = X_test
        self.y = y_test
        
    def generate_algorithm_specific_plots(self) -> dict:
        
        plot_paths = {}
        
        plt.figure(figsize=(24, 12)) 
        feature_names = self.X.columns.tolist() if hasattr(self.X, 'columns') else None
        
        single_tree = self.model.estimators_[0]
        
        plot_tree(
            single_tree,
            feature_names=feature_names,
            filled=True,     
            rounded=True,    
            max_depth=3,     
            fontsize=10
        )        
        plt.title("Struttura di un Albero (Regressione - Estratto dalla RF - Primi 3 livelli)")
        tree_path = os.path.join(self.PLOT_DIR, "rf_single_tree_structure.png")
        plt.savefig(tree_path, bbox_inches='tight') 
        plt.close()
        plot_paths["single_tree_structure"] = tree_path
        
        plt.figure(figsize=(10, 6))
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1]
        
        top_n = min(15, self.X.shape[1])
        
        plt.bar(range(top_n), importances[indices][:top_n], align="center", color="coral")
        plt.xticks(range(top_n), [feature_names[i] for i in indices][:top_n], rotation=45, ha='right')
        plt.title("Random Forest Regression: Feature Importance")
        plt.ylabel("Importanza Relativa (Riduzione MSE)")
        plt.tight_layout()
        
        imp_path = os.path.join(self.PLOT_DIR, "rf_feature_importance.png")
        plt.savefig(imp_path)
        plt.close()
        plot_paths["feature_importance"] = imp_path

        print(f"Plot salvati in: {self.PLOT_DIR}")
        return plot_paths

if __name__ == "__main__":
    
    print("\n--- Test Random Forest Classification ---")
    default_dataset = "Student Placed-Not Placed Dataset"
    rf_model_c = RandomForestC(dataset=default_dataset)
    dataset_path = data.DATASETS[default_dataset]["path"]
    drop_columns = data.DATASETS[default_dataset]["drop_columns"]
    objective_column = data.DATASETS[default_dataset]["objective_column"]

    rf_model_c.import_data(dataset_path, drop_columns, objective_column)
    rf_model_c.fit(rf_model_c.X, rf_model_c.y, None, None)
    rf_model_c.calculate_metrics()
    rf_model_c.generate_plots()
    rf_model_c.generate_algorithm_specific_plots()
    rf_model_c.export_results()

    print("\n--- Test Random Forest Regression ---")
    default_dataset = "Student Salary Dataset"
    rf_model_r = RandomForestR(dataset=default_dataset)
    dataset_path = data.DATASETS[default_dataset]["path"]
    drop_columns = data.DATASETS[default_dataset]["drop_columns"]
    objective_column = data.DATASETS[default_dataset]["objective_column"]

    rf_model_r.import_data(dataset_path, drop_columns, objective_column)
    rf_model_r.fit(rf_model_r.X, rf_model_r.y, None, None)
    rf_model_r.calculate_metrics()
    rf_model_r.generate_plots()
    rf_model_r.generate_algorithm_specific_plots()
    rf_model_r.export_results()