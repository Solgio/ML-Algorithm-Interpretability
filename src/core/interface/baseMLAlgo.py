from abc import ABC, abstractmethod
import os
import pandas as pd
from sklearn.model_selection import train_test_split

class BaseMLAlgo(ABC):
    
    def __init__(self, model_name: str, task_type: str, dataset: str):
        self.model_name = model_name
        self.task_type = task_type
        self.dataset = dataset
        PROJECT_NAME="{}_{}_{}".format(model_name, task_type, dataset)
        self.PLOT_DIR = os.path.join("../output", PROJECT_NAME)
        os.makedirs(self.PLOT_DIR, exist_ok=True)
        
    def import_data(self, dataset_path: str, drop_columns: list, objective_column: str,  test_size: float = 0.2, random_state: int = 42):
        self.df = pd.read_csv(dataset_path)
        self.df = self.df.dropna()
        y = self.df[objective_column]
        self.df = self.df.drop(columns=drop_columns)
        X = pd.get_dummies(self.df, drop_first=True).astype(float)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        
        return X_train, X_test, y_train, y_test
        
        
    @abstractmethod
    def fit(self, X_train, y_train, X_test, y_test):
        pass

    @abstractmethod
    def calculate_metrics(self) -> dict:
        pass
    
    @abstractmethod
    def generate_plots(self) -> dict:
        pass
    
    @abstractmethod
    def generate_algorithm_specific_plots(self) -> dict:
        pass
    
    @abstractmethod
    def SHAP_analysis(self, x_sample):
        pass
    
    @abstractmethod
    def export_results(self) -> dict:
        pass
    