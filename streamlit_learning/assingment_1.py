import streamlit as st

st.title("Favourite Language Picker App")
st.subheader("you can choose your favourite language")
st.text("Welcome to app")
st.write("choose your favourite language ")
language=st.selectbox("your favourite language is ",["Java","Python","C","C++","Assembly"])

st.success(f"your favourite language is {language}")