from abc import ABC, abstractmethod
import pandas as pd
from typing import Optional, Tuple
import logging
from enum import Enum

class MissingDataStrategy(Enum):
    DROP = "drop"
    FILL_MEAN = "fill_mean"
    FILL_MEDIAN = "fill_median"
    FILL_MODE = "fill_mode"
    BACKWARD_FILL = "backward_fill"

class DataProcessor(ABC):
    """Abstract base class for data processing."""

    @abstractmethod
    def drop_columns(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """Drop specified columns from the DataFrame."""
        pass
    
    @abstractmethod
    def handle_missing_data(self, df: pd.DataFrame) -> pd.DataFrame:
        pass
    
    @abstractmethod
    def encode_categorical(self, df: pd.DataFrame)-> pd.DataFrame:
        pass

class PandasDataProcessor(DataProcessor):
    """Concrete implementation of DataProcessor using pandas."""
    
    def __init__(self, missing_strategy: MissingDataStrategy = MissingDataStrategy.DROP, categorical_columns: Optional[list] = None, drop_first: bool = True):
        self.missing_data_strategy = missing_strategy
        self.categorical_columns = categorical_columns
        self.drop_first = drop_first

    def drop_columns(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """Drop specified columns from the DataFrame.
            Raises exceptions if columns are not found."""
        invalid=set(columns) - set(df.columns)
        if invalid:
                logging.error(f"Error dropping columns, COLUMNS NOT FOUND: {invalid}")
                raise ValueError(f"Error dropping columns, COLUMNS NOT FOUND: {invalid}")
        logging.info(f"Dropping columns: {columns}")
        return df.drop(columns=columns)

    def handle_missing_data(self, df: pd.DataFrame, columns: Optional[list] = None) -> pd.DataFrame:
        """Handle missing data according to the specified strategy."""
        logging.info(f"Handling missing data using strategy: {self.missing_data_strategy.value}")
        if self.missing_data_strategy == MissingDataStrategy.DROP:
            logging.info("Dropping rows with missing data.")
            return df.dropna()
        
        elif self.missing_data_strategy == MissingDataStrategy.FILL_MEAN:
            logging.info("Filling missing data with mean values.")
            return df.fillna(df.mean())
        
        elif self.missing_data_strategy == MissingDataStrategy.FILL_MEDIAN:
            logging.info("Filling missing data with median values.")
            return df.fillna(df.median())
        
        elif self.missing_data_strategy == MissingDataStrategy.FILL_MODE:
            logging.info("Filling missing data with mode values.")
            return df.fillna(df.mode().iloc[0])
        
        elif self.missing_data_strategy == MissingDataStrategy.BACKWARD_FILL:
            logging.info("Filling missing data with backward fill.")
            return df.fillna(method='bfill')
        
        else:
            raise ValueError(f"Unsupported missing data strategy: {self.missing_data_strategy}")

    def encode_categorical(self, df: pd.DataFrame) -> pd.DataFrame:
        """Encode categorical variables using one-hot encoding."""
        if self.categorical_columns is None:
            self.categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
            
        if not self.categorical_columns:
            logging.info("No categorical columns specified, skipping encoding.")
            return df
        
        logging.info("Encoding categorical variables using one-hot encoding")
        return pd.get_dummies(df, columns=self.categorical_columns, drop_first=self.drop_first)