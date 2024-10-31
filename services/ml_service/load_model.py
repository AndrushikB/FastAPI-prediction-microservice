
from sklearn.linear_model import Lasso
import joblib


def load_flats_model(model_path: str):
    """Загружаем обученную модель оттока.
    Args:
        model_path (str): Путь до модели.
    """
    
    try:
        model = joblib.load(model_path)
        print("Model loaded successfully")
    except Exception as e:
        print(f"Failed to load model: {e}")
    return model

if __name__ == "__main__":
    model = load_flats_model(model_path='../models/model.pkl')
    
    print(f"Model parameter names: {model.feature_names_in_}")