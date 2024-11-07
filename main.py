import streamlit as st
from sklearn.datasets import load_iris

st.write('Hello, My Friend')
st.write('Good Morning')
st.balloons()

data = load_iris(as_frame=True).frame
st.write(data.head())