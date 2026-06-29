import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Student Analytics Dashboard",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Analytics Dashboard")
st.markdown("---")

trusted = pd.read_csv(
    "data/trusted/trusted_student_snapshot.csv"
)
total_student = len(trusted)

avg_gpa = round(trusted["gpa"].mean(),2)

avg_salary = round(
    trusted["expected_salary_thb"].mean(),0
)

international = trusted["is_international"].sum()

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Students",
    total_student
)

c2.metric(
    "Average GPA",
    avg_gpa
)

c3.metric(
    "Expected Salary",
    f"{avg_salary:,.0f} THB"
)

c4.metric(
    "International",
    international
)

st.markdown("## 🔍 Filters")

col1,col2,col3 = st.columns(3)

campus = col1.selectbox(
    "Campus",
    ["All"] + sorted(trusted["campus"].dropna().unique().tolist())
)

faculty = col2.selectbox(
    "Faculty",
    ["All"] + sorted(trusted["faculty_or_school"].dropna().unique().tolist())
)

year = col3.selectbox(
    "Year",
    ["All"] + sorted(trusted["year_of_study"].dropna().unique().tolist())
)

df = trusted.copy()

if campus != "All":
    df = df[df["campus"]==campus]

if faculty != "All":
    df = df[df["faculty_or_school"]==faculty]

if year != "All":
    df = df[df["year_of_study"]==year]

left,right = st.columns(2)

campus_chart = (
    df.groupby("campus")
    .size()
    .reset_index(name="Student")
)

fig = px.bar(
    campus_chart,
    x="campus",
    y="Student",
    title="Students by Campus"
)

left.plotly_chart(
    fig,
    use_container_width=True
)

career = (
    df.groupby("career_interest")
    .size()
    .reset_index(name="Student")
)

fig = px.bar(
    career,
    x="career_interest",
    y="Student",
    color="Student",
    title="Career Interest"
)

right.plotly_chart(
    fig,
    use_container_width=True
)

left,right = st.columns(2)

fig = px.histogram(
    df,
    x="gpa",
    nbins=15,
    title="GPA Distribution"
)

left.plotly_chart(
    fig,
    use_container_width=True
)

faculty = (
    df.groupby("faculty_or_school")
    .size()
    .reset_index(name="Student")
)

fig = px.pie(
    faculty,
    names="faculty_or_school",
    values="Student",
    title="Faculty Distribution"
)

right.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("## 📋 Student Data")

st.dataframe(
    df,
    use_container_width=True
)

