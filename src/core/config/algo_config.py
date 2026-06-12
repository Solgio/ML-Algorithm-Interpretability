ALGORITHMS = {
    "Regression": {
        "Linear Regression": {
            "module": "models.LR",
            "class": "LinearRegression",
            "description": "OLS Linear Regression (sklearn)",
            "prompt": "This model has very high intrinsic transparency and its parameters are directly interpretable. Explain the impact (magnitude) and direction (positive or negative sign) of the main coefficients. Describe how a unit increase in a factor causes a proportional change in the final prediction, but warn that these are correlations and not absolute causal laws.",
        },
        "Decision tree":{
            "module": "models.DecTree",
            "class": "DecisionTreeR",
            "description": "Decision Tree (sklearn)",
            "prompt": "This model has high local traceability based on structural explainability. Explain the decisions as a sequence of 'if... then' logical rules (decision path) that faithfully reflect human reasoning. Use global feature importance to highlight the fundamental filtering criterion at the top of the tree.",
            "param_grid": {
            'criterion': ['squared_error', 'absolute_error', 'friedman_mse', 'poisson'],
            'max_depth': [None, 5, 20],
            'min_samples_split': [2, 10],
            'min_samples_leaf': [1, 4],
            'ccp_alpha': [0.0, 0.1]
        }
        },
        "Random Forest":{
            "module": "models.RandForest",
            "class": "RandomForestR",
            "description": "Random Forest (sklearn)",
            "prompt": "This model is an 'Ensemble' with medium transparency, requiring the use of feature importance (post-hoc explainability) to be understood. Explain that the algorithm creates many parallel scenarios and makes a majority decision. The main factors identified represent the arguments that convinced the majority, compensating for any individual errors.",
            "param_grid": {
            'n_estimators': [100, 200],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 10],
            'min_samples_leaf': [1, 4],
            'max_features': ['sqrt', 'log2'],
            'ccp_alpha': [0.0, 0.1],
            'criterion': ['squared_error', 'absolute_error', 'friedman_mse', 'poisson'],
            'min_impurity_decrease': [0.0, 0.1]
        }
        },
        "XGBoost":{
            "module": "models.XGBoost",
            "class": "XGBoostR",
            "description": "XGBRegressor (xgboost)",
            "prompt": "This model has low intrinsic transparency (opaque model) and relies on post-hoc explanations. Explain that the algorithm proceeds through successive steps, progressively focusing on the most difficult cases. Use feature importance to illustrate which variables were most useful in correcting errors during this learning process.",
            "param_grid": {
            'n_estimators': [100, 300],
            'max_depth': [3, 10],
            'learning_rate': [0.01, 0.2],
            'subsample': [0.8, 1.0],
            'colsample_bytree': [0.6, 1.0],
            'gamma': [0, 0.2]
            }
        },
    },
    "Classification": {
        "Logistic Regression": {
            "module": "models.LogR",
            "class": "LogisticRegression",
            "description": "Logistic Regression (sklearn)",
            "prompt": "This model offers probabilistic explainability. Do not talk about logarithms, but explain how an increase in a specific variable multiplies the probabilities (odds ratio) of an event occurring. Comment on the model's certainty, noting that probabilities very close to 0 or 100 indicate high confidence.",
            },
        "SVM":{
            "module": "models.SVM",
            "class": "SVM",
            "description": "Support Vector Machine (sklearn.svm.SVC)",
            "prompt": "This is an opaque model with low transparency. Explain that the algorithm ignores obvious cases and seeks the optimal dividing line by focusing only on borderline instances, i.e., those that are most ambiguous (the support vectors). Use the most important features to explain which 'coordinates' define this critical boundary.",
            "param_grid": {
              'C': [0.1, 1, 10, 100],   
              'gamma':['scale', 'auto', 0.1, 0.01, 0.001, 0.0001],
              'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],
              'class_weight': [None, 'balanced'],
              'degree': [2, 4]
              }
        },
        "Decision tree":{
            "module": "models.DecTree",
            "class": "DecisionTreeC",
            "description": "Decision Tree (sklearn)",
            "prompt": "This model has high local traceability based on structural explainability. Explain the decisions as a sequence of 'if... then' logical rules (decision path) that faithfully reflect human reasoning. Use global feature importance to highlight the fundamental filtering criterion at the top of the tree.",
            "param_grid": {
            'criterion': ['gini', 'entropy'],
            'max_depth': [None, 5, 20],
            'min_samples_split': [2, 10],
            'min_samples_leaf': [1, 4],
            'ccp_alpha': [0.0, 0.1]
        }
        },
        "Random Forest":{
            "module": "models.RandForest",
            "class": "RandomForestC",
            "description": "Random Forest (sklearn)",
            "prompt": "This model is an 'Ensemble' with medium transparency, requiring the use of feature importance (post-hoc explainability) to be understood. Explain that the algorithm creates many parallel scenarios and makes a majority decision. The main factors identified represent the arguments that convinced the majority, compensating for any individual errors.",
            "param_grid": {
            'n_estimators': [100, 200],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 10],
            'min_samples_leaf': [1, 4],
            'max_features': ['sqrt', 'log2'],
            'ccp_alpha': [0.0, 0.1],
            'criterion': ['gini', 'entropy', 'log_loss'],
            'min_impurity_decrease': [0.0, 0.1]
        }
        },
        "XGBoost":{
            "module": "models.XGBoost",
            "class": "XGBoostC",
            "description": "XGBClassifier (xgboost)",
            "prompt": "This model has low intrinsic transparency (opaque model) and relies on post-hoc explanations. Explain that the algorithm proceeds through successive steps, progressively focusing on the most difficult cases. Use feature importance to illustrate which variables were most useful in correcting errors during this learning process.",
            "param_grid": {
            'n_estimators': [100, 300],
            'max_depth': [3, 10],
            'learning_rate': [0.01, 0.2],
            'subsample': [0.8, 1.0],
            'colsample_bytree': [0.6, 1.0],
            'gamma': [0, 0.2],
        }
        },
    },
}