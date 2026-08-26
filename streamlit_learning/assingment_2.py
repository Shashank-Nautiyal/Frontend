import streamlit as st 
import datetime 

st.title("Age Calculator ")
st.subheader("you can calculate your age here ")

current_date=datetime.date.today()
st.write(f"Date : {current_date}")



dob=st.date_input("Enter your dob",min_value=datetime.date(2000, 1, 1),max_value=current_date)

Name=st.text_input("Enter your Name ")

age=(current_date-dob).days

if Name and dob :
    if st.button("Know your age"):
        st.write(f"{Name} your age is {age//365} years")



