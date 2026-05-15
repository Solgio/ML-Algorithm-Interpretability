import pandas as pd
import config.datasets_config as data
from sklearn.preprocessing import StandardScaler
from interface.regressionAlgo import BaseRegressionAlgo
from sklearn.linear_model import LinearRegression as SklearnLinearRegression
        
class LinearRegression(BaseRegressionAlgo):
    def __init__(self, dataset: str):
        super().__init__(model_name="Linear Regression", dataset=dataset)
        self.scaler = StandardScaler()

    def fit(self, X_train, y_train, X_test, y_test):
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        self.X = pd.DataFrame(X_train_scaled, columns=X_train.columns)
        self.y = y_train
        
        self.model = SklearnLinearRegression()
        self.model.fit(self.X, self.y)
        
    def generate_algorithm_specific_plots(self) -> dict:
        return {}

if __name__ == "__main__":
    lr_model = LinearRegression("Student Salary Dataset")
    dataset_path = data.DATASETS["Student Salary Dataset"]["path"]
    drop_columns = data.DATASETS["Student Salary Dataset"]["drop_columns"]
    objective_column = data.DATASETS["Student Salary Dataset"]["objective_column"]
    
    lr_model.import_data(dataset_path, drop_columns, objective_column)    