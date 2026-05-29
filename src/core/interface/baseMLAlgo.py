from abc import ABC, abstractmethod
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from infrastracture.data.Pipeline import DataPipeline
from infrastracture.data.dataLoader import CSVDataLoader
from infrastracture.data.dataProcessor import MissingDataStrategy, PandasDataProcessor
from infrastracture.data.dataSplitter import StratifiedDataSplitter, DataSplitConfig
from infrastracture.data.dataValidator import SchemaValidator

class BaseMLAlgo(ABC):
    """Abstract base class for machine learning algorithms."""
    
    def __init__(self, model_name: str, task_type: str, dataset: str, dataset_path: str, param_grid: dict):
        self.model_name = model_name
        self.task_type = task_type
        self.dataset = dataset
        self.dataset_path = dataset_path
        self.param_grid = param_grid or {}
        PROJECT_NAME="{}_{}_{}".format(model_name, task_type, dataset)
        self.PLOT_DIR = os.path.join("../output", PROJECT_NAME)
        os.makedirs(self.PLOT_DIR, exist_ok=True)
        self.data_pipeline = self._setup_data_pipeline()
        
    def _setup_data_pipeline(self):
        """Helper method to set up the data pipeline with default components."""
        loader = CSVDataLoader(self.dataset_path,encoding='utf-8')
        processor = PandasDataProcessor(
            missing_strategy=MissingDataStrategy.DROP,
            drop_first=True
        )
        validator = SchemaValidator(min_rows=10, min_columns=2)
        splitter = StratifiedDataSplitter( DataSplitConfig(test_size=0.2, random_state=42, stratify=True))
        return DataPipeline(loader, validator, processor, splitter)

    def import_data(self, drop_columns: list, objective_column: str,  test_size: float = 0.2, random_state: int = 42):
        """Updating the value for the data pipeline before running the complete pipeline."""
        if test_size !=0.2 or random_state != 42:
            split_config = DataSplitConfig(test_size=test_size, random_state=random_state, stratify=True)
            self.data_pipeline.splitter = StratifiedDataSplitter(split_config)
        X_train, X_test, y_train, y_test, X_full = self.data_pipeline.process(
            objective_column=objective_column,
            drop_columns=drop_columns,
            task_type=self.task_type
        )
        self.df = X_full
        self.X = X_test
        self.y = y_test
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
    