import streamlit as st

# Title of the app
st.title("Flowing with Data Structures")

# Input for the user to enter items
items_input = st.text_input("Enter items separated by commas:")

# Button to process the input
if st.button("Process Items"):
    # Split the input string into a list of items
    items = [item.strip() for item in items_input.split(",") if item.strip()]
    
    # Create a set from the list to remove duplicates
    items_set = set(items)
    
    # Create a dictionary with item counts
    items_count = {item: items.count(item) for item in items_set}
    
    # Display the results
    st.write("List of Items:", items)
    st.write("Set of Unique Items:", items_set)
    st.write("Item Counts:", items_count)
