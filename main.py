import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Configure page
st.set_page_config(
    page_title="AI Tool Pipeline Dashboard",
    page_icon="🚀",
    layout="wide"
)

# CSS
st.markdown("""
<style>
.main-header {
    font-size: 2.5rem;
    font-weight: 700;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 0.5rem;
}
.sub-header {
    font-size: 1.2rem;
    color: #7f8c8d;
    text-align: center;
    margin-bottom: 2rem;
}
.section-header {
    font-size: 1.5rem;
    font-weight: 600;
    color: #2c3e50;
    margin: 2rem 0 1rem 0;
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load AI tool pipeline data"""
    data = [
        {"Name": "Enterprise GPT Subscription", "Department": "Briefly Level", "Quarter": "Not Assigned Yet", "Status": "Budget Evaluation", "Priority": "P2", "Reviewer": "Ankita Avadhani"},
        {"Name": "Hubspot Copilot", "Department": "Bus Dev/ Revenue", "Quarter": "Not Assigned Yet", "Status": "Budget Evaluation", "Priority": "P1", "Reviewer": "Ankita Avadhani"},
        {"Name": "Lead/ Funnel AI Tooling", "Department": "Bus Dev/ Revenue", "Quarter": "Not Assigned Yet", "Status": "Budget Evaluation", "Priority": "P1", "Reviewer": "Ankita Avadhani"},
        {"Name": "Clio Data Copilot", "Department": "Briefly + All Firm", "Quarter": "Not Assigned Yet", "Status": "Budget Evaluation", "Priority": "P1", "Reviewer": "Ankita Avadhani"},
        {"Name": "Managing Collections", "Department": "Briefly + All Firm", "Quarter": "Not Assigned Yet", "Status": "Tool Discovery Phase", "Priority": "P0", "Reviewer": "Monica Goyal"},
        {"Name": "Accounting firm scaling", "Department": "Finance/ Accounting", "Quarter": "Not Assigned Yet", "Status": "Tool Discovery Phase", "Priority": "P0", "Reviewer": "Ankita Avadhani"},
        {"Name": "Finance App Builder", "Department": "Finance/ Accounting", "Quarter": "Not Assigned Yet", "Status": "Pilot", "Priority": "P0", "Reviewer": "Monica Goyal"},
        {"Name": "No Code SQL + Python", "Department": "Finance/ Accounting", "Quarter": "Q3 2025", "Status": "Budget Evaluation", "Priority": "P1", "Reviewer": "Monica Goyal"},
        {"Name": "Origination + Accounting Scale", "Department": "Finance/ Accounting", "Quarter": "Q3 2025", "Status": "Budget Evaluation", "Priority": "P1", "Reviewer": "Monica Goyal"},
        {"Name": "Manual receipt capture", "Department": "Finance/ Accounting", "Quarter": "Q3 2025", "Status": "Budget Evaluation", "Priority": "P1", "Reviewer": "Monica Goyal"},
        {"Name": "Predictive Financial Forecasting", "Department": "Finance/ Accounting", "Quarter": "Q3 2025", "Status": "Budget Evaluation", "Priority": "P2", "Reviewer": "Monica Goyal"},
        {"Name": "Email Management AP Team", "Department": "IT", "Quarter": "Not Assigned Yet", "Status": "Budget Evaluation", "Priority": "P1", "Reviewer": "Monica Goyal"},
        {"Name": "Data Management Tools", "Department": "Scale Leadership", "Quarter": "Not Assigned Yet", "Status": "Budget Evaluation", "Priority": "P1", "Reviewer": "Monica Goyal"},
        {"Name": "BD LinkedIn automation", "Department": "Scale Leadership", "Quarter": "Q2 2026", "Status": "Budget Evaluation", "Priority": "P1", "Reviewer": "Monica Goyal"},
        {"Name": "CRM and Client Relations", "Department": "Rimon Leadership", "Quarter": "Not Assigned Yet", "Status": "Budget Evaluation", "Priority": "P1", "Reviewer": "Monica Goyal"},
        {"Name": "Document Review AI", "Department": "Briefly Level", "Quarter": "Not Assigned Yet", "Status": "Budget Evaluation", "Priority": "P1", "Reviewer": "Ankita Avadhani"},
        {"Name": "Contract Analysis AI", "Department": "Briefly Level", "Quarter": "Q4 2025", "Status": "Tool Evaluation", "Priority": "P1", "Reviewer": "Ankita Avadhani"},
        {"Name": "Lead Generation AI", "Department": "Bus Dev/ Revenue", "Quarter": "Not Assigned Yet", "Status": "Tool Evaluation", "Priority": "P1", "Reviewer": "Ankita Avadhani"},
        {"Name": "Case Management AI", "Department": "Briefly + All Firm", "Quarter": "Not Assigned Yet", "Status": "Budget Evaluation", "Priority": "P1", "Reviewer": "Ankita Avadhani"},
        {"Name": "Content Creation AI", "Department": "Marketing", "Quarter": "Not Assigned Yet", "Status": "Tool Discovery Phase", "Priority": "P2", "Reviewer": "Monica Goyal"},
        {"Name": "AI Research Assistant", "Department": "Owner", "Quarter": "Not Assigned", "Status": "Unknown", "Priority": "P1", "Reviewer": "TBD"},
        {"Name": "Time Tracking AI", "Department": "Owner", "Quarter": "Not Assigned", "Status": "Unknown", "Priority": "P2", "Reviewer": "TBD"},
        {"Name": "Client Communication AI", "Department": "Owner", "Quarter": "Not Assigned", "Status": "Unknown", "Priority": "P1", "Reviewer": "TBD"}
    ]
    
    df = pd.DataFrame(data)
    df['Quarter_Clean'] = df['Quarter'].replace({
        'Not Assigned Yet': 'Unscheduled',
        'Not Assigned': 'TBD'
    })
    return df

def main():
    # Header
    st.markdown('<div class="main-header">🚀 AI Tool Pipeline Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Executive Strategic Overview | COO Dashboard</div>', unsafe_allow_html=True)
    st.markdown(f"*Last Updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*")
    
    # Load data
    df = load_data()
    
    # KPIs
    st.markdown("## 📊 Executive Dashboard")
    
    total_tools = len(df)
    high_priority = len(df[df['Priority'] == 'P1'])
    scheduled_tools = len(df[~df['Quarter'].str.contains('Not Assigned', na=False)])
    in_pilot = len(df[df['Status'].str.contains('Pilot', na=False)])
    budget_evaluation = len(df[df['Status'].str.contains('Budget', na=False)])
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("📊 Total AI Tools", total_tools)
    with col2:
        st.metric("🔥 High Priority (P1)", high_priority, f"{high_priority/total_tools:.0%} of total")
    with col3:
        st.metric("📅 Scheduled", scheduled_tools, f"{scheduled_tools/total_tools:.0%} scheduled")
    with col4:
        st.metric("🧪 In Pilot", in_pilot)
    with col5:
        st.metric("💰 Budget Review", budget_evaluation)
    
    st.markdown("---")
    
    # Department x Quarter Matrix
    st.markdown('<div class="section-header">🗓️ Department × Quarter Roadmap</div>', unsafe_allow_html=True)
    
    pivot_data = df.groupby(['Department', 'Quarter_Clean']).size().reset_index(name='Tool_Count')
    pivot_table = pivot_data.pivot(index='Department', columns='Quarter_Clean', values='Tool_Count').fillna(0)
    
    st.subheader("Tool Distribution Matrix")
    st.dataframe(
        pivot_table.style.background_gradient(cmap='Blues', axis=None),
        use_container_width=True
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Tools by Department")
        dept_totals = df['Department'].value_counts()
        st.bar_chart(dept_totals)
    
    with col2:
        st.subheader("Tools by Quarter")
        quarter_totals = df['Quarter_Clean'].value_counts()
        st.bar_chart(quarter_totals)
    
    st.markdown("---")
    
    # Quarter Breakdown
    st.markdown('<div class="section-header">📋 Quarter-by-Quarter Breakdown</div>', unsafe_allow_html=True)
    
    quarters = ['Q3 2025', 'Q4 2025', 'Q2 2026', 'Unscheduled', 'TBD']
    tabs = st.tabs(quarters)
    
    for tab, quarter in zip(tabs, quarters):
        with tab:
            quarter_data = df[df['Quarter_Clean'] == quarter]
            
            if len(quarter_data) == 0:
                st.info(f"No tools scheduled for {quarter}")
                continue
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Tools", len(quarter_data))
            with col2:
                p1_count = len(quarter_data[quarter_data['Priority'] == 'P1'])
                st.metric("High Priority", p1_count)
            with col3:
                unique_depts = quarter_data['Department'].nunique()
                st.metric("Departments", unique_depts)
            
            st.subheader(f"Tools by Department - {quarter}")
            if len(quarter_data) > 0:
                dept_breakdown = quarter_data['Department'].value_counts()
                st.bar_chart(dept_breakdown)
            
            st.subheader("Detailed Tool List")
            display_cols = ['Name', 'Department', 'Priority', 'Status', 'Reviewer']
            quarter_display = quarter_data[display_cols].copy()
            st.dataframe(quarter_display, use_container_width=True)
    
    st.markdown("---")
    
    # Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div
