from abc import ABC, abstractmethod
import pandas as pd
from typing import Optional
import logging

class DataValidator(ABC):
    """Abstract base class for data validation."""

    @abstractmethod
    def validate(self, df: pd.DataFrame, objective_column: Optional[str] = None) -> bool:
        """Validate the dataset and return a tuple of (is_valid, error_message).
           is_valid is True if the dataset is valid, False otherwise."""
        pass
    
class SchemaValidator(DataValidator):
    """Concrete implementation of DataValidator that checks for required columns and data types."""
    def __init__(self, min_rows: int= 10, min_columns: int = 1):
        self.min_rows = min_rows
        self.min_columns = min_columns

    def validate(self, df: pd.DataFrame, objective_column: Optional[str] = None) -> bool:
        """Validate the dataset by checking for required columns and data types.
           Returns a tuple of (is_valid, error_message)."""
        if df.shape[0] < self.min_rows:
            raise ValueError(f"Validation failed, NOT ENOUGH ROWS: Found {df.shape[0]}, expected at least {self.min_rows}")
        
        if df.shape[1] < self.min_columns:
            raise ValueError(f"Validation failed, NOT ENOUGH COLUMNS: Found {df.shape[1]}, expected at least {self.min_columns}")
        
        if objective_column and objective_column not in df.columns:
                raise ValueError(f"Validation failed, OBJECTIVE COLUMN NOT FOUND: '{objective_column}' not in dataset columns.")
            
        if objective_column and df[objective_column].isnull().all():
                raise ValueError(f"Validation failed, OBJECTIVE COLUMN ALL NULL: '{objective_column}' contains only null values.")
            
        logging.info("Dataset validation successful.")
        return True