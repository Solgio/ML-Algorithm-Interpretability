import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import plot_tree
from config.datasets_config import DATASETS as data
from interface.classificationAlgo import BaseClassificationAlgo
from sklearn.tree import DecisionTreeClassifier as SklearnDecisionTreeClassifier

from interface.regressionAlgo import BaseRegressionAlgo
from sklearn.tree import DecisionTreeRegressor as SklearnDecisionTreeRegressor

class DecisionTreeC(BaseClassificationAlgo):
    def __init__(self, dataset: str):
        super().__init__(dataset=dataset, model_name="Decision Tree C")

    def fit(self, X_train, y_train, X_test, y_test):
        
        self.model = SklearnDecisionTreeClassifier(
            random_state=42,
            ccp_alpha=0.01
            )   
        self.model.fit(X_train, y_train)
        
        self.X = X_test
        self.y = y_test
                
    def generate_algorithm_specific_plots(self) -> dict:
        plot_paths = {}
        plt.figure(figsize=(24, 12)) 
        feature_names = self.X.columns.tolist() if hasattr(self.X, 'columns') else None
        class_names = [str(c) for c in self.model.classes_] if hasattr(self.model, 'classes_') else None
        plot_tree(
            self.model,
            feature_names=feature_names,
            class_names=class_names,
            filled=True,     
            rounded=True,    
            max_depth=3,     
            fontsize=10
        )        
        plt.title("Struttura dell'Albero di Decisione (Classificazione - Primi 3 livelli)")
        tree_path = os.path.join(self.PLOT_DIR, "decision_tree_structure.png")
        plt.savefig(tree_path, bbox_inches='tight') 
        plt.close()
        
        plot_paths["decision_tree_structure"] = tree_path
        print(f"Plot dell'albero salvato in: {tree_path}")
        
        plt.figure(figsize=(10, 6))
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1]
        
        plt.bar(range(len(indices)), importances[indices], color='forestgreen')
        plt.xticks(range(len(indices)), [feature_names[i] for i in indices], rotation=45, ha='right')
        plt.title("Decision Tree: Feature Importance")
        imp_path = os.path.join(self.PLOT_DIR, "dt_feature_importance.png")
        plt.savefig(imp_path, bbox_inches='tight')
        plt.close()
        
        plot_paths["feature_importance"] = imp_path
        return plot_paths

class DecisionTreeR(BaseRegressionAlgo):
    def __init__(self, dataset: str):
        super().__init__(dataset=dataset, model_name="Decision Tree R")

    def fit(self, X_train, y_train, X_test, y_test):
                
        self.model = SklearnDecisionTreeRegressor(random_state=42, ccp_alpha=0.01)
        self.model.fit(X_train, y_train)
        
        self.X = X_test
        self.y = y_test
        
    def generate_algorithm_specific_plots(self) -> dict:
        plot_paths = {}

        plt.figure(figsize=(24, 12)) 
        feature_names = self.X.columns.tolist() if hasattr(self.X, 'columns') else None
        class_names = [str(c) for c in self.model.classes_] if hasattr(self.model, 'classes_') else None
        plot_tree(
            self.model,
            feature_names=feature_names,
            class_names=class_names,
            filled=True,     
            rounded=True,    
            max_depth=3,     
            fontsize=10
        )        
        plt.title("Struttura dell'Albero di Decisione (Classificazione - Primi 3 livelli)")
        tree_path = os.path.join(self.PLOT_DIR, "decision_tree_structure.png")
        plt.savefig(tree_path, bbox_inches='tight') 
        plt.close()
        
        print(f"Plot dell'albero salvato in: {tree_path}")
        
        plot_paths["decision_tree_structure"] = tree_path

        plt.figure(figsize=(10, 6))
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1]
        
        plt.bar(range(len(indices)), importances[indices], color='forestgreen')
        plt.xticks(range(len(indices)), [feature_names[i] for i in indices], rotation=45, ha='right')
        plt.title("Decision Tree: Feature Importance")
        imp_path = os.path.join(self.PLOT_DIR, "dt_feature_importance.png")
        plt.savefig(imp_path, bbox_inches='tight')
        plt.close()

        plot_paths["feature_importance"] = imp_path
        return plot_paths

if __name__ == "__main__":
    
    print("--- Test Decision Tree Classification ---")
    default_dataset = "Student Placed-Not Placed Dataset"
    dt_model = DecisionTreeC(dataset=default_dataset)
    dataset_path = data.DATASETS[default_dataset]["path"]
    drop_columns = data.DATASETS[default_dataset]["drop_columns"]
    objective_column = data.DATASETS[default_dataset]["objective_column"]

    dt_model.import_data(dataset_path, drop_columns, objective_column)
    dt_model.fit(dt_model.X, dt_model.y, None, None)
    dt_model.generate_algorithm_specific_plots()
    
    print("\n--- Test Decision Tree Regression ---")
    default_dataset = "Student Salary Dataset"
    dt_model = DecisionTreeR(dataset=default_dataset)
    dataset_path = data.DATASETS[default_dataset]["path"]
    drop_columns = data.DATASETS[default_dataset]["drop_columns"]
    objective_column = data.DATASETS[default_dataset]["objective_column"]

    dt_model.import_data(dataset_path, drop_columns, objective_column)
    dt_model.fit(dt_model.X, dt_model.y, None, None)
    dt_model.calculate_metrics()
    dt_model.generate_plots()
    dt_model.generate_algorithm_specific_plots()
    dt_model.export_results()