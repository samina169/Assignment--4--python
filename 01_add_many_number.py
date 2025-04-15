import streamlit as st

# Title of the app
st.title("Add Many Numbers")

# Input for the user to enter numbers
numbers_input = st.text_input("Enter numbers separated by commas:")

# Button to calculate the sum
if st.button("Calculate Sum"):
    # Split the input string into a list of numbers
    numbers = [float(num) for num in numbers_input.split(",") if num.strip()]
    total = sum(numbers)
    st.write(f"The sum of the numbers is: {total}")
