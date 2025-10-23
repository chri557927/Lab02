# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st
import os

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="📚",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE
st.title("Web Development Lab02")

st.subheader("CS 1301")
st.subheader("Web Development - Section E")
st.subheader("Chris Hernandez")

# INTRODUCTORY TEXT
st.write("""

Welcome to my Lab02 Studying app!

On the left we have our main pages:

1. Study survey- Enter the number of hours you study each week.

2. Graphs- Graphs based on the survey
""")

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "GT_Library.jpeg")

st.image(image_path)
