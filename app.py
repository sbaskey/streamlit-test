import requests
import io
from tensorflow.keras.models import load_model
import pandas as pd
import streamlit as st
from sklearn.metrics import mean_squared_error


x=pd.read_csv('test.csv')
st.write(x)
model = load_model('new_model.h5',custom_objects={'mse': mean_squared_error})

