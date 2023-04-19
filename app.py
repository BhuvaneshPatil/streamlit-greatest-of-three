import streamlit as st

st.title("Find the largest among three given numbers")

number1 = st.number_input("Enter the first number:")
number2 = st.number_input("Enter the second number:")
number3 = st.number_input("Enter the third number:")

if st.button("Find the largest number"):
    largest_number = max(number1, number2, number3)
    st.success("The largest number is: {}".format(largest_number))
