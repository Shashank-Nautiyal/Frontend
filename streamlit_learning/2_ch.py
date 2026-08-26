import streamlit as st

st.title("This is second ch")
st.subheader("we learn more thing")

select=st.selectbox("select from here",["option one","option two","option three"])
if select:
    st.success(f"you selected {select}")

if st.button("this is button "):
    st.write ("you pressed the button")

st.checkbox("you can make and check only one item ")
second_check=st.checkbox("for second one you need to make new checkbox")

if second_check:
    st.write("you check the second option")

radio_button=st.radio("same as select box but different theme",["this is first","second","third"])

st.write(f"you choose radio button  {radio_button}")

level=st.slider("here is an slider",0,10,5)

st.write(f"your level is :{level} ")

input_int=st.number_input("this is an number input",min_value=2,max_value=20,step=2)
st.write (f"your int input is {input_int}")

input_text= st.text_input("anything you want take form user side ")
if input_text:
    st.write(f"you write {input_text}")

dob=st.date_input("enter your dob ")
st.write(f"your dob is {dob}")