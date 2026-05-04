import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Jaeug Choi | Data Analyst & Process Automation & BI Portfolio",
    page_icon="📊",
    layout="wide",
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 20px;
        color: #666;
        margin-top: 0px;
    }
    .section-title {
        font-size: 28px;
        font-weight: 700;
        margin-top: 35px;
        margin-bottom: 15px;
    }
    .card {
        padding: 22px;
        border-radius: 16px;
        background-color: #f8f9fa;
        border: 1px solid #e5e7eb;
        margin-bottom: 15px;
    }
    .metric-card {
        padding: 18px;
        border-radius: 14px;
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        text-align: center;
    }
    .small-text {
        color: #666;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Projects", "Skills", "Demo Dashboard", "Contact"]
)

st.sidebar.markdown("---")
st.sidebar.write("**Portfolio Focus**")
st.sidebar.write("Data Analysis · Automation · BI Reporting")

# -----------------------------
# Data
# -----------------------------
projects = [
    {
        "title": "AR Dashboard & Receivables Analysis",
        "category": "Business Analytics",
        "description": """
        <ul>
            <li>Built a data pipeline to analyze AR movement and overdue balances</li>
            <li>Developed logic to separate receivables based on service periods (pre-2025 vs post-2025 ownership)</li>
            <li>Handled customers with overlapping billing periods across multiple years</li>
            <li>Delivered a dashboard to track AR ownership and support weekly reporting</li>
        </ul>
        """,
        "impact": "Enabled accurate tracking of AR ownership and supported weekly reporting by combining business logic with dashboard-based analysis.",
        "tools": "Python, SQL, Power BI, Excel",
    },
    {
        "title": "Electricity Billing & Cash Flow Anomaly Analysis",
        "category": "Business Analytics",
        "description": """
        <ul>
            <li>Analyzed electricity consumption and billing data to identify mismatches between usage and charged amounts</li>
            <li>Built logic to account for changing tariffs (e.g., monthly and seasonal kWh price variations)</li>
            <li>Compared expected vs actual billing to detect anomalies and cash flow gaps</li>
        </ul>
        """,
        "impact": """
        <ul>
            <li>Identified discrepancies in cash flow by comparing expected vs actual billing</li>
            <li>Worked with the finance team to investigate underlying causes</li>
        </ul>
        """,
        "tools": "Python, Excel",
    },
    {
        "title": "Excel KPI Automation Workflow",
        "category": "Process Automation",
        "description": "Automated weekly KPI tracking, archive comparison, status change detection, and conditional classification logic.",
        "impact": "Reduced manual Excel workload and improved consistency in weekly operations reporting.",
        "tools": "Excel, Python, Power Query, VBA logic concepts",
    },
]

skills = {
    "Programming": ["Python", "SQL"],
    "Data & BI": ["Power BI", "Excel"],
    "Analytics": ["Process Automation", "Business Analysis"]
}

sample_ar_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Recovered_AR": [120000, 135000, 150000, 142000, 168000, 181000],
    "Overdue_AR": [220000, 210000, 198000, 205000, 187000, 175000],
    "Recovery_Rate": [54.5, 58.0, 61.2, 59.3, 64.1, 67.4],
})

# -----------------------------
# Pages
# -----------------------------
if page == "Home":
    st.markdown('<p class="main-title">Jaeug Choi</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">Process & Data Management Specialist | Data Analytics · Automation · BI Reporting</p>',
        unsafe_allow_html=True,
    )

    st.write(
        "I build data workflows, dashboards, and automation tools that help business teams reduce manual work, "
        "track operational performance, and make faster decisions."
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Report Time Saved", ">70%")
    with col2:
        st.metric("Dashboard Focus", "AR / KPI")
    with col3:
        st.metric("Core Stack", "Python + SQL + BI")

    st.markdown('<p class="section-title">About Me</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="card">
        I work in data management and operations, focusing on accounts receivable analytics, KPI reporting, dashboard maintenance, 
        and process automation. My strength is connecting business problems with practical technical solutions using Python, SQL, Power BI, and Excel.
        </div>
        """,
        unsafe_allow_html=True,
    )

elif page == "Projects":
    st.markdown('<p class="section-title">Projects</p>', unsafe_allow_html=True)

    for project in projects:
        st.markdown(
            f"""
            <div class="card">
                <h3>{project['title']}</h3>
                <p><b>Category:</b> {project['category']}</p>
                <p>{project['description']}</p>
                <p><b>Impact:</b> {project['impact']}</p>
                <p class="small-text"><b>Tools:</b> {project['tools']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif page == "Skills":
    st.markdown('<p class="section-title">Skills</p>', unsafe_allow_html=True)

    for category, items in skills.items():
        st.markdown(f"**{category}**")
        for skill in items:
            st.markdown(f"- {skill}")
            
elif page == "Demo Dashboard":
    st.markdown('<p class="section-title">Demo AR Dashboard</p>', unsafe_allow_html=True)
    st.write("This sample dashboard shows how AR recovery and overdue receivables can be tracked over time.")

    uploaded_file = st.file_uploader("Upload your own CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("CSV uploaded successfully.")
        st.dataframe(df, use_container_width=True)
    else:
        df = sample_ar_data
        st.info("Using sample AR data. Upload a CSV to test your own data.")
        st.dataframe(df, use_container_width=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Latest Recovered AR", f"€{df['Recovered_AR'].iloc[-1]:,.0f}")
    with col2:
        st.metric("Latest Overdue AR", f"€{df['Overdue_AR'].iloc[-1]:,.0f}")
    with col3:
        st.metric("Latest Recovery Rate", f"{df['Recovery_Rate'].iloc[-1]:.1f}%")

    fig1 = px.line(
        df,
        x="Month",
        y=["Recovered_AR", "Overdue_AR"],
        markers=True,
        title="Recovered AR vs Overdue AR",
    )
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.line(
        df,
        x="Month",
        y="Recovery_Rate",
        markers=True,
        title="Recovery Rate Trend (%)",
    )
    st.plotly_chart(fig2, use_container_width=True)

elif page == "Contact":
    st.markdown('<p class="section-title">Contact</p>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="card">
        <p><b>Email:</b> your.email@example.com</p>
        <p><b>LinkedIn:</b> https://www.linkedin.com/in/your-profile</p>
        <p><b>GitHub:</b> https://github.com/your-github</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("Feel free to reach out for data analytics, dashboarding, or automation-related opportunities.")

