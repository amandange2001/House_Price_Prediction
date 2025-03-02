import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
import joblib


data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["Target"] = data.target


X = df[['MedInc', 'HouseAge', 'AveRooms', 'AveOccup']]
y = df["Target"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


project_dir = os.path.dirname(os.path.abspath(__file__))  
model_dir = os.path.join(project_dir, 'models')  


os.makedirs(model_dir, exist_ok=True)


model_path = os.path.join(model_dir, 'house_price_model.pkl')
joblib.dump(model, model_path)

print(f"Model training complete. Saved as '{model_path}'.")
