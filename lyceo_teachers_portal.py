import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Lyceo Teacher's Portal")

# Sample Data
data = {
    "Student Name": ["Alice", "Bob", "Carlos", "Diana", "Elena", "Felix", "Grace", "Henry", "Isla", "Jake"],
    "Engagement (%)": [85, 78, 90, 88, 72, 95, 80, 76, 82, 89],
    "Performance Score": [88, 75, 92, 90, 68, 97, 79, 73, 81, 86],
    "Hands-Up Count": [5, 3, 6, 7, 2, 9, 4, 3, 4, 6],
}

df = pd.DataFrame(data)

# Class Overview Table
st.subheader("Class Overview")
st.dataframe(df)

# Engagement and Performance Trends Chart
st.subheader("Class Engagement & Performance Trends")
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df["Student Name"], df["Engagement (%)"], marker="o", label="Engagement (%)")
ax.plot(df["Student Name"], df["Performance Score"], marker="s", label="Performance Score")
ax.set_xlabel("Students")
ax.set_ylabel("Percentage Score")
ax.set_title("Class Engagement & Performance Trends")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Student Selection for Details
st.subheader("Student Performance Details")
student_selected = st.selectbox("Select a student:", df["Student Name"])
student_data = df[df["Student Name"] == student_selected]
st.write(student_data)

# Hands-Up Feature Visualization
st.subheader("Hands-Up Feature")
st.bar_chart(df.set_index("Student Name")["Hands-Up Count"])
