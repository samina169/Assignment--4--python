import streamlit as st

# Title of the app
st.title("Shorten List of Items")

# Input for the user to enter items
items_input = st.text_input("Enter items separated by commas:")

# Button to shorten the list
if st.button("Shorten List"):
    # Split the input string into a list of items
    items = [item.strip() for item in items_input.split(",") if item.strip()]
    
    # Check if the list is not empty
    if items:
        # Shorten the list to the first 5 items (or fewer if the list is shorter)
        shortened_list = items[:5]
        st.write("The shortened list of items is:")
        st.write(shortened_list)
    else:
        st.write("Please enter at least one item.")
