import pandas as pd
import streamlit as st

from pyodide.http import open_url

data = open_url("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv")

df = pd.read_csv(data)


st.write('hello')
st.write(df)