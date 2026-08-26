import streamlit as st
import pandas as pd 

st.title("Chai Sales dashboard ")
file=st.file_uploader("Uplaod your file here",type=["csv"])

if file:
    df=pd.read_csv("chai_sales.csv")

    st.subheader("Data preview")
    st.dataframe(df)

if file:
    st.write(df.describe())

if file:
    cities=df["City"].unique()
    selected_city=st.selectbox("select the city",cities)
    fileterd_data=df[df["City"]==selected_city]
    st.dataframe(fileterd_data)