import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="Employee Attrition Dashboard",
    layout="wide"
)

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

# REPLACE THIS WITH YOUR ACTUAL CSV FILE NAME
df = pd.read_csv(r"C:\Users\niles\Downloads\Palo Alto Networks.csv")

# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title("Employee Attrition Analytics Dashboard")

st.markdown("""
Interactive workforce analytics dashboard for employee attrition analysis.
""")

# -------------------------------------------------
# SIDEBAR FILTERS
# -------------------------------------------------

st.sidebar.header("Dashboard Filters")

department_filter = st.sidebar.multiselect(
    "Select Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)

jobrole_filter = st.sidebar.multiselect(
    "Select Job Role",
    options=df["JobRole"].unique(),
    default=df["JobRole"].unique()
)

overtime_filter = st.sidebar.multiselect(
    "Overtime",
    options=df["OverTime"].unique(),
    default=df["OverTime"].unique()
)

travel_filter = st.sidebar.multiselect(
    "Business Travel",
    options=df["BusinessTravel"].unique(),
    default=df["BusinessTravel"].unique()
)

tenure_filter = st.sidebar.slider(
    "Years At Company",
    int(df["YearsAtCompany"].min()),
    int(df["YearsAtCompany"].max()),
    (
        int(df["YearsAtCompany"].min()),
        int(df["YearsAtCompany"].max())
    )
)

# -------------------------------------------------
# APPLY FILTERS
# -------------------------------------------------

filtered_df = df[
    (df["Department"].isin(department_filter)) &
    (df["JobRole"].isin(jobrole_filter)) &
    (df["OverTime"].isin(overtime_filter)) &
    (df["BusinessTravel"].isin(travel_filter)) &
    (
        df["YearsAtCompany"].between(
            tenure_filter[0],
            tenure_filter[1]
        )
    )
]

# -------------------------------------------------
# KPI SECTION
# -------------------------------------------------

total_employees = len(filtered_df)

employees_left = len(
    filtered_df[filtered_df["Attrition"] == 1]
)

employees_retained = len(
    filtered_df[filtered_df["Attrition"] == 0]
)

attrition_rate = (
    employees_left / total_employees
) * 100 if total_employees > 0 else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Employees",
    total_employees
)

col2.metric(
    "Employees Left",
    employees_left
)

col3.metric(
    "Employees Retained",
    employees_retained
)

col4.metric(
    "Attrition Rate",
    f"{attrition_rate:.2f}%"
)

st.divider()

# -------------------------------------------------
# PIE CHART
# -------------------------------------------------

st.subheader("Retention vs Attrition Distribution")

overview_df = pd.DataFrame({
    "Category": ["Retained", "Exited"],
    "Count": [employees_retained, employees_left]
})

fig_pie = px.pie(
    overview_df,
    names="Category",
    values="Count",
    hole=0.4
)

st.plotly_chart(fig_pie, use_container_width=True)

# -------------------------------------------------
# DEPARTMENT ATTRITION
# -------------------------------------------------

st.subheader("Department-wise Attrition")

department_attrition = (
    filtered_df
    .groupby("Department")["Attrition"]
    .mean()
    .reset_index()
)

department_attrition["AttritionRate"] = (
    department_attrition["Attrition"] * 100
)

fig1 = px.bar(
    department_attrition,
    x="Department",
    y="AttritionRate",
    text_auto=".2f",
    title="Department Attrition Rate (%)"
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------------------------------------
# ROLE EXIT FREQUENCY
# -------------------------------------------------

st.subheader("Role-wise Exit Frequency")

role_exit = (
    filtered_df[filtered_df["Attrition"] == 1]
    .groupby("JobRole")
    .size()
    .reset_index(name="ExitCount")
)

role_exit = role_exit.sort_values(
    by="ExitCount",
    ascending=False
)

fig2 = px.bar(
    role_exit,
    x="ExitCount",
    y="JobRole",
    orientation="h",
    text_auto=True,
    title="Employee Exits by Job Role"
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------------------------------
# AGE GROUP ANALYSIS
# -------------------------------------------------

st.subheader("Age Group Attrition Analysis")

bins = [18, 25, 35, 45, 55, 65]

labels = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "56-65"
]

filtered_df["AgeGroup"] = pd.cut(
    filtered_df["Age"],
    bins=bins,
    labels=labels
)

age_attrition = (
    filtered_df
    .groupby("AgeGroup")["Attrition"]
    .mean()
    .reset_index()
)

age_attrition["AttritionRate"] = (
    age_attrition["Attrition"] * 100
)

fig3 = px.bar(
    age_attrition,
    x="AgeGroup",
    y="AttritionRate",
    text_auto=".2f",
    title="Age Group Attrition Rate (%)"
)

st.plotly_chart(fig3, use_container_width=True)

# -------------------------------------------------
# OVERTIME ANALYSIS
# -------------------------------------------------

st.subheader("Overtime Impact")

overtime_attrition = (
    filtered_df
    .groupby("OverTime")["Attrition"]
    .mean()
    .reset_index()
)

overtime_attrition["AttritionRate"] = (
    overtime_attrition["Attrition"] * 100
)

fig4 = px.bar(
    overtime_attrition,
    x="OverTime",
    y="AttritionRate",
    text_auto=".2f",
    title="Overtime vs Attrition"
)

st.plotly_chart(fig4, use_container_width=True)

# -------------------------------------------------
# BUSINESS TRAVEL ANALYSIS
# -------------------------------------------------

st.subheader("Business Travel Impact")

travel_attrition = (
    filtered_df
    .groupby("BusinessTravel")["Attrition"]
    .mean()
    .reset_index()
)

travel_attrition["AttritionRate"] = (
    travel_attrition["Attrition"] * 100
)

fig5 = px.bar(
    travel_attrition,
    x="BusinessTravel",
    y="AttritionRate",
    text_auto=".2f",
    title="Business Travel vs Attrition"
)

st.plotly_chart(fig5, use_container_width=True)

# -------------------------------------------------
# HEATMAP
# -------------------------------------------------

st.subheader("Department and Role Attrition Heatmap")

heatmap_data = (
    filtered_df
    .pivot_table(
        values="Attrition",
        index="Department",
        columns="JobRole",
        aggfunc="mean"
    )
)

heatmap_data = heatmap_data * 100

fig_heatmap = px.imshow(
    heatmap_data,
    text_auto=".1f",
    aspect="auto",
    title="Attrition Heatmap (%)"
)

st.plotly_chart(fig_heatmap, use_container_width=True)

# -------------------------------------------------
# RAW DATA
# -------------------------------------------------

st.subheader("Filtered Employee Data")

st.dataframe(filtered_df)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.divider()

st.markdown("""
Dashboard developed using Streamlit and Plotly for workforce attrition analytics.
""")