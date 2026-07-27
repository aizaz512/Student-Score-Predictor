import joblib

MODEL_PATH = "models/score_model.pkl"


def load_model():
    """
    Load the trained machine learning model.
    """

    model = joblib.load(MODEL_PATH)

    return model