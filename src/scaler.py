# src/scaling.py
from sklearn.preprocessing import RobustScaler


import joblib


def scale_features(X):

    scaler = RobustScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler


def save_scaler(scaler, path="models/scaler.pkl"):

    joblib.dump(scaler, path)


def load_scaler(path="models/scaler.pkl"):

    return joblib.load(path)