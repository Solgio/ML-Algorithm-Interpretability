import os
import optuna
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
import xgboost as xgb
import matplotlib.pyplot as plt
import shap
from sklearn.preprocessing import LabelEncoder
from config.datasets_config import DATASETS as data
from interface.classificationAlgo import BaseClassificationAlgo
from interface.regressionAlgo import BaseRegressionAlgo

class XGBoostC(BaseClassificationAlgo):
    def __init__(self, dataset: str):
        super().__init__(dataset=dataset, model_name="XGBoost C")

    def fit(self, X_train, y_train, X_test, y_test):
        self.le = LabelEncoder()
        y_train_encoded = self.le.fit_transform(y_train)
        y_test_encoded = self.le.transform(y_test)
        
        num_classes = len(np.unique(y_train_encoded))
        current_objective = "mlogloss" if num_classes > 2 else "logloss"
        scoring_metric = 'roc_auc_ovr' if num_classes > 2 else 'roc_auc'
        def objective(trial):
            params = {
                'n_estimators': trial.suggest_categorical('n_estimators', self.param_grid['n_estimators']),
                'max_depth': trial.suggest_int('max_depth', self.param_grid['max_depth'][0], self.param_grid['max_depth'][1]),
                'learning_rate': trial.suggest_categorical('learning_rate', self.param_grid['learning_rate']),
                'subsample': trial.suggest_float('subsample', self.param_grid['subsample'][0], self.param_grid['subsample'][1]),
                'colsample_bytree': trial.suggest_float('colsample_bytree', self.param_grid['colsample_bytree'][0], self.param_grid['colsample_bytree'][1]),
                'gamma': trial.suggest_float('gamma', self.param_grid['gamma'][0], self.param_grid['gamma'][1])
            }
            
            pipeline = Pipeline([
                ('xgb', xgb.XGBClassifier(
                    **params,
                    random_state=42,
                    eval_metric=current_objective
                ))
            ], memory=None)
            
            scores = cross_val_score(pipeline, X_train, y_train_encoded, cv=5, scoring=scoring_metric, n_jobs=-1)
            return scores.mean()

        print("Inizio ottimizzazione iperparametri con Optuna (Tree-structured Parzen Estimators)...")
        optuna.logging.set_verbosity(optuna.logging.WARNING)
        study = optuna.create_study(direction='maximize')
        study.optimize(objective, n_trials=30, n_jobs=-1, show_progress_bar=True)
        print(f"Migliori parametri individuati da Optuna: {study.best_params}")
        best_p = study.best_params
        self.model = Pipeline([
            ('xgb', xgb.XGBClassifier(
                **best_p,
                random_state=42,
                eval_metric=current_objective
            ))
        ], memory=None)

        self.model.fit(
            X_train, y_train_encoded, xgb__eval_set=[(X_train, y_train_encoded), (X_test, y_test_encoded)], xgb__verbose=False)
        
        self.X = X_test
        self.y = y_test_encoded
        
        mapping = dict(zip(range(len(self.le.classes_)), self.le.classes_))
        print(f"\n  [INFO XGBoost] Legenda classi per i plot: {mapping}")
        
    def generate_algorithm_specific_plots(self) -> dict:
        plot_paths = {}
        xgb_model = self.model.named_steps['xgb'] if isinstance(self.model, Pipeline) else self.model
        
        plt.figure(figsize=(10, 6))
        xgb.plot_importance(xgb_model, importance_type='weight', max_num_features=15, title="XGBoost: Feature Importance (Frequency/Weight)")
        imp_weight_path = os.path.join(self.PLOT_DIR, "xgb_feature_importance_weight.png")
        plt.savefig(imp_weight_path, bbox_inches='tight')
        plt.close()
        plot_paths["feature_importance_weight"] = imp_weight_path

        plt.figure(figsize=(10, 6))
        xgb.plot_importance(xgb_model, importance_type='gain', max_num_features=15, title="XGBoost: Feature Importance (Gain)")
        imp_gain_path = os.path.join(self.PLOT_DIR, "xgb_feature_importance_gain.png")
        plt.savefig(imp_gain_path, bbox_inches='tight')
        plt.close()
        plot_paths["feature_importance_gain"] = imp_gain_path
        
        plt.figure(figsize=(10, 6))
        xgb.plot_importance(xgb_model, importance_type='cover', max_num_features=15, title="XGBoost: Feature Importance (Cover)")
        imp_cover_path = os.path.join(self.PLOT_DIR, "xgb_feature_importance_cover.png")
        plt.savefig(imp_cover_path, bbox_inches='tight')
        plt.close()
        plot_paths["feature_importance_cover"] = imp_cover_path

        try:
            _, ax = plt.subplots(figsize=(30, 15))
            xgb.plot_tree(xgb_model, num_trees=0, ax=ax)
            tree_path = os.path.join(self.PLOT_DIR, "xgb_tree_0.png")
            plt.savefig(tree_path, bbox_inches='tight', dpi=300)
            plt.close()
            plot_paths["tree_visualization"] = tree_path
        except Exception as e:
            print(f"Impossibile generare la visualizzazione dell'albero. Assicurati che graphviz sia installato. Errore: {e}")

        results = xgb_model.evals_result()
        if results:
            plt.figure(figsize=(8, 6))
            metric_key = next(iter(results['validation_0'].keys()))
            epochs = len(results['validation_0'][metric_key])
            x_axis = range(0, epochs)
            plt.plot(x_axis, results['validation_0'][metric_key], label='Train')
            plt.plot(x_axis, results['validation_1'][metric_key], label='Test')
            plt.legend()
            plt.ylabel('Log Loss' if metric_key == 'logloss' else 'Multi-Class Log Loss')
            plt.xlabel('Iterazioni (Alberi)')
            plt.title('XGBoost Learning Curve')
            lc_path = os.path.join(self.PLOT_DIR, "xgb_learning_curve.png")
            plt.savefig(lc_path)
            plt.close()
            plot_paths["learning_curve"] = lc_path
            
        print(f"Plot specifici XGBoost Classificazione salvati in: {self.PLOT_DIR}")
        return plot_paths

    def SHAP_analysis(self, x_sample, dependence_variable):
        xgb_model = self.model.named_steps['xgb'] if isinstance(self.model, Pipeline) else self.model
        explainer = shap.TreeExplainer(xgb_model)
        shap_values = explainer(x_sample)
        print("\nSHAP values (TreeExplainer) calcolati con successo!")
        
        shap.summary_plot(shap_values, x_sample, show=False)
        summary_path = os.path.join(self.PLOT_DIR, "shap_summary_xgb.png")
        plt.savefig(summary_path, bbox_inches='tight')
        plt.close()
        
        sample_ind = 0
        plt.figure(figsize=(10, 6))
        if len(shap_values.shape) == 3:
            shap.plots.waterfall(shap_values[sample_ind, :, 1], show=False)
        else:
            shap.plots.waterfall(shap_values[sample_ind], show=False)
            
        local_exp_path = os.path.join(self.PLOT_DIR, f"shap_local_explanation_sample_{sample_ind}.png")
        plt.savefig(local_exp_path, bbox_inches='tight')
        plt.close()

        return {
            "shap_summary": summary_path,
            "local_explanation": local_exp_path
        }


class XGBoostR(BaseRegressionAlgo):
    def __init__(self, dataset: str):
        super().__init__(dataset=dataset, model_name="XGBoost R")

    def fit(self, X_train, y_train, X_test, y_test):
        
        def objective(trial):
            params = {
                'n_estimators': trial.suggest_categorical('n_estimators', self.param_grid['n_estimators']),
                'max_depth': trial.suggest_int('max_depth', self.param_grid['max_depth'][0], self.param_grid['max_depth'][1]),
                'learning_rate': trial.suggest_categorical('learning_rate', self.param_grid['learning_rate']),
                'subsample': trial.suggest_float('subsample', self.param_grid['subsample'][0], self.param_grid['subsample'][1]),
                'colsample_bytree': trial.suggest_float('colsample_bytree', self.param_grid['colsample_bytree'][0], self.param_grid['colsample_bytree'][1]),
                'gamma': trial.suggest_float('gamma', self.param_grid['gamma'][0], self.param_grid['gamma'][1])
            }
            
            pipeline = Pipeline([
                ('xgb', xgb.XGBRegressor(
                    **params,
                    random_state=42,
                    eval_metric="rmse"
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
            ('xgb', xgb.XGBRegressor(
                **best_p,
                random_state=42,
                eval_metric="rmse"
            ))
        ], memory=None)
        self.model.fit(
            X_train, y_train,
            xgb__eval_set=[(X_train, y_train), (X_test, y_test)],
            xgb__verbose=False
        )
        
        self.X = X_test
        self.y = y_test
        
    def generate_algorithm_specific_plots(self) -> dict:
        plot_paths = {}
        xgb_model = self.model.named_steps['xgb'] if isinstance(self.model, Pipeline) else self.model
        
        plt.figure(figsize=(10, 6))
        xgb.plot_importance(xgb_model, importance_type='weight', max_num_features=15, title="XGBoost Regressor: Feature Importance (Frequency/Weight)")
        imp_weight_path = os.path.join(self.PLOT_DIR, "xgb_reg_feature_importance_weight.png")
        plt.savefig(imp_weight_path, bbox_inches='tight')
        plt.close()
        plot_paths["feature_importance_weight"] = imp_weight_path

        plt.figure(figsize=(10, 6))
        xgb.plot_importance(xgb_model, importance_type='gain', max_num_features=15, title="XGBoost Regressor: Feature Importance (Gain - Riduzione MSE)")
        imp_gain_path = os.path.join(self.PLOT_DIR, "xgb_reg_feature_importance_gain.png")
        plt.savefig(imp_gain_path, bbox_inches='tight')
        plt.close()
        plot_paths["feature_importance_gain"] = imp_gain_path
        
        plt.figure(figsize=(10, 6))
        xgb.plot_importance(xgb_model, importance_type='cover', max_num_features=15, title="XGBoost Regressor: Feature Importance (Cover)")
        imp_cover_path = os.path.join(self.PLOT_DIR, "xgb_reg_feature_importance_cover.png")
        plt.savefig(imp_cover_path, bbox_inches='tight')
        plt.close()
        plot_paths["feature_importance_cover"] = imp_cover_path

        try:
            _, ax = plt.subplots(figsize=(30, 15))
            xgb.plot_tree(xgb_model, num_trees=0, ax=ax)
            tree_path = os.path.join(self.PLOT_DIR, "xgb_reg_tree_0.png")
            plt.savefig(tree_path, bbox_inches='tight', dpi=300)
            plt.close()
            plot_paths["tree_visualization"] = tree_path
        except Exception as e:
            print(f"Impossibile generare la visualizzazione dell'albero. Assicurati che graphviz sia installato. Errore: {e}")

        print(f"Plot specifici XGBoost Regressione salvati in: {self.PLOT_DIR}")
        return plot_paths

    def SHAP_analysis(self, x_sample, dependence_variable):
        xgb_model = self.model.named_steps['xgb'] if isinstance(self.model, Pipeline) else self.model
        explainer = shap.TreeExplainer(xgb_model)
        shap_values = explainer(x_sample)
        print("\nSHAP values (TreeExplainer) calcolati con successo!")
        
        shap.summary_plot(shap_values, x_sample, show=False)
        summary_path = os.path.join(self.PLOT_DIR, "shap_summary_xgb_reg.png")
        plt.savefig(summary_path, bbox_inches='tight')
        plt.close()
        
        sample_ind = 0
        plt.figure(figsize=(10, 6))
        shap.plots.waterfall(shap_values[sample_ind], show=False)
            
        local_exp_path = os.path.join(self.PLOT_DIR, f"shap_local_explanation_sample_{sample_ind}_reg.png")
        plt.savefig(local_exp_path, bbox_inches='tight')
        plt.close()

        return {
            "shap_summary": summary_path,
            "local_explanation": local_exp_path
        }


if __name__ == "__main__":
    print("--- Test XGBoost Classification ---")
    default_dataset = "Student Placed-Not Placed Dataset"
    XGB_model_c = XGBoostC(dataset=default_dataset)
    dataset_path_c = data.DATASETS[default_dataset]["path"]
    drop_columns_c = data.DATASETS[default_dataset]["drop_columns"]
    objective_column_c = data.DATASETS[default_dataset]["objective_column"]

    XGB_model_c.import_data(dataset_path_c, drop_columns_c, objective_column_c)
    XGB_model_c.fit(XGB_model_c.X, XGB_model_c.y, None, None)
    XGB_model_c.calculate_metrics()
    XGB_model_c.generate_plots()
    XGB_model_c.generate_algorithm_specific_plots()
    XGB_model_c.export_results()

    print("\n--- Test XGBoost Regression ---")
    default_dataset = "Student Salary Dataset"
    XGB_model_r = XGBoostR(dataset=default_dataset)
    dataset_path_r = data.DATASETS[default_dataset]["path"]
    drop_columns_r = data.DATASETS[default_dataset]["drop_columns"]
    objective_column_r = data.DATASETS[default_dataset]["objective_column"]

    XGB_model_r.import_data(dataset_path_r, drop_columns_r, objective_column_r)
    XGB_model_r.fit(XGB_model_r.X, XGB_model_r.y, None, None)
    XGB_model_r.calculate_metrics()
    XGB_model_r.generate_plots()
    XGB_model_r.generate_algorithm_specific_plots()
    XGB_model_r.export_results()