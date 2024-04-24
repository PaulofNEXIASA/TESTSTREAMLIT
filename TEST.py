import streamlit as st
import pandas as pd
import numpy as np

pip install pipreqs



st.write("""
# My first app
Hello *world!*
""")
x = st.slider('x',  min_value=1, max_value=5000, value=15)  # 👈 this is a widget
df = [list(range(x)),list(range(x,-1, -1)),list(range(x))]


st.line_chart(df)
st.area_chart(df)
st.scatter_chart (df)
# st.altair_chart(df)
# st.map(df)

