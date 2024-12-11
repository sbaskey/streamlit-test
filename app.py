import requests
import io
from tensorflow.keras.models import load_model

# URL of the model on GitHub
MODEL_URL = "https://github.com/sbaskey/streamlit-test/blob/main/new_model.h5"

def load_keras_model_from_url(url):
    # Download the model file
    response = requests.get(url)
    if response.status_code == 200:
        # Load the model directly from the in-memory bytes
        model = load_model(io.BytesIO(response.content))
        return model
    else:
        raise Exception(f"Failed to download model. HTTP status: {response.status_code}")

# Load the model
model = load_keras_model_from_url(MODEL_URL)

# Use the model
print("Keras model loaded successfully!")
