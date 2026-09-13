import streamlit as st
import pandas as pd
import random

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
    135deg,
    #0f172a,
    #1e1b4b,
    #312e81,
    #0f172a
    );
    color: white;
}

/* ALL TEXT */

label, p, div, span {
    color: white !important;
}

/* TITLE */

h1 {
    color: #60a5fa;
    text-align: center;
    font-size: 50px;
}

/* BUTTON */

.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #2563eb, #7c3aed);
    color: white;
    font-size: 18px;
    border-radius: 12px;
    height: 3em;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(to right, #1d4ed8, #6d28d9);
    color: white;
}

/* PREDICTION BOX */

.prediction-box {
    padding: 20px;
    border-radius: 15px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.1);
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    color: white;
}

/* SLIDER LABELS */

.stSlider label {
    color: white !important;
    font-size: 20px !important;
    font-weight: bold !important;
}

/* SLIDER VALUES */

.stSlider div {
    color: white !important;
}

/* DROPDOWN BOX */

div[data-baseweb="select"] > div {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 10px !important;
}

/* DROPDOWN TEXT */

div[data-baseweb="select"] span {
    color: white !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

/* DROPDOWN MENU */

ul {
    background-color: #1e293b !important;
}

/* DROPDOWN OPTIONS */

li {
    color: white !important;
    font-size: 16px !important;
}

/* HOVER EFFECT */

li:hover {
    background-color: #312e81 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.title("🎓 Student Performance Predictor")

st.write("### Predict • Analyze • Improve Student Performance")

st.write("---")

# ---------------- INPUT SECTION ---------------- #

st.markdown("## 📋 Enter Student Details")

# STUDY HOURS

st.write("### 📚 Study Hours per Day")

study_hours = st.slider(
    "Study Hours",
    0.0, 12.0, 2.0,
    key="study",
    label_visibility="collapsed"
)

# ATTENDANCE

st.write("### 📅 Attendance Percentage")

attendance = st.slider(
    "Attendance",
    0.0, 100.0, 80.0,
    key="attendance",
    label_visibility="collapsed"
)

# MENTAL HEALTH

st.write("### 🧠 Mental Health Rating")

mental_health = st.slider(
    "Mental Health",
    1, 10, 5,
    key="mental",
    label_visibility="collapsed"
)

# SLEEP HOURS

st.write("### 😴 Sleep Hours per Night")

sleep_hours = st.slider(
    "Sleep Hours",
    0.0, 12.0, 7.0,
    key="sleep",
    label_visibility="collapsed"
)

# PART TIME JOB

st.write("### 💼 Part-Time Job")

part_time_job = st.selectbox(
    "Part Time Job",
    ["No", "Yes"],
    label_visibility="collapsed"
)

# ---------------- PREDICTION ---------------- #

if st.button("🚀 Predict Exam Score"):

    score = (
        study_hours * 5
        + attendance * 0.3
        + mental_health * 2
        + sleep_hours * 2
    )

    if part_time_job == "Yes":
        score -= 5

    score = max(0, min(100, score))

    # RESULT BOX

    st.markdown(
        f"""
        <div class="prediction-box">
            🎯 Predicted Exam Score: {score:.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # PROGRESS BAR

    st.progress(int(score))

    # PERFORMANCE STATUS

    if score >= 85:
        st.success("🏆 Excellent Performance")
        st.balloons()

    elif score >= 60:
        st.warning("📘 Average Performance")

    else:
        st.error("⚠ Needs Improvement")

    # RECOMMENDATIONS

    st.write("## 🤖 Recommendations")

    if study_hours < 3:
        st.info("📚 Increase study hours for better performance.")

    if attendance < 75:
        st.info("🏫 Improve attendance percentage.")

    if sleep_hours < 6:
        st.info("😴 Maintain proper sleep schedule.")

    if mental_health < 5:
        st.info("🧠 Focus on mental wellness.")

    if part_time_job == "Yes":
        st.info("💼 Balance work and study time effectively.")

    # BAR CHART

    st.write("## 📊 Student Analysis")

    chart_data = pd.DataFrame({
        "Factors": [
            "Study Hours",
            "Attendance",
            "Mental Health",
            "Sleep Hours"
        ],
        "Values": [
            study_hours * 10,
            attendance,
            mental_health * 10,
            sleep_hours * 10
        ]
    })

    st.bar_chart(chart_data.set_index("Factors"))

    # MOTIVATION

    quotes = [
        "Success is the sum of small efforts repeated daily.",
        "Consistency beats motivation.",
        "Dream big. Study smart.",
        "Every topper was once a beginner."
    ]

    st.info(f"💡 Motivation: {random.choice(quotes)}")

    # DOWNLOAD REPORT

    report = f'''
STUDENT PERFORMANCE REPORT

Predicted Score: {score:.2f}

Study Hours: {study_hours}
Attendance: {attendance}
Mental Health: {mental_health}
Sleep Hours: {sleep_hours}
Part-Time Job: {part_time_job}
'''

    st.download_button(
        "📥 Download Report",
        report,
        file_name="student_report.txt"
    )

# ---------------- ABOUT PROJECT ---------------- #

st.write("---")

st.write("## ℹ About Project")

st.info("""
This Machine Learning-based Student Performance Prediction
system analyzes student behavior and academic factors
to predict exam scores and provide recommendations.
""")

# ---------------- FOOTER ---------------- #

st.markdown("""
<hr>
<center>
Developed with ❤️ using Streamlit & Machine Learning
</center>
""", unsafe_allow_html=True)