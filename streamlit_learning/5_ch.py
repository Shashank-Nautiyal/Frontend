import streamlit as st 
import requests


st.title("Live currency conversion")
amount=st.number_input("Enter the amount",min_value=1)

target_currency=st.selectbox("Select the target currency",["USD","JPY","EUR","JBP"])

if st.button("Convert"):
    url="https://api.exchangerate-api.com/v4/latest/INR"
    response=requests.get(url)

    if response.status_code==200:
        data=response.json()
        rate=data["rates"][target_currency]
        converted_value=rate*amount
        st.success(f"{amount}INR = {converted_value:.2f}{target_currency}")
    else:
        st.write("Cant get the conversion rate")
