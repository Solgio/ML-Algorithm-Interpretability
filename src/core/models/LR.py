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
        x_train_scaled = self.scaler.fit_transform(X_train)
        x_test_scaled = self.scaler.transform(X_test)
        
        self.model = SklearnLinearRegression()
        self.model.fit(pd.DataFrame(x_train_scaled, columns=X_train.columns), y_train)
        
        self.X = pd.DataFrame(x_test_scaled, columns=X_test.columns)
        self.y = y_test
        
    def generate_algorithm_specific_plots(self) -> dict:
        import matplotlib.pyplot as plt
        import seaborn as sns
        import scipy.stats as stats
        import os
        
        plot_paths = {}
        y_pred = self.model.predict(self.X)
        residuals = self.y - y_pred

        plt.figure(figsize=(8, 6))
        plt.scatter(self.y, y_pred, alpha=0.6, edgecolors='k')
        plt.plot([self.y.min(), self.y.max()], [self.y.min(), self.y.max()], 'r--', lw=2)
        plt.xlabel('Valori Reali')
        plt.ylabel('Valori Predetti')
        plt.title('Actual vs Predicted')
        avp_path = os.path.join(self.PLOT_DIR, "actual_vs_predicted.png")
        plt.savefig(avp_path)
        plt.close()
        plot_paths["actual_vs_predicted"] = avp_path

        plt.figure(figsize=(8, 6))
        sns.residplot(x=y_pred, y=residuals, lowess=True, line_kws={'color': 'red'})
        plt.xlabel('Valori Predetti (Fitted)')
        plt.ylabel('Residui')
        plt.title('Residuals vs Fitted Values')
        rvf_path = os.path.join(self.PLOT_DIR, "residuals_vs_fitted.png")
        plt.savefig(rvf_path)
        plt.close()
        plot_paths["residuals_vs_fitted"] = rvf_path

        plt.figure(figsize=(8, 6))
        stats.probplot(residuals, dist="norm", plot=plt)
        plt.title('Q-Q Plot dei Residui')
        qq_path = os.path.join(self.PLOT_DIR, "qq_plot.png")
        plt.savefig(qq_path)
        plt.close()
        plot_paths["qq_plot"] = qq_path

        plt.figure(figsize=(10, 6))
        coefs = pd.Series(self.model.coef_, index=self.X.columns).sort_values()
        coefs.plot(kind='barh', color='teal')
        plt.title('Linear Regression: Valore dei Coefficienti')
        weight_path = os.path.join(self.PLOT_DIR, "weight_plot.png")
        plt.savefig(weight_path, bbox_inches='tight')
        plt.close()
        plot_paths["weight_plot"] = weight_path

        return plot_paths

if __name__ == "__main__":
    default_dataset = "Student Salary Dataset"
    lr_model = LinearRegression(default_dataset)
    dataset_path = data.DATASETS[default_dataset]["path"]
    drop_columns = data.DATASETS[default_dataset]["drop_columns"]
    objective_column = data.DATASETS[default_dataset]["objective_column"]

    lr_model.import_data(dataset_path, drop_columns, objective_column)
    lr_model.fit(lr_model.X, lr_model.y, None, None)
    lr_model.calculate_metrics()
    lr_model.generate_plots()
    lr_model.generate_algorithm_specific_plots()
    lr_model.export_results()