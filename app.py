import requests
import io
from tensorflow.keras.models import load_model
import pandas as pd

x=pd.read_csv('test.csv')
st.write(x)
