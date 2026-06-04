import os
import optuna
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
import src.core.config.datasets_config as data
from sklearn.preprocessing import StandardScaler
from src.core.interface.classificationAlgo import BaseClassificationAlgo
from sklearn.linear_model import LogisticRegression as SklearnLogisticRegression

import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="sklearn")
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")
        
class LogisticRegression(BaseClassificationAlgo):
    def __init__(self, dataset: str, dataset_path: str, param_grid: dict = None):
        super().__init__(model_name="Logistic Regression", dataset=dataset, dataset_path=dataset_path, param_grid=param_grid)
        self.scaler = StandardScaler()

    def fit(self, X_train, y_train, X_test, y_test):
        unique_classes = np.unique(y_train)
        if len(unique_classes) < 2:
            raise ValueError(f"Dati invalidi: y_train contiene una sola classe {unique_classes}. "
                             "Controlla il dataset o il caricamento.")
        scoring_metric = 'roc_auc_ovr' if len(unique_classes) > 2 else 'roc_auc'
        
        y_train_arr = y_train.values if hasattr(y_train, 'values') else y_train
        
        # 2. Funzione obiettivo per Optuna
        def objective(trial):
            if self.param_grid and 'C' in self.param_grid:
                c = trial.suggest_float('C', self.param_grid['C'][0], self.param_grid['C'][1], log=True)
            else:
                c = trial.suggest_float('C', 1e-4, 1e2, log=True)   
            
            if self.param_grid and 'solver' in self.param_grid:
                solver = trial.suggest_categorical('solver', self.param_grid['solver'])
            else:
                solver = trial.suggest_categorical('solver', ['lbfgs', 'liblinear'])
            if solver == 'lbfgs':
                model_params = {'C': c, 'solver': solver, 'max_iter': 2000, 'random_state': 42}
            else:
                penalty = trial.suggest_categorical('penalty', ['l1', 'l2'])
                l1_ratio = 1.0 if penalty == 'l1' else 0.0
                model_params = {
                    'C': c, 
                    'solver': solver, 
                    'penalty': penalty, 
                    'l1_ratio': l1_ratio,
                    'max_iter': 2000, 
                    'random_state': 42
                }
            pipeline = Pipeline([
                ('scaler', StandardScaler()),
                ('logr', SklearnLogisticRegression(**model_params))
            ], memory=None)
            
            scores = cross_val_score(pipeline, X_train, y_train_arr, cv=5, scoring=scoring_metric, n_jobs=-1)
            return scores.mean()
            
        print("Inizio ottimizzazione iperparametri con Optuna (Logistic Regression)...")
        optuna.logging.set_verbosity(optuna.logging.WARNING)
        
        study = optuna.create_study(direction='maximize')
        study.optimize(objective, n_trials=30, show_progress_bar=True)
        
        print(f"Migliori parametri individuati da Optuna: {study.best_params}")
        
        best_p = study.best_params
        final_solver = best_p.get('solver', 'lbfgs')
        final_params = {
            'C': best_p['C'],
            'solver': final_solver,
            'max_iter': 2000,
            'random_state': 42
        }
        if final_solver != 'lbfgs' and 'penalty' in best_p:
            final_params['penalty'] = best_p['penalty']
            final_params['l1_ratio'] = 1.0 if best_p['penalty'] == 'l1' else 0.0

        self.model = Pipeline([
            ('scaler', StandardScaler()),
            ('logr', SklearnLogisticRegression(**final_params))
        ], memory=None)
        
        self.model.fit(X_train, y_train_arr)
        
        final_logr = self.model.named_steps['logr']
        
        type(self.model).coef_ = property(lambda s: final_logr.coef_)
        type(self.model).classes_ = property(lambda s: final_logr.classes_)
        
        if isinstance(X_test, pd.DataFrame):
            X_test_num = X_test.select_dtypes(include=[np.number])
            self.X = X_test_num.reindex(columns=X_train.columns, fill_value=0).astype(np.float64)
        else:
            self.X = pd.DataFrame(X_test, columns=X_train.columns).astype(np.float64)
            
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
    logr_model = LogisticRegression(dataset=default_dataset, dataset_path=data.DATASETS[default_dataset]["path"])
    drop_columns = data.DATASETS[default_dataset]["drop_columns"]
    objective_column = data.DATASETS[default_dataset]["objective_column"]

    logr_model.import_data(logr_model.dataset_path, drop_columns, objective_column)
    logr_model.fit(logr_model.X, logr_model.y, None, None)
    logr_model.calculate_metrics()
    logr_model.generate_plots()
    logr_model.generate_algorithm_specific_plots()
    logr_model.export_results()