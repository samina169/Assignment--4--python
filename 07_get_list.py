import streamlit as st

# Title of the app
st.title("Get List of Items")

# Input for the user to enter items
items_input = st.text_input("Enter items separated by commas:")

# Button to display the list
if st.button("Display List"):
    # Split the input string into a list of items
    items = [item.strip() for item in items_input.split(",") if item.strip()]
    
    # Check if the list is not empty
    if items:
        st.write("The list of items is:")
        st.write(items)
    else:
        st.write("Please enter at least one item.")
