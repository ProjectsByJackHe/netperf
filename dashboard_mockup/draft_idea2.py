import streamlit as st
import pandas as pd
import numpy as np

st.title("Draft Idea #2")

chart_data = pd.DataFrame(
   {
       "column1": list(range(20)) * 3,
       "column2": np.random.randn(60),
       "column3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
   }
)

st.bar_chart(chart_data, x="col1", y="col2", color="col3")
