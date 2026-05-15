import os
import sklearn.svm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import config.datasets_config as data
from sklearn.preprocessing import StandardScaler
from interface.classificationAlgo import BaseClassificationAlgo
        
class SVM(BaseClassificationAlgo):
    def __init__(self, dataset: str):
        super().__init__(model_name="SVM", dataset=dataset)
        self.scaler = StandardScaler()

    def fit(self, X_train, y_train, X_test, y_test):
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        self.model = sklearn.svm.SVC(kernel='rbf', C=1.0, gamma='scale')
        self.model.fit(pd.DataFrame(X_train_scaled, columns=X_train.columns), y_train)
        
        self.X = pd.DataFrame(X_test_scaled, columns=X_test.columns)
        self.y = y_test
    
    def generate_algorithm_specific_plots(self) -> dict:
        decision_function = self.model.decision_function(self.X)
        plt.figure(figsize=(10, 6))
        plt.savefig(os.path.join(self.PLOT_DIR, "svm_decision_function.png"))
        plt.close()
        return {
            "svm_decision_function": os.path.join(self.PLOT_DIR, "svm_decision_function.png")
        }

if __name__ == "__main__":
    lr_model = SVM(dataset="Student Placed-Not Placed Dataset")
    dataset_path = data.DATASETS["Student Placed-Not Placed Dataset"]["path"]
    drop_columns = data.DATASETS["Student Placed-Not Placed Dataset"]["drop_columns"]
    objective_column = data.DATASETS["Student Placed-Not Placed Dataset"]["objective_column"]

    lr_model.import_data(dataset_path, drop_columns, objective_column)