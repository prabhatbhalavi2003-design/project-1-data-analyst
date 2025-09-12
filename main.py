import streamlit as st
from src.data_loader import data_load
from src.dashboard import create_dashboard

# Load data
df = data_load("research/raw.csv")

# Set page config
st.set_page_config(
    page_title="Student Performance Analysis", page_icon="analysis.png", layout="wide")

# Main title
st.title("📊 Student Performance Analysis Dashboard")

# Create tabs
tab1, tab2 = st.tabs(["📋 Data Overview", "📊 Analytics Dashboard"])

# Tab 1: Data Overview (Dataframe)
with tab1:
    st.header("📋 Student Performance Data")
    st.write(
        "Explore the raw data below. You can sort, filter, and search through the student performance records."
    )

    # Add some basic stats at the top
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Students", len(df))
    col2.metric("Average Math Score", round(df['math_score'].mean()))
    col3.metric("Average Reading Score", round(df['reading_score'].mean()))
    col4.metric("Average Writing Score", round(df['writing_score'].mean()))

    # Display the dataframe
    st.subheader("📊 Data Table")
    st.dataframe(df)

# Tab 2: Analytics Dashboard
with tab2:
    st.header("📊 Analytics Dashboard")
    st.write("Comprehensive analysis and visualizations of student performance data.")

    # Create the dashboard with all visualizations
    create_dashboard(df)
