import streamlit as st
import numpy as np
import pandas as pd


st.write("TThis is my first streamlit app!")
st.title("Welcome to my Streamlit App")
st.header("This is a header")
st.subheader("This is a subheader")

st.sidebar.title("Sidebar Title")
st.sidebar.header("Sidebar Header") 

st.text("This is a text")
st.image("chart_t1.png")
st.checkbox("Done!")

st.radio("Pick one", ["Option 1", "Option 2"])

df = pd.DataFrame(np.random.randn(100, 2), columns=["Product A", "Product B"])
print(df)
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.video("https://www.youtube.com/watch?v=9bZkp7q19f0")