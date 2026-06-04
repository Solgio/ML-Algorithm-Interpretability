from abc import ABC, abstractmethod
import os
from typing import Dict, Optional
import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from src.core.domain.enums import TaskType
from src.core.infrastructure.explainers.adapter import SHAPAnalyzerAdapter
from src.core.infrastructure.explainers.service import ExplainerService
from src.core.infrastructure.data.Pipeline import DataPipeline
from src.core.infrastructure.data.dataLoader import CSVDataLoader
from src.core.infrastructure.data.dataProcessor import MissingDataStrategy, PandasDataProcessor
from src.core.infrastructure.data.dataSplitter import StratifiedDataSplitter, DataSplitConfig
from src.core.infrastructure.data.dataValidator import SchemaValidator

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
    
    def explain_with_shap(self, x_sample: pd.DataFrame, 
                     dependence_variable: str) -> Dict[str, str]:
        """Execute SHAP analysis """
        logging.info("Inizio SHAP analysis...")
    
        try:
            task_type = self._get_task_type()
            logging.info(f"Task type: {task_type.value}")
            
            adapter = SHAPAnalyzerAdapter(
                model=self.model,
                x_train=self.X,
                plot_dir=self.PLOT_DIR,
                task_type=task_type
            )
            
            plot_paths = adapter.explain(x_sample, dependence_variable)
            logging.info(f"✓ SHAP completato. Plot: {list(plot_paths.keys())}")
            return plot_paths
            
        except Exception as e:
            logging.exception(f"Errore SHAP: {e}")
            return {}

    def _get_task_type(self) -> TaskType:
        """Determina il task type della classe"""
        base_class_names = [cls.__name__ for cls in self.__class__.__mro__]

        if 'BaseClassificationAlgo' in base_class_names:
            return TaskType.CLASSIFICATION
        elif 'BaseRegressionAlgo' in base_class_names:
            return TaskType.REGRESSION

        logging.warning("Task type indeterminato, uso CLASSIFICATION")
        return TaskType.CLASSIFICATION

    @abstractmethod
    def export_results(self) -> dict:
        pass
    