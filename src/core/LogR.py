import os
import shap
import sklearn
import pandas as pd
import kagglehub as kh

dataset_dir = kh.dataset_download("darkmatternet/nasa-near-earth-asteroids-and-close-approaches")

file_path = os.path.join(dataset_dir, "near_earth_asteroids_2025 (1).csv")

df = pd.read_csv(file_path)

print("Dataset loaded successfully from:\n", file_path)

df_placed = df[df['placed'] == 1].copy()

y = df_placed['pha']
X = df_placed.drop(columns=['pha', 'placed'])

X = pd.get_dummies(X, drop_first=True)

model = sklearn.linear_model.LogisticRegression()
model.fit(X, y)

print("Model coefficients:\n")
for i in range(X.shape[1]):
    print(f"{X.columns[i]} = {model.coef_[i]:.5f}")