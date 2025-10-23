# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import csv
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Study survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title(" Weekly Study Hours Tracker")
st.write("Enter how many hours you studied each day of the week:")

# Days of the week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Dictionary to store input
study_hours = {}

# Create numeric input boxes for each day
for day in days:
    study_hours[day] = st.number_input(f"{day} hours studied", min_value=0.0, max_value=24.0, step=0.5)

# Button to save data
if st.button("Save Data"):
    filename = "data.csv"
    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Day", "Hours Studied"])
        for day, hours in study_hours.items():
            writer.writerow([day, hours])

    st.success("Your study data has been saved.")
