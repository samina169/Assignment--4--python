import streamlit as st

# Title of the app
st.title("Erase Canvas")

# Create a placeholder for the canvas
canvas_placeholder = st.empty()

# Button to erase the canvas
if st.button("Erase Canvas"):
    # Clear the canvas by updating the placeholder
    canvas_placeholder.empty()
    st.write("The canvas has been erased.")
