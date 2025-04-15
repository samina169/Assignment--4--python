import streamlit as st

# Title of the app
st.title("Double the List of Numbers")

# Input for the user to enter numbers
numbers_input = st.text_input("Enter numbers separated by commas:")

# Button to double the numbers
if st.button("Double Numbers"):
    # Split the input string into a list of numbers
    numbers = [float(num) for num in numbers_input.split(",") if num.strip()]
    doubled_numbers = [num * 2 for num in numbers]
    st.write(f"The doubled numbers are: {doubled_numbers}")
