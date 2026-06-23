import os
import shap
import sklearn.svm
import optuna
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import src.core.config.datasets_config as data
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.inspection import DecisionBoundaryDisplay
from src.core.interface.classificationAlgo import BaseClassificationAlgo
        
class SVM(BaseClassificationAlgo):
    def __init__(self, dataset: str, dataset_path: str, param_grid: dict = None):
        super().__init__(dataset=dataset, dataset_path=dataset_path, model_name="SVM", param_grid=param_grid)
        self.scaler = StandardScaler()

    def fit(self, X_train, y_train, X_test, y_test):
        unique_classes = np.unique(y_train)
        if len(unique_classes) < 2:
            raise ValueError(f"Invalid data: y_train contains only one class {unique_classes}. "
                         "Check the dataset or loading.")
        scoring_metric = 'roc_auc_ovr' if len(unique_classes) > 2 else 'roc_auc'
        X_train_arr = np.asarray(X_train, dtype=np.float64)
        y_train_arr = np.asarray(y_train).ravel()
        
        def objective(trial):
            c = trial.suggest_float('C',self.param_grid['C'][0], self.param_grid['C'][1], log=True)   
            kernel = trial.suggest_categorical('kernel', self.param_grid['kernel'])
            gamma = trial.suggest_categorical('gamma', self.param_grid['gamma'])
            degree = trial.suggest_int('degree', self.param_grid['degree'][0], self.param_grid['degree'][1]) if kernel == 'poly' else 3
            class_weight = trial.suggest_categorical('class_weight', self.param_grid['class_weight'])
            
            pipeline = Pipeline([
                ('scaler', StandardScaler()),
                ('svc', sklearn.svm.SVC(C=c, kernel=kernel, gamma=gamma, degree=degree, class_weight=class_weight, random_state=42, probability=True))
            ], memory=None)
            
            scores = cross_val_score(pipeline, X_train_arr, y_train_arr, cv=5, scoring=scoring_metric, n_jobs=-1)
            return scores.mean()
            
        
        print("Inizio ottimizzazione iperparametri con Optuna (Tree-structured Parzen Estimators)...")
        optuna.logging.set_verbosity(optuna.logging.WARNING)
        
        study = optuna.create_study(direction='maximize')
        study.optimize(objective, n_trials=30, show_progress_bar=True)
        
        print(f"Migliori parametri individuati da Optuna: {study.best_params}")
        
        best_p = study.best_params
        self.model = Pipeline([
            ('scaler', StandardScaler()),
            ('svc', sklearn.svm.SVC(
                C=best_p['C'],
                kernel=best_p['kernel'],
                gamma=best_p['gamma'],
                degree=best_p.get('degree', 3),
                class_weight=best_p['class_weight'],
                probability=True,
                random_state=42
            ))
        ], memory=None)
        
        self.model.fit(X_train_arr, y_train_arr)
        #final_svc = self.model.named_steps['svc']
        #if hasattr(final_svc, "coef_"):
        #    self.model.coef_ = final_svc.coef_
        #if hasattr(final_svc, "feature_importances_"):
        #    self.model.feature_importances_ = final_svc.feature_importances_
        
        self.X = X_test
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
        
        _ = ax.scatter(
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
    svm_model = SVM(dataset=default_dataset, dataset_path=data.DATASETS[default_dataset]["path"])
    drop_columns = data.DATASETS[default_dataset]["drop_columns"]
    objective_column = data.DATASETS[default_dataset]["objective_column"]

    svm_model.import_data(svm_model.dataset_path, drop_columns, objective_column)
    svm_model.fit(svm_model.X, svm_model.y, None, None)
    svm_model.calculate_metrics()
    svm_model.generate_plots()
    svm_model.generate_algorithm_specific_plots()
    svm_model.export_results()