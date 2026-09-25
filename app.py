import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from data_procesing import process_student_data





# Page configuration
st.set_page_config(
    page_title="Student Academic Risk",
    page_icon="🎓",
    layout="wide"
)

# Title
st.title("🎓 Student Academic Risk Early Warning System")

st.write(
    "Dashboard for monitoring student academic performance "
    "and identifying students who may need support."
)


#process the data
data = process_student_data()



# Display data
# Calculate risk counts
total_students = len(data)

high_risk = len(
    data[data["risk_level"] == "High Risk"]
)

medium_risk = len(
    data[data["risk_level"] == "Medium Risk"]
)

low_risk = len(
    data[data["risk_level"] == "Low Risk"]
)

# Display summary
st.subheader("📊 Risk Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Students",
        total_students
    )

with col2:
    st.metric(
        "🔴 High Risk",
        high_risk
    )

with col3:
    st.metric(
        "🟡 Medium Risk",
        medium_risk
    )

with col4:
    st.metric(
        "🟢 Low Risk",
        low_risk
    )



# Risk Distribution
st.subheader("📊 Risk Distribution")

risk_counts = data["risk_level"].value_counts()

fig, ax = plt.subplots(figsize=(4, 2.5))

risk_counts.plot(
    kind="bar",
    ax=ax,
    width=0.5
)

ax.set_xlabel("")
ax.set_ylabel("Students")
ax.set_title("Academic Risk Distribution", fontsize=12)

ax.tick_params(
    axis="both",
    labelsize=9
)

ax.tick_params(
    axis="x",
    rotation=0
)

plt.tight_layout()

st.pyplot(fig, width="content")


# Risk Filter
st.subheader("🔎 Filter Students")

risk_options = ["All", "High Risk", "Medium Risk", "Low Risk"]

selected_risk = st.selectbox(
    "Select Risk Level",
    risk_options
)

if selected_risk == "All":
    filtered_data = data
else:
    filtered_data = data[
        data["risk_level"] == selected_risk
    ]


# Risk Reason Filter
reason_options = [
    "All",
    "Low Attendance",
    "Low Assignment Score",
    "Low Mid-term Score"
]

selected_reason = st.selectbox(
    "Select Risk Reason",
    reason_options
)

if selected_reason == "All":
    filtered_data = filtered_data
else:
    filtered_data = filtered_data[
        filtered_data["risk_reason"].str.contains(
            selected_reason,
            na=False
        )
    ]


    # Student Search
st.subheader("🔍 Search Student")

search_text = st.text_input(
    "Enter student name or Roll No."
)

if search_text:
    filtered_data = filtered_data[
        filtered_data["student_name"].str.contains(
            search_text,
            case=False,
            na=False
        )
        |
        filtered_data["student_id"].str.contains(
            search_text,
            case=False,
            na=False
        )
    ]
# Display student data
st.subheader("📋 Student Risk Data")

display_data = filtered_data[[
    "student_id",
    "student_name",
    "attendance",
    "assignment_score",
    "mid_score",
    "risk_level",
    "risk_reason"
]].copy()


# Colour risk level
def highlight_risk(value):
    if value == "High Risk":
        return "color: #b30000; font-weight: bold"
    elif value == "Medium Risk":
        return " color: #996600; font-weight: bold"
    elif value == "Low Risk":
        return "color: #006600; font-weight: bold"
    return ""


def highlight_reason(value):
    if "Low Attendance" in value:
        return "color: #b30000; font-weight: bold"
    elif "Low Assignment Score" in value:
        return "color: #996600; font-weight: bold"
    elif "Low Mid-term Score" in value:
        return " color: #0059b3; font-weight: bold"
    elif value == "No major risk":
        return "color: #006600; font-weight: bold"

    return ""

styled_data = display_data.style.map(
    highlight_risk,
    subset=["risk_level"]
).map(
    highlight_reason,
    subset=["risk_reason"]
)


st.dataframe(
    styled_data,
    width="stretch"
)   




# Student Performance
st.subheader("📈 Student Performance")

student_list = data["student_id"].tolist()

selected_student = st.selectbox(
    "Select Student",
    student_list
)

student = data[
    data["student_id"] == selected_student
].iloc[0]

performance = pd.Series({
    "Attendance": student["attendance"],
    "Assignment": student["assignment_percentage"],
    "Mid-term": student["mid_percentage"],
    "Overall": student["overall_score"]
})

fig, ax = plt.subplots(figsize=(4, 2.5))

performance.plot(
    kind="bar",
    ax=ax,
    width=0.5
)

ax.set_ylabel("Percentage")
ax.set_title(
    f"{student['student_name']}'s - Performance"
)

ax.set_ylim(0, 100)
ax.tick_params(axis="x", rotation=0, labelsize=9)
ax.tick_params(axis="y", labelsize=9)

st.pyplot(fig, width="content")    



