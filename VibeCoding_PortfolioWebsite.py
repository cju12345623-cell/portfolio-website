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
    .small-text {
        color: #666;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Session State
# -----------------------------
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

if "selected_project" not in st.session_state:
    st.session_state["selected_project"] = None

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")

if st.sidebar.button("Home"):
    st.session_state["page"] = "Home"
    st.session_state["selected_project"] = None
    st.rerun()

if st.sidebar.button("Projects"):
    st.session_state["page"] = "Projects"
    st.session_state["selected_project"] = None
    st.rerun()

if st.sidebar.button("Skills"):
    st.session_state["page"] = "Skills"
    st.session_state["selected_project"] = None
    st.rerun()

if st.sidebar.button("Demo Dashboard"):
    st.session_state["page"] = "Demo Dashboard"
    st.session_state["selected_project"] = None
    st.rerun()

if st.sidebar.button("Contact"):
    st.session_state["page"] = "Contact"
    st.session_state["selected_project"] = None
    st.rerun()

page = st.session_state["page"]

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
        "impact": """
        <ul>
            <li>Enabled accurate tracking of AR ownership</li>
            <li>Supported weekly reporting by combining business logic with dashboard-based analysis</li>
        </ul>
        """,
        "tools": "Python, SQL, Power BI, Excel",
    },
    {
        "title": "Electricity Billing & Cash Flow Anomaly Analysis",
        "category": "Business Analytics",
        "description": """
        <ul>
            <li>Analyzed electricity consumption and billing data to identify mismatches between usage and charged amounts</li>
            <li>Built logic to account for changing tariffs, such as monthly and seasonal kWh price variations</li>
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
        "description": """
        <ul>
            <li>Automated weekly KPI tracking and archive comparison</li>
            <li>Implemented logic for status change detection and conditional classification</li>
            <li>Standardized weekly KPI reporting checks</li>
        </ul>
        """,
        "impact": "Reduced repetitive Excel workload and improved consistency in weekly operations reporting.",
        "tools": "Excel, Python, Power Query, VBA logic concepts",
    },
]

skills = {
    "Programming": ["Python", "SQL"],
    "Data & BI": ["Power BI", "Excel"],
    "Analytics": ["Process Automation", "Business Analysis"],
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
        "I build data pipelines, dashboards, and automation tools that help business teams reduce manual work, "
        "track operational performance, and make faster decisions."
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Focus Area", "AR Analytics")
    with col2:
        st.metric("Dashboard Focus", "AR / KPI")
    with col3:
        st.metric("Core Stack", "Python + SQL + BI")

    st.markdown('<p class="section-title">About Me</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="card">
        I work in data management and operations, focusing on accounts receivable analytics, KPI reporting, dashboard maintenance,
        and process automation. My strength is connecting business problems with practical technical solutions using Python, SQL,
        Power BI, and Excel.
        <br><br>
        <b>Education:</b> M.Sc. in Bioinformatics (ongoing), currently completing thesis while working in data analytics.
        </div>
        """,
        unsafe_allow_html=True,
    )

elif page == "Projects":
    st.markdown('<p class="section-title">Projects</p>', unsafe_allow_html=True)

    cols = st.columns(3)

    for i, project in enumerate(projects):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"### {project['title']}")
                st.markdown(f"**{project['category']}**")

                if st.button("Open Project", key=f"open_{i}"):
                    st.session_state["selected_project"] = project["title"]
                    st.session_state["page"] = "Project Detail"
                    st.rerun()

elif page == "Project Detail":
    project_name = st.session_state.get("selected_project")

    if st.button("⬅ Back to Projects"):
        st.session_state["page"] = "Projects"
        st.session_state["selected_project"] = None
        st.rerun()

    st.markdown(f'<p class="section-title">{project_name}</p>', unsafe_allow_html=True)

    selected_project = next(
        (p for p in projects if p["title"] == project_name),
        None
    )

    if selected_project:
        st.markdown(f"**Category:** {selected_project['category']}")

        st.markdown("### Overview")
        st.markdown(selected_project["description"], unsafe_allow_html=True)

        st.markdown("### Impact")
        st.markdown(selected_project["impact"], unsafe_allow_html=True)

        st.markdown(f"**Tools:** {selected_project['tools']}")
        st.markdown("---")

    if project_name == "AR Dashboard & Receivables Analysis":
        st.markdown("### Pipeline Overview")

        st.markdown(
            """
            <div class="card">
            <b>Raw AR Data</b> → <b>Cleaning</b> → <b>Merging</b> → 
            <b>Receivables Separation Logic</b> → <b>Monthly AR Dataset</b> → 
            <b>Power BI Dashboard</b>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### What the logic does")
        st.write(
            "The project separates receivables based on service periods and ownership rules. "
            "The main challenge is handling customers whose billing periods overlap across multiple years, "
            "such as 2024–2025 or 2023–2025."
        )

        flow_data = pd.DataFrame({
            "Step": [
                "Raw Data",
                "Cleaning",
                "Merging",
                "Separation Logic",
                "Reporting Dataset",
                "Dashboard",
            ],
            "Description": [
                "Collect AR and billing-related data",
                "Clean missing, duplicated, or inconsistent records",
                "Merge multiple data sources based on customer and billing references",
                "Split receivables by service period and ownership",
                "Generate structured weekly reporting data",
                "Visualize AR ownership and movement",
            ],
        })

        st.dataframe(flow_data, width="stretch")

        sample_split = pd.DataFrame({
            "AR Category": ["Company-owned AR", "Transferred AR", "Overlapping period"],
            "Amount": [420000, 310000, 95000],
        })

        fig = px.pie(
            sample_split,
            names="AR Category",
            values="Amount",
            title="Sample AR Ownership Split",
        )
        st.plotly_chart(fig, width="stretch")

    elif project_name == "Electricity Billing & Cash Flow Anomaly Analysis":
        st.markdown("### Analysis Flow")

        st.markdown(
            """
            <div class="card">
            <b>Consumption Data</b> → <b>Tariff Logic</b> → <b>Expected Billing</b> → 
            <b>Actual Billing Comparison</b> → <b>Anomaly Detection</b> → <b>Cash Flow Review</b>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### What the logic does")
        st.write(
            "This analysis compares expected charges based on electricity consumption and changing tariffs "
            "against actual billed amounts. The goal is to detect mismatches and investigate possible cash flow gaps."
        )

        sample_billing = pd.DataFrame({
            "Month": ["Jan", "Feb", "Mar", "Apr"],
            "Consumption_kWh": [1200, 1350, 1280, 1500],
            "Tariff_EUR_per_kWh": [0.30, 0.30, 0.30, 0.31],
            "Expected_Billing": [360, 405, 384, 465],
            "Actual_Billing": [360, 420, 384, 510],
        })

        sample_billing["Difference"] = (
            sample_billing["Actual_Billing"] - sample_billing["Expected_Billing"]
        )

        st.dataframe(sample_billing, width="stretch")

        fig = px.bar(
            sample_billing,
            x="Month",
            y="Difference",
            title="Sample Billing Difference by Month",
        )
        st.plotly_chart(fig, width="stretch")

    elif project_name == "Excel KPI Automation Workflow":
        st.markdown("### Workflow Overview")

        st.markdown(
            """
            <div class="card">
            <b>Weekly KPI File</b> → <b>Archive Comparison</b> → 
            <b>Status Change Detection</b> → <b>Classification Logic</b> → 
            <b>Updated KPI Report</b>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### What the workflow does")
        st.write(
            "This workflow automates repetitive Excel-based KPI checks and helps maintain consistent weekly reporting."
        )

        kpi_flow = pd.DataFrame({
            "Step": [
                "Import weekly data",
                "Compare with archive",
                "Detect changes",
                "Classify status",
                "Prepare report",
            ],
            "Purpose": [
                "Load the latest KPI file",
                "Check whether items already existed in previous archives",
                "Identify status movements and new entries",
                "Apply KPI classification logic",
                "Generate structured output for weekly review",
            ],
        })

        st.dataframe(kpi_flow, width="stretch")

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
        st.dataframe(df, width="stretch")
    else:
        df = sample_ar_data
        st.info("Using sample AR data. Upload a CSV to test your own data.")
        st.dataframe(df, width="stretch")

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
    st.plotly_chart(fig1, width="stretch")

    fig2 = px.line(
        df,
        x="Month",
        y="Recovery_Rate",
        markers=True,
        title="Recovery Rate Trend (%)",
    )
    st.plotly_chart(fig2, width="stretch")

elif page == "Contact":
    st.markdown('<p class="section-title">Contact</p>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="card">
        <p><b>Email:</b> your.email@example.com</p>
        <p><b>LinkedIn:</b> https://www.linkedin.com/in/your-profile</p>
        <p><b>GitHub:</b> https://github.com/cju12345623-cell</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("Feel free to reach out for data analytics, dashboarding, or automation-related opportunities.")