import os
import re
import pandas as pd
import optuna
import warnings
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from pysr import PySRRegressor
from src.core.interface.regressionAlgo import BaseRegressionAlgo

class SymbolicRegressor(BaseRegressionAlgo):
    def __init__(self, dataset: str, dataset_path: str, param_grid: dict = None):
        # Default parameter grid for PySR if none is provided
        if param_grid is None:
            param_grid = {
                'niterations': [5, 40],
                'maxsize': [10, 30],
                'parsimony': [0.0001, 0.05]
            }
        super().__init__(model_name="SymbolicRegressor", dataset=dataset, dataset_path=dataset_path, param_grid=param_grid)
        
    def _sanitize_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        PySR variables must be strictly alphanumeric or underscores.
        This safely replaces hyphens, spaces, and other symbols.
        """
        if not isinstance(df, pd.DataFrame):
            return df
        
        new_columns = []
        for col in df.columns:
            # Replace any non-alphanumeric character (except existing underscores) with an underscore
            sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', str(col))
            # Collapse consecutive underscores into a single one for neatness
            sanitized = re.sub(r'_+', '_', sanitized)
            # Drop any trailing or leading underscores
            sanitized = sanitized.strip('_')
            new_columns.append(sanitized)
            
        df_clean = df.copy()
        df_clean.columns = new_columns
        return df_clean

    def fit(self, X_train, y_train, X_test, y_test):
        # SANITIZATION: Fix column names right before training to comply with PySR rules
        X_train = self._sanitize_column_names(X_train)
        X_test = self._sanitize_column_names(X_test)
        
        def objective(trial):
            # 1. Suggest parameters
            params = {
                'niterations': trial.suggest_int('niterations', self.param_grid['niterations'][0], self.param_grid['niterations'][1]),
                'maxsize': trial.suggest_int('maxsize', self.param_grid['maxsize'][0], self.param_grid['maxsize'][1]),
                'parsimony': trial.suggest_float('parsimony', self.param_grid['parsimony'][0], self.param_grid['parsimony'][1], log=True)
            }
            
            # 2. Build the Pipeline (Scaling + PySR)
            scaler = StandardScaler().set_output(transform="pandas") if hasattr(StandardScaler, "set_output") else StandardScaler()
            
            pipeline = Pipeline([
                ('scaler', scaler),
                ('pysr', PySRRegressor(
                    **params,
                    binary_operators=["+", "*", "-", "/"],
                    unary_operators=["sin", "cos", "exp"],
                    temp_equation_file=True,
                    verbosity=0,             
                    random_state=42
                ))
            ], memory=None)
            
            # 3. Cross-Validation
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                scores = cross_val_score(pipeline, X_train, y_train.values if hasattr(y_train, 'values') else y_train, 
                                         cv=3, scoring='neg_mean_squared_error', n_jobs=1)
                
            return scores.mean()

        print("Inizio ottimizzazione iperparametri con Optuna per Symbolic Regression (PySR)...")
        optuna.logging.set_verbosity(optuna.logging.WARNING)
        study = optuna.create_study(direction='maximize')
        
        # PySR is computationally heavy, keep n_trials lower
        study.optimize(objective, n_trials=10, show_progress_bar=True)
        print(f"Migliori parametri individuati da Optuna: {study.best_params}")
        best_p = study.best_params
        
        # 4. Final Pipeline Model construction
        final_scaler = StandardScaler().set_output(transform="pandas") if hasattr(StandardScaler, "set_output") else StandardScaler()
        
        self.model = Pipeline([
            ('scaler', final_scaler),
            ('pysr', PySRRegressor(
                **best_p,
                binary_operators=["+", "*", "-", "/"],
                unary_operators=["sin", "cos", "exp"],
                temp_equation_file=True,
                random_state=42
            ))
        ], memory=None)
        
        print("Training final PySR Pipeline...")
        self.model.fit(X_train, y_train.values if hasattr(y_train, 'values') else y_train)
        
        self.X = X_test
        self.y = y_test
        
    def predict(self, X_train=None, y_train=None, X_test=None, y_test=None):
        return self.model.predict(self.X)
    
    def generate_algorithm_specific_plots(self) -> dict:
        # PySR does not have built-in feature importance, but we can visualize the discovered equations
        equation_path = os.path.join(self.PLOT_DIR, "pysr_equation.txt")
        with open(equation_path, "w") as f:
            f.write(str(self.model.named_steps['pysr'].equations_))
        
        return {"pysr_equation": equation_path}