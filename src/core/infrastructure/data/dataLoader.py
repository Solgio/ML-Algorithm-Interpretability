from abc import ABC, abstractmethod
import pandas as pd
from typing import Tuple
import logging

class DataLoader(ABC):
    """Abstract base class for data loading."""
 
    @abstractmethod
    def load_data(self)-> pd.DataFrame:
        """Load the dataset into a DataFrame.
           Raises exceptions if loading fails or if the dataset is invalid."""
        pass

class DataError(Exception):
    """Custom exception for data loading errors."""
    pass
    
class CSVDataLoader(DataLoader):
    """Concrete implementation of DataLoader for CSV files."""
    
    def __init__(self, file_path: str, encoding: str = 'utf-8', **csv_kwargs):
        self.file_path = file_path
        self.encoding = encoding
        self.csv_kwargs = csv_kwargs

    def load_data(self) -> pd.DataFrame:
        """Load the dataset from a CSV file.
        Raises DataError with specific messages for different failure scenarios."""
        try:
            logging.info(f"Loading CSV file: {self.file_path}")
            df = pd.read_csv(self.file_path, encoding=self.encoding, **self.csv_kwargs)
            logging.info(f"CSV file loaded successfully: {self.file_path} (shape: {df.shape})")
            return df
            
        except FileNotFoundError as e:
            logging.exception(f"Error loading CSV file, FILE NOT FOUND: {e}")
            raise DataError(f"Error loading CSV file, FILE NOT FOUND: {e}")
        
        except pd.errors.EmptyDataError as e:
            logging.exception(f"Error loading CSV file, EMPTY DATA: {e}")
            raise DataError(f"Error loading CSV file, EMPTY DATA: {e}")
        
        except pd.errors.ParserError as e:
            logging.exception(f"Error loading CSV file, PARSING ERROR: {e}")
            raise DataError(f"Error loading CSV file, PARSING ERROR: {e}")
        
        except Exception as e:
            logging.exception(f"Error loading CSV file, UNKNOWN ERROR: {e}")
            raise DataError(f"Error loading CSV file, UNKNOWN ERROR: {e}")