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
from sympy.printing.dot import dotprint
import graphviz

class SymbolicRegressor(BaseRegressionAlgo):
    def __init__(self, dataset: str, dataset_path: str, param_grid: dict = None):
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
            sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', str(col))
            sanitized = re.sub(r'_+', '_', sanitized)
            sanitized = sanitized.strip('_')
            new_columns.append(sanitized)
            
        df_clean = df.copy()
        df_clean.columns = new_columns
        return df_clean

    def fit(self, X_train, y_train, X_test, y_test):
        X_train = self._sanitize_column_names(X_train)
        X_test = self._sanitize_column_names(X_test)
        
        def objective(trial):
            params = {
                'niterations': trial.suggest_int('niterations', self.param_grid['niterations'][0], self.param_grid['niterations'][1]),
                'maxsize': trial.suggest_int('maxsize', self.param_grid['maxsize'][0], self.param_grid['maxsize'][1]),
                'parsimony': trial.suggest_float('parsimony', self.param_grid['parsimony'][0], self.param_grid['parsimony'][1], log=True)
            }
            
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
            
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                scores = cross_val_score(pipeline, X_train, y_train.values if hasattr(y_train, 'values') else y_train, 
                                         cv=3, scoring='neg_mean_squared_error', n_jobs=1)
                
            return scores.mean()

        print("Starting hyperparameter optimization with Optuna for Symbolic Regression (PySR)...")
        optuna.logging.set_verbosity(optuna.logging.WARNING)
        study = optuna.create_study(direction='maximize')
        
        study.optimize(objective, n_trials=10, show_progress_bar=True)
        print(f"Best parameters found by Optuna: {study.best_params}")
        best_p = study.best_params
        
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
        import matplotlib.pyplot as plt
        pysr_model = self.model.named_steps['pysr']
        df = pysr_model.equations_
        
        equation_path = os.path.join(self.PLOT_DIR, "pysr_equation.txt")
        with open(equation_path, "w") as f:
            f.write(str(df))
            
        pareto_path = os.path.join(self.PLOT_DIR, "pysr_pareto_front.png")
        plt.figure(figsize=(9, 5))
        plt.plot(df['complexity'], df['loss'], marker='o', linestyle='-', color='b', label='Pareto Frontier')
        
        try:
            best_idx = pysr_model.pick_best_index()
            chosen_row = df.iloc[best_idx]
            plt.scatter(chosen_row['complexity'], chosen_row['loss'], color='red', s=150, zorder=5, label='Chosen Model')
        except Exception:
            pass 
            
        plt.xlabel('Complexity (Number of Nodes)')
        plt.ylabel('Loss')
        plt.title('PySR Pareto Frontier: Complexity vs. Loss')
        plt.yscale('log')
        plt.grid(True, which="both", ls="--", alpha=0.5)
        plt.legend()
        plt.tight_layout()
        
        plt.savefig(pareto_path)
        plt.close()
        
        try:
            best_expr = pysr_model.sympy()
            dot_graph_data = dotprint(best_expr)
            tree_path = os.path.join(self.PLOT_DIR, "pysr_expression_tree")
            src = graphviz.Source(dot_graph_data)
            src.render(tree_path, format='png', cleanup=True)

            tree_png_path = f"{tree_path}.png"
        except Exception as e:
            print(f"Could not render equation tree: {e}")
            tree_png_path = None
        
        return {"pysr_equation": equation_path, "pysr_pareto_front": pareto_path, "pysr_expression_tree": tree_png_path}