import os
import pickle
import pandas as pd
import numpy as np

# lấy root project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# build path đúng
model_path = os.path.join(BASE_DIR, "models", "model.pkl")
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")
columns_path = os.path.join(BASE_DIR, "models", "columns.pkl")

print("Loading model from:", model_path)  # debug

# load
model = pickle.load(open(model_path, "rb"))
scaler = pickle.load(open(scaler_path, "rb"))
columns = pickle.load(open(columns_path, "rb"))


def predict_price(car_input):
    df = pd.DataFrame([car_input])

    # encode
    df = pd.get_dummies(df)

    # align columns
    df = df.reindex(columns=columns, fill_value=0)

    # scale
    df_scaled = scaler.transform(df)

    # predict log
    y_pred = model.predict(df_scaled)

    # convert price
    price = np.expm1(y_pred[0])

    return price