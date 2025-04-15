import streamlit as st

# Title of the app
st.title("Get First Element from a List")

# Input for the user to enter items
items_input = st.text_input("Enter items separated by commas:")

# Button to get the first element
if st.button("Get First Element"):
    # Split the input string into a list of items
    items = [item.strip() for item in items_input.split(",") if item.strip()]
    
    # Check if the list is not empty
    if items:
        first_element = items[0]
        st.write(f"The first element is: {first_element}")
    else:
        st.write("Please enter at least one item.")
