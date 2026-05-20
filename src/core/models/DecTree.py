import os
import matplotlib.pyplot as plt
import optuna
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.tree import plot_tree
from sklearn.model_selection import cross_val_score
from config.datasets_config import DATASETS as data
from interface.classificationAlgo import BaseClassificationAlgo
from sklearn.tree import DecisionTreeClassifier as SklearnDecisionTreeClassifier

from interface.regressionAlgo import BaseRegressionAlgo
from sklearn.tree import DecisionTreeRegressor as SklearnDecisionTreeRegressor

class DecisionTreeC(BaseClassificationAlgo):
    def __init__(self, dataset: str, param_grid: dict = None):
        super().__init__(dataset=dataset, model_name="Decision Tree C", param_grid=param_grid)

    def fit(self, X_train, y_train, X_test, y_test):
        unique_classes = np.unique(y_train)
        if len(unique_classes) < 2:
            raise ValueError(f"Dati invalidi: y_train contiene una sola classe {unique_classes}. "
                         "Controlla il dataset o il caricamento.")
        scoring_metric = 'roc_auc_ovr' if len(unique_classes) > 2 else 'roc_auc'
        
        def objective(trial):
            params = {
                'criterion': trial.suggest_categorical('criterion', self.param_grid['criterion']),
                'max_depth': trial.suggest_categorical('max_depth', self.param_grid['max_depth']),
                'min_samples_split': trial.suggest_int('min_samples_split', self.param_grid['min_samples_split'][0], self.param_grid['min_samples_split'][1]),
                'min_samples_leaf': trial.suggest_int('min_samples_leaf', self.param_grid['min_samples_leaf'][0], self.param_grid['min_samples_leaf'][1]),
                'ccp_alpha': trial.suggest_float('ccp_alpha', self.param_grid['ccp_alpha'][0], self.param_grid['ccp_alpha'][1])
            }
            
            pipeline = Pipeline([
                ('dt', SklearnDecisionTreeClassifier(  # nosonar - False positive per parametri dinamici
                    **params,
                    random_state=42
                ))
            ], memory=None)
            
            scores = cross_val_score(pipeline, X_train, y_train.values, cv=5, scoring=scoring_metric, n_jobs=-1)
            return scores.mean()
        
        print("Inizio ottimizzazione iperparametri con Optuna (Tree-structured Parzen Estimators)...")
        optuna.logging.set_verbosity(optuna.logging.WARNING)
        
        study = optuna.create_study(direction='maximize')
        study.optimize(objective, n_trials=30, n_jobs=-1, show_progress_bar=True)
        
        print(f"Migliori parametri individuati da Optuna: {study.best_params}")
        
        best_p = study.best_params
        self.model = Pipeline([
            ('dt', SklearnDecisionTreeClassifier(  # nosonar - False positive per parametri dinamici
                **best_p,
                random_state=42
            ))
        ], memory=None)
        
        self.model.fit(X_train, y_train.values)
                
        self.X = X_test
        self.y = y_test
                
    def generate_algorithm_specific_plots(self) -> dict:
        plot_paths = {}
        plt.figure(figsize=(24, 12)) 
        tree_model = self.model.named_steps['dt'] if isinstance(self.model, Pipeline) else self.model
        
        feature_names = self.X.columns.tolist() if hasattr(self.X, 'columns') else None
        class_names = [str(c) for c in tree_model.classes_]
        plot_tree(
            tree_model,
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
        importances = tree_model.feature_importances_
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
                
        def objective(trial):
            params = {
                'criterion': trial.suggest_categorical('criterion', self.param_grid['criterion']),
                'max_depth': trial.suggest_categorical('max_depth', self.param_grid['max_depth']),
                'min_samples_split': trial.suggest_int('min_samples_split', self.param_grid['min_samples_split'][0], self.param_grid['min_samples_split'][1]),
                'min_samples_leaf': trial.suggest_int('min_samples_leaf', self.param_grid['min_samples_leaf'][0], self.param_grid['min_samples_leaf'][1]),
                'ccp_alpha': trial.suggest_float('ccp_alpha', self.param_grid['ccp_alpha'][0], self.param_grid['ccp_alpha'][1])
            }
            
            pipeline = Pipeline([
                ('dt', SklearnDecisionTreeRegressor(  # nosonar - False positive per parametri dinamici
                    **params,
                    random_state=42
                ))
            ], memory=None)
            
            scores = cross_val_score(pipeline, X_train, y_train.values, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
            return scores.mean()
        
        print("Inizio ottimizzazione iperparametri con Optuna (Tree-structured Parzen Estimators)...")
        optuna.logging.set_verbosity(optuna.logging.WARNING)
        
        study = optuna.create_study(direction='maximize')
        study.optimize(objective, n_trials=30, n_jobs=-1, show_progress_bar=True)
        
        print(f"Migliori parametri individuati da Optuna: {study.best_params}")
        
        best_p = study.best_params
        self.model = Pipeline([
            ('dt', SklearnDecisionTreeRegressor( # nosonar - False positive per parametri dinamici
                **best_p,
                random_state=42
            ))
        ], memory=None)
        
        self.model.fit(X_train, y_train.values)
                
        self.X = X_test
        self.y = y_test
        
    def generate_algorithm_specific_plots(self) -> dict:
        plot_paths = {}

        plt.figure(figsize=(24, 12)) 
        tree_model = self.model.named_steps['dt'] if isinstance(self.model, Pipeline) else self.model
        
        feature_names = self.X.columns.tolist() if hasattr(self.X, 'columns') else None
        plot_tree(
            tree_model,
            feature_names=feature_names,
            class_names=None,
            filled=True,     
            rounded=True,    
            max_depth=3,     
            fontsize=10
        )        
        plt.title("Struttura dell'Albero di Decisione (Regresione - Primi 3 livelli)")
        tree_path = os.path.join(self.PLOT_DIR, "decision_tree_structure.png")
        plt.savefig(tree_path, bbox_inches='tight') 
        plt.close()
        
        print(f"Plot dell'albero salvato in: {tree_path}")
        
        plot_paths["decision_tree_structure"] = tree_path

        plt.figure(figsize=(10, 6))
        importances = tree_model.feature_importances_
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