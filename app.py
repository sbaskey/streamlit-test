import os
import requests
import streamlit as st
import pickle  # Example: Use the appropriate module for your model type

# URL of the model on GitHub
MODEL_URL = "https://github.com/sbaskey/Crop_Yield/blob/master/dnn/new_model.h5>"

@st.cache_resource
def download_and_load_model():
    response = requests.get(MODEL_URL)
    if response.status_code == 200:
        with open("model.pkl", "wb") as f:
            f.write(response.content)
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)  # Use appropriate loader for your model
        return model
    else:
        st.error("Failed to download the model.")
        return None

# Load the model
model = download_and_load_model()

# Use the model in your app
if model:
    st.write("Model loaded successfully!")
    # Add your app logic here
