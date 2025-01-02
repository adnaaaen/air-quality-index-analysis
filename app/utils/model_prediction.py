import pandas as pd
import joblib
import os
from app.config import Paths


MODEL_DIR = Paths.get_path("MODEL_DIR")
ENCODER_DIR = Paths.get_path("ENCODERS_DIR")
LINEAR_MODEL = joblib.load(os.path.join(MODEL_DIR, "linear_regression_model.joblib"))
BINARY_ENCODER = joblib.load(os.path.join(ENCODER_DIR, "binary_encoder.joblib"))
STANDARD_SCALER = joblib.load(os.path.join(ENCODER_DIR, "standard_scaler.joblib"))


def get_prediction(df: pd.DataFrame):
    encoded_df = BINARY_ENCODER.transform(df)
    scaled_df = STANDARD_SCALER.transform(encoded_df)
    prediction = LINEAR_MODEL.predict(scaled_df)
    return prediction
