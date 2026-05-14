from abc import ABC, abstractmethod
from baseMLAlgo import BaseMLAlgo

class ClassificationAlgo(BaseMLAlgo):
    @abstractmethod
    def __init__(self, model_name: str, dataset: str):
        self.model_name = model_name
        super().__init__(model_name=model_name, task_type="classification", dataset=dataset)

    def import_data(self, file_path: str, drop_columns: list):
        pass
    
    @abstractmethod
    def fit(self, X_train, y_train, X_test, y_test):
        pass

    def calculate_metrics(self) -> dict:
        pass
    
    def generate_plots(self) -> dict:
        pass
    
    def SHAP_analysis(self, X_sample):
        pass
    
    def export_results(self) -> dict:
        pass