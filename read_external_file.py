import pandas as pd
import streamlit as st

from pyodide.http import open_url

url = "https://raw.githubusercontent.com/franciscobmacedo/testing-stlite/main/a1_cin_assessments_episodes_referrals_2013_to_2022.csv"

data = open_url(url)

df = pd.read_csv(data)


st.write('hello')
st.write(df)