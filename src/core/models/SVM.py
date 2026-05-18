import os
import sklearn.svm
import optuna
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import config.datasets_config as data
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.inspection import DecisionBoundaryDisplay
from interface.classificationAlgo import BaseClassificationAlgo
        
class SVM(BaseClassificationAlgo):
    def __init__(self, dataset: str):
        super().__init__(model_name="SVM", dataset=dataset)
        self.scaler = StandardScaler()
        self.param_grid = {
              'C': [0.1, 1, 10, 100],   
              'gamma':['scale', 'auto', 0.1, 0.01, 0.001, 0.0001],
              'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],
              'class_weight': [None, 'balanced']
              }

    def fit(self, X_train, y_train, X_test, y_test):
        
        unique_classes = np.unique(y_train)
        if len(unique_classes) < 2:
            raise ValueError(f"Dati invalidi: y_train contiene una sola classe {unique_classes}. "
                         "Controlla il dataset o il caricamento.")
        
        def objective(trial):
            c = trial.suggest_float('C', 1e-2, 1e2, log=True)   
            kernel = trial.suggest_categorical('kernel', ['linear', 'rbf', 'poly', 'sigmoid'])
            gamma = trial.suggest_categorical('gamma', ['scale', 'auto'])
            degree = trial.suggest_int('degree', 2, 4) if kernel == 'poly' else 3
            class_weight = trial.suggest_categorical('class_weight', [None, 'balanced'])
            
            pipeline = Pipeline([
                ('scaler', StandardScaler()),
                ('svc', sklearn.svm.SVC(C=c, kernel=kernel, gamma=gamma, degree=degree, class_weight=class_weight, random_state=42))
            ])
            
            scores = cross_val_score(pipeline, X_train, y_train.values, cv=5, scoring='roc_auc', n_jobs=-1)
            return scores.mean()
            
        
        print("Inizio ottimizzazione iperparametri con Optuna (Tree-structured Parzen Estimators)...")
        optuna.logging.set_verbosity(optuna.logging.WARNING)
        
        study = optuna.create_study(direction='maximize')
        study.optimize(objective, n_trials=30)
        
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
        ])
        
        self.model.fit(X_train, y_train.values)
        final_svc = self.model.named_steps['svc']
        if hasattr(final_svc, "coef_"):
            self.model.coef_ = final_svc.coef_
        if hasattr(final_svc, "feature_importances_"):
            self.model.feature_importances_ = final_svc.feature_importances_
        
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