from interface.regressionAlgo import BaseRegressionAlgo
from sklearn.linear_model import LogisticRegression as SklearnLogisticRegression
import config.datasets_config as DATASET
        
class LogisticRegression(BaseRegressionAlgo):
    def __init__(self, dataset: str):
        super().__init__(model_name="Logistic Regression", dataset=dataset)

    def fit(self, X_train, y_train, X_test, y_test):
        self.model = SklearnLogisticRegression()
        self.model.fit(X_train, y_train)
        self.X = X_train
        self.y = y_train

if __name__ == "__main__":
    lr_model = SklearnLogisticRegression()
    dataset_path = "../dataset/placement_data.csv"
    drop_columns = DATASET["Student Placement Dataset"]["drop_columns"]
    objective_column = DATASET["Student Placement Dataset"]["objective_column"]
    
    lr_model.import_data(dataset_path, drop_columns, objective_column)
    
    