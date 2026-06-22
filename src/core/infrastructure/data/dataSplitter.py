from abc import ABC, abstractmethod
from logging import config
import pandas as pd
from typing import Optional, Tuple
import logging
from enum import Enum
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataSplitConfig:
    test_size: float = 0.2
    random_state: int = 42
    stratify: bool = True
    
    def valildate(self)-> None:
        if not (0 < self.test_size < 1):
            raise ValueError(f"Invalid test_size: {self.test_size}. Must be between 0 and 1.")
        if not isinstance(self.random_state, int):
            raise ValueError(f"Invalid random_state: {self.random_state}. Must be an integer .")
        if self.random_state < 0:
            raise ValueError(f"Invalid random_state: {self.random_state}. Must be a non-negative integer.")

class DataSplitter(ABC):
    """Interface responsible for splitting the dataset into training and testing sets."""
    @abstractmethod
    def split(self, X: pd.DataFrame, y: pd.Series, task_type: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """Split the dataset into training and testing sets."""
        pass

class StratifiedDataSplitter(DataSplitter):
    """Class responsible for splitting the dataset into training and testing sets."""
    def __init__(self, config: DataSplitConfig):
        config.valildate()
        self.config = config
        logging.info(f"DataSplitter initialized with config: {self.config}")
        
    def split(self, X: pd.DataFrame, y: pd.Series, task_type: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """Split the dataset into training and testing sets."""
        stratify_param = y if (task_type == "classification" and self.config.stratify) else None
        logging.info(f"Splitting data with test_size={self.config.test_size}, random_state={self.config.random_state}, stratify={'enabled' if stratify_param is not None else 'disabled'}")
        return train_test_split(X, y, test_size=self.config.test_size, random_state=self.config.random_state, stratify=stratify_param)
