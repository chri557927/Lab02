# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Graphs",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title("Studying Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
# 2. Load the data from 'data.json' into a Python dictionary.
#    - Use a 'try-except' block here as well.

current_dir = os.path.dirname(__file__)
csv_file = os.path.join(current_dir, "data.csv")
df = pd.read_csv(csv_file)

if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    st.dataframe(df)
else:
    st.error("CSV file not found.")
    df = pd.DataFrame()

st.divider()

# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Graph 1: Weekly Study Hours") # CHANGE THIS TO THE TITLE OF YOUR GRAPH

st.write("This static bar chart shows the number of hours studied each day, using data from the CSV file.")

st.bar_chart(df.set_index("Day")["Hours Studied"])


# GRAPH 2: DYNAMIC GRAPH
st.subheader("Graph 2: Filtered Study Hours by Day")  # CHANGE THIS TO THE TITLE OF YOUR GRAPH

st.write("Use the selector below to view study hours for specific days. This graph is dynamic and updates automatically.")

day_options = df["Day"].dropna().unique().tolist() if "Day" in df.columns else []
default_days = [d for d in ["Mon", "Tue", "Wed"] if d in day_options]

selected_days = st.multiselect(
    "Select days to view:",
    options=day_options,
    default=default_days
)

filtered_df = df[df["Day"].isin(selected_days)]

st.line_chart(filtered_df.set_index("Day")["Hours Studied"])#NEW

if "selected_days" not in st.session_state:
    st.session_state.selected_days = selected_days
else:
    st.session_state.selected_days = selected_days


# GRAPH 3: DYNAMIC GRAPH
json_file = os.path.join(current_dir, "data.json")

if os.path.exists(json_file):
    try:
        with open(json_file, "r") as f:
            json_data = json.load(f)
    except json.JSONDecodeError:
        st.error("Error: JSON file is not valid JSON.")
        json_data = {"data_points": []}
else:
    st.error("JSON file not found.")
    json_data = {"data_points": []}

if "data_points" in json_data and json_data["data_points"]:
    json_df = pd.DataFrame(json_data["data_points"])

    #slider
    scale = st.slider("Adjust scale of values", 1, 3, 1)
    json_df["Scaled Value"] = json_df["value"] * scale

    #bar chart
    st.bar_chart(json_df.set_index("label")["Scaled Value"])

    st.caption("Use the slider to adjust how the values are scaled. This demonstrates dynamic graphing with JSON data.")
else:
    st.warning("No data points found in JSON file.")
