import pytest
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier

from src.core.infrastructure.explainers.base import Explainer
from src.core.infrastructure.explainers.strategy import ExplainerStrategy, select_explainer_strategy
from src.core.infrastructure.explainers.strategies.shap_kernel_explainer import SHAPKernelExplainer
from src.core.infrastructure.explainers.strategies.shap_tree_explainer import SHAPTreeExplainer
from src.core.infrastructure.explainers.adapter import SHAPAnalyzerAdapter

from src.core.domain.enums import Algorithm, TaskType


class TestExplainerStrategy:
    """Test strategy selection"""
    
    def test_tree_classification(self):
        s = select_explainer_strategy(Algorithm.XGBOOST_CLASSIFIER, TaskType.CLASSIFICATION)
        assert s == ExplainerStrategy.TREE
    
    def test_kernel_classification(self):
        s = select_explainer_strategy(Algorithm.SVM, TaskType.CLASSIFICATION)
        assert s == ExplainerStrategy.KERNEL
    
    def test_kernel_regression(self):
        s = select_explainer_strategy(Algorithm.LINEAR_REGRESSION, TaskType.REGRESSION)
        assert s == ExplainerStrategy.KERNEL
    
    def test_invalid_svm_regression(self):
        with pytest.raises(ValueError):
            select_explainer_strategy(Algorithm.SVM, TaskType.REGRESSION)


class TestSHAPAnalyzerAdapter:
    """Test adapter"""
    
    @pytest.fixture
    def classif_data(self):
        X = pd.DataFrame({'f1': np.random.default_rng(50).random(50), 'f2': np.random.default_rng(50).random(50)})
        y = (X['f1'] > 0.5).astype(int)
        return X, y
    
    @pytest.fixture
    def regr_data(self):
        X = pd.DataFrame({'f1': np.random.default_rng(50).random(50), 'f2': np.random.default_rng(50).random(50)})
        y = X['f1'] + X['f2'] + np.random.default_rng(50).random(50) * 0.1
        return X, y
    
    def test_classif_kernel(self, classif_data, tmp_path):
        X, y = classif_data
        model = SVC(kernel='rbf', probability=True)
        model.fit(X, y)
        
        adapter = SHAPAnalyzerAdapter(model, X, str(tmp_path), TaskType.CLASSIFICATION)
        result = adapter.explain(X.iloc[:10], 'f1')
        
        assert isinstance(result, dict)
        assert 'shap_summary' in result
    
    def test_regr_kernel(self, regr_data, tmp_path):
        X, y = regr_data
        model = LinearRegression()
        model.fit(X, y)
        
        adapter = SHAPAnalyzerAdapter(model, X, str(tmp_path), TaskType.REGRESSION)
        result = adapter.explain(X.iloc[:10], 'f1')
        
        assert isinstance(result, dict)
        assert 'shap_summary' in result
    
    def test_classif_tree(self, classif_data, tmp_path):
        X, y = classif_data
        model = DecisionTreeClassifier(max_depth=5, random_state=42)
        model.fit(X, y)
        
        adapter = SHAPAnalyzerAdapter(model, X, str(tmp_path), TaskType.CLASSIFICATION)
        result = adapter.explain(X.iloc[:10], 'f1')
        
        assert isinstance(result, dict)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])