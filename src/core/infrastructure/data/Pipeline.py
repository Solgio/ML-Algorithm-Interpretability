import pandas as pd
from abc import ABC, abstractmethod
from typing import Tuple
import logging
from .dataLoader import DataLoader
from .dataValidator import DataValidator
from .dataProcessor import DataProcessor
from .dataSplitter import DataSplitter

class DataPipeline:
    """Class responsible for orchestrating the data loading, validation, processing, and splitting steps."""
    
    def __init__(self, loader: DataLoader, validator: DataValidator, processor: DataProcessor, splitter: DataSplitter):
        self.loader = loader
        self.validator = validator
        self.processor = processor
        self.splitter = splitter

    def process(self, objective_column: str, drop_columns: list=None, task_type: str="classification") -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """Run the preprocessing data pipeline and return the training and testing sets."""
        logging.info("Loading data...")
        df = self.loader.load_data()
        logging.info("Validating data...")
        self.validator.validate(df, objective_column)
        logging.info("Processing data...")
        if drop_columns:
            df = self.processor.drop_columns(df, drop_columns)
        df = self.processor.handle_missing_data(df)
        y = df[objective_column]
        if objective_column in df.columns:
            X = df.drop(columns=[objective_column])
        else:
            X = df
        X = self.processor.encode_categorical(X)
        logging.info("Splitting data...")
        X_train, X_test, y_train, y_test = self.splitter.split(X, y, task_type=task_type)
        logging.info("Data pipeline completed successfully.")
        return X_train, X_test, y_train, y_test, X