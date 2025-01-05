import pandas as pd
import joblib
import os
from app.config import Paths


MODEL_DIR = Paths.get_path("MODEL_DIR")
ENCODER_DIR = Paths.get_path("ENCODERS_DIR")
RANDOM_FOREST_REGRESSOR = joblib.load(
    os.path.join(MODEL_DIR, "random_forest_regressor.joblib")
)
BINARY_ENCODER = joblib.load(os.path.join(ENCODER_DIR, "binary_encoder.joblib"))
STANDARD_SCALER = joblib.load(os.path.join(ENCODER_DIR, "standard_scaler.joblib"))


def get_prediction(df: pd.DataFrame):
    encoded_df = BINARY_ENCODER.transform(df)
    scaled_df = STANDARD_SCALER.transform(encoded_df)
    prediction = RANDOM_FOREST_REGRESSOR.predict(scaled_df)
    return enumerate(prediction, start=1)
