import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configure Streamlit page
st.set_page_config(
    page_title="AI Tool Pipeline Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for executive styling
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
    .metric-container {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin: 0.5rem 0;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin: 2rem 0 1rem 0;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
    }
    .priority-high {
        background-color: #e74c3c;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .priority-medium {
        background-color: #f39c12;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .priority-low {
        background-color: #27ae60;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .insight-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin: 1rem 0;
    }
    .action-box {
        background-color: #fff3cd;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and process the AI tool pipeline data"""
    # Your actual data from the Excel file
    data = [
        {"Name": "Enterprise GPT Subscription", "Requesting Stakeholder": "Briefly Level", "Target Quarter Date Release": "Not Assigned Yet", "Evaluation Status": "Budget Evaluation", "Prioritization Status": "P2", "Reviewed By": "Ankita Avadhani", "Potential Tool Name/  Phase of Exploring Tools": "Chat GPT Enterprise", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Hubspot Copilot", "Requesting Stakeholder": "Bus Dev/ Revenue", "Target Quarter Date Release": "Not Assigned Yet", "Evaluation Status": "Budget Evaluation", "Prioritization Status": "P1", "Reviewed By": "Ankita Avadhani", "Potential Tool Name/  Phase of Exploring Tools": "GPT Integrations", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Lead/ Funnel AI Tooling", "Requesting Stakeholder": "Bus Dev/ Revenue", "Target Quarter Date Release": "Not Assigned Yet", "Evaluation Status": "Budget Evaluation", "Prioritization Status": "P1", "Reviewed By": "Ankita Avadhani", "Potential Tool Name/  Phase of Exploring Tools": "Clay AI", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Clio Data Copilot", "Requesting Stakeholder": "Briefly + All Firm", "Target Quarter Date Release": "Not Assigned Yet", "Evaluation Status": "Budget Evaluation", "Prioritization Status": "P1", "Reviewed By": "Ankita Avadhani", "Potential Tool Name/  Phase of Exploring Tools": "Clio Duo", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Managing Collections", "Requesting Stakeholder": "Briefly + All Firm", "Target Quarter Date Release": "Not Assigned Yet", "Evaluation Status": "Tool Discovery Phase", "Prioritization Status": "P0", "Reviewed By": "Monica Goyal", "Potential Tool Name/  Phase of Exploring Tools": "Caddi/Airia?", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Accounting firm scaling", "Requesting Stakeholder": "Finance/ Accounting", "Target Quarter Date Release": "Not Assigned Yet", "Evaluation Status": "Tool Discovery Phase", "Prioritization Status": "P0", "Reviewed By": "Ankita Avadhani", "Potential Tool Name/  Phase of Exploring Tools": "Discovery Phase", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Finance App Builder", "Requesting Stakeholder": "Finance/ Accounting", "Target Quarter Date Release": "Not Assigned Yet", "Evaluation Status": "Pilot", "Prioritization Status": "P0", "Reviewed By": "Monica Goyal", "Potential Tool Name/  Phase of Exploring Tools": "Decipad", "Total Priority Score": "43", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "No Code SQL + Python", "Requesting Stakeholder": "Finance/ Accounting", "Target Quarter Date Release": "Q3 2025", "Evaluation Status": "Budget Evaluation", "Prioritization Status": "P1", "Reviewed By": "Monica Goyal", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Origination + Accounting Scale", "Requesting Stakeholder": "Finance/ Accounting", "Target Quarter Date Release": "Q3 2025", "Evaluation Status": "Budget Evaluation", "Prioritization Status": "P1", "Reviewed By": "Monica Goyal", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Manual receipt capture", "Requesting Stakeholder": "Finance/ Accounting", "Target Quarter Date Release": "Q3 2025", "Evaluation Status": "Budget Evaluation", "Prioritization Status": "P1", "Reviewed By": "Monica Goyal", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Predictive Financial Forecasting", "Requesting Stakeholder": "Finance/ Accounting", "Target Quarter Date Release": "Q3 2025", "Evaluation Status": "Budget Evaluation", "Prioritization Status": "P2", "Reviewed By": "Monica Goyal", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Email Management AP Team", "Requesting Stakeholder": "IT", "Target Quarter Date Release": "Not Assigned Yet", "Evaluation Status": "Budget Evaluation", "Prioritization Status": "P1", "Reviewed By": "Monica Goyal", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Data Management Tools", "Requesting Stakeholder": "Scale Leadership", "Target Quarter Date Release": "Not Assigned Yet", "Evaluation Status": "Budget Evaluation", "Prioritization Status": "P1", "Reviewed By": "Monica Goyal", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "BD LinkedIn automation", "Requesting Stakeholder": "Scale Leadership", "Target Quarter Date Release": "Q2 2026", "Evaluation Status": "Budget Evaluation", "Prioritization Status": "P1", "Reviewed By": "Monica Goyal", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "CRM and Client Relations", "Requesting Stakeholder": "Rimon Leadership", "Target Quarter Date Release": "Not Assigned Yet", "Evaluation Status": "Budget Evaluation", "Prioritization Status": "P1", "Reviewed By": "Monica Goyal", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Document Review AI", "Requesting Stakeholder": "Briefly Level", "Target Quarter Date Release": "Not Assigned Yet", "Evaluation Status": "Budget Evaluation", "Prioritization Status": "P1", "Reviewed By": "Ankita Avadhani", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Contract Analysis AI", "Requesting Stakeholder": "Briefly Level", "Target Quarter Date Release": "Q4 2025", "Evaluation Status": "Tool Evaluation", "Prioritization Status": "P1", "Reviewed By": "Ankita Avadhani", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Lead Generation AI", "Requesting Stakeholder": "Bus Dev/ Revenue", "Target Quarter Date Release": "Not Assigned Yet", "Evaluation Status": "Tool Evaluation", "Prioritization Status": "P1", "Reviewed By": "Ankita Avadhani", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Case Management AI", "Requesting Stakeholder": "Briefly + All Firm", "Target Quarter Date Release": "Not Assigned Yet", "Evaluation Status": "Budget Evaluation", "Prioritization Status": "P1", "Reviewed By": "Ankita Avadhani", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Content Creation AI", "Requesting Stakeholder": "Marketing", "Target Quarter Date Release": "Not Assigned Yet", "Evaluation Status": "Tool Discovery Phase", "Prioritization Status": "P2", "Reviewed By": "Monica Goyal", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "AI Research Assistant", "Requesting Stakeholder": "Owner", "Target Quarter Date Release": "Not Assigned", "Evaluation Status": "Unknown", "Prioritization Status": "P1", "Reviewed By": "TBD", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Time Tracking AI", "Requesting Stakeholder": "Owner", "Target Quarter Date Release": "Not Assigned", "Evaluation Status": "Unknown", "Prioritization Status": "P2", "Reviewed By": "TBD", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""},
        {"Name": "Client Communication AI", "Requesting Stakeholder": "Owner", "Target Quarter Date Release": "Not Assigned", "Evaluation Status": "Unknown", "Prioritization Status": "P1", "Reviewed By": "TBD", "Potential Tool Name/  Phase of Exploring Tools": "TBD", "Total Priority Score": "", "Target Success Metric": "", "Estimated Budget": ""}
    ]
    
    df = pd.DataFrame(data)
    
    # Clean and standardize data
    df['Department'] = df['Requesting Stakeholder']
    df['Quarter'] = df['Target Quarter Date Release']
    df['Status'] = df['Evaluation Status']
    df['Priority'] = df['Prioritization Status']
    df['Reviewer'] = df['Reviewed By']
    df['Tool_Technology'] = df['Potential Tool Name/  Phase of Exploring Tools']
    df['Priority_Score'] = df['Total Priority Score']
    
    # Clean quarter names for better display
    quarter_mapping = {
        'Not Assigned Yet': 'Unscheduled',
        'Not Assigned': 'TBD'
    }
    df['Quarter_Clean'] = df['Quarter'].replace(quarter_mapping)
    
    return df

def create_executive_kpis(df):
    """Create executive KPI metrics"""
    total_tools = len(df)
    high_priority = len(df[df['Priority'] == 'P1'])
    scheduled_tools = len(df[~df['Quarter'].str.contains('Not Assigned', na=False)])
    in_pilot = len(df[df['Status'].str.contains('Pilot', na=False)])
    budget_evaluation = len(df[df['Status'].str.contains('Budget', na=False)])
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            label="📊 Total AI Tools",
            value=total_tools,
            help="Total number of AI tools in the pipeline"
        )
    
    with col2:
        st.metric(
            label="🔥 High Priority (P1)",
            value=high_priority,
            delta=f"{high_priority/total_tools:.0%} of total",
            help="Critical tools requiring immediate attention"
        )
    
    with col3:
        st.metric(
            label="📅 Scheduled",
            value=scheduled_tools,
            delta=f"{scheduled_tools/total_tools:.0%} scheduled",
            help="Tools with assigned target quarters"
        )
    
    with col4:
        st.metric(
            label="🧪 In Pilot",
            value=in_pilot,
            help="Tools currently being piloted"
        )
    
    with col5:
        st.metric(
            label="💰 Budget Review",
            value=budget_evaluation,
            help="Tools awaiting budget approval"
        )

def create_department_quarter_heatmap(df):
    """Create the main department x quarter roadmap using Streamlit charts"""
    st.markdown('<div class="section-header">🗓️ Department × Quarter Roadmap</div>', unsafe_allow_html=True)
    
    # Create pivot table for heatmap visualization
    pivot_data = df.groupby(['Department', 'Quarter_Clean']).size().reset_index(name='Tool_Count')
    pivot_table = pivot_data.pivot(index='Department', columns='Quarter_Clean', values='Tool_Count').fillna(0)
    
    # Display the heatmap data as a styled dataframe
    st.subheader("Tool Distribution Matrix")
    st.dataframe(
        pivot_table.style.background_gradient(cmap='Blues', axis=None),
        use_container_width=True
    )
    
    # Create bar chart for each quarter
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Tools by Department")
        dept_totals = df['Department'].value_counts()
        st.bar_chart(dept_totals)
    
    with col2:
        st.subheader("Tools by Quarter")
        quarter_totals = df['Quarter_Clean'].value_counts()
        st.bar_chart(quarter_totals)
    
    return pivot_table

def create_quarter_drill_down(df):
    """Create quarter-by-quarter breakdown with drill-down capability"""
    st.markdown('<div class="section-header">📋 Quarter-by-Quarter Breakdown</div>', unsafe_allow_html=True)
    
    # Get unique quarters sorted
    quarters = df['Quarter_Clean'].unique()
    quarters = sorted([q for q in quarters if q not in ['Unscheduled', 'TBD']] + 
                     [q for q in quarters if q in ['Unscheduled', 'TBD']])
    
    # Create tabs for each quarter
    tabs = st.tabs(quarters)
    
    for tab, quarter in zip(tabs, quarters):
        with tab:
            quarter_data = df[df['Quarter_Clean'] == quarter]
            
            if len(quarter_data) == 0:
                st.info(f"No tools scheduled for {quarter}")
                continue
            
            # Summary metrics for this quarter
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Tools", len(quarter_data))
            with col2:
                p1_count = len(quarter_data[quarter_data['Priority'] == 'P1'])
                st.metric("High Priority", p1_count)
            with col3:
                unique_depts = quarter_data['Department'].nunique()
                st.metric("Departments", unique_depts)
            
            # Department breakdown chart
            st.subheader(f"Tools by Department - {quarter}")
            dept_breakdown = quarter_data['Department'].value_counts()
            st.bar_chart(dept_breakdown)
            
            # Detailed table
            st.subheader("Detailed Tool List")
            display_cols = ['Name', 'Department', 'Priority', 'Status', 'Reviewer', 'Tool_Technology']
            quarter_display = quarter_data[display_cols].copy()
            
            # Add color coding for priorities
            def highlight_priority(row):
                if row['Priority'] == 'P1':
                    return ['background-color: #ffebee'] * len(row)
                elif row['Priority'] == 'P2':
                    return ['background-color: #fff3e0'] * len(row)
                else:
                    return ['background-color: #e8f5e8'] * len(row)
            
            styled_df = quarter_display.style.apply(highlight_priority, axis=1)
            st.dataframe(styled_df, use_container_width=True)

def create_priority_analysis(df):
    """Create priority distribution and analysis"""
    st.markdown('<div class="section-header">🎯 Priority Analysis</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Priority Distribution")
        priority_counts = df['Priority'].value_counts()
        st.bar_chart(priority_counts)
        
        # Show priority breakdown
        for priority in ['P1', 'P2', 'P0']:
            if priority in priority_counts:
                count = priority_counts[priority]
                percentage = (count / len(df)) * 100
                priority_label = {'P1': 'High Priority', 'P2': 'Medium Priority', 'P0': 'Low Priority'}[priority]
                st.write(f"**{priority_label}**: {count} tools ({percentage:.1f}%)")
    
    with col2:
        st.subheader("High Priority Tools by Department")
        high_priority_df = df[df['Priority'] == 'P1']
        if len(high_priority_df) > 0:
            high_priority_by_dept = high_priority_df['Department'].value_counts()
            st.bar_chart(high_priority_by_dept)
        else:
            st.info("No high priority tools found")

def create_status_pipeline(df):
    """Create status pipeline analysis"""
    st.markdown('<div class="section-header">⚡ Status Pipeline</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Current Status Distribution")
        status_counts = df['Status'].value_counts()
        st.bar_chart(status_counts)
        
        # Show status details
        for status, count in status_counts.items():
            percentage = (count / len(df)) * 100
            st.write(f"**{status}**: {count} tools ({percentage:.1f}%)")
    
    with col2:
        st.subheader("Status by Priority")
        status_priority = pd.crosstab(df['Status'], df['Priority'])
        st.dataframe(status_priority)

def create_executive_summary(df):
    """Create executive summary with key insights"""
    st.markdown('<div class="section-header">📈 Executive Summary</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔍 Key Insights")
        
        # Calculate key insights
        unscheduled = len(df[df['Quarter'].str.contains('Not Assigned', na=False)])
        high_priority = len(df[df['Priority'] == 'P1'])
        top_dept = df['Department'].value_counts().index[0]
        top_dept_count = df['Department'].value_counts().iloc[0]
        
        insights_html = f"""
        <div class="insight-box">
        <h4>🚨 Critical Actions Needed:</h4>
        <ul>
        <li>{unscheduled} tools need quarter assignment</li>
        <li>{high_priority} high-priority tools require immediate attention</li>
        <li>{top_dept} has the heaviest pipeline ({top_dept_count} tools)</li>
        </ul>
        
        <h4>📊 Pipeline Health:</h4>
        <ul>
        <li>{len(df[df['Status'].str.contains('Budget', na=False)])} tools awaiting budget approval</li>
        <li>{len(df[df['Status'].str.contains('Pilot', na=False)])} tools in pilot phase</li>
        <li>{len(df[df['Reviewer'].str.contains('TBD', na=False)])} tools need reviewer assignment</li>
        </ul>
        </div>
        """
        st.markdown(insights_html, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📋 Recommended Actions")
        
        recommendations_html = """
        <div class="action-box">
        <h4>⚡ Immediate (This Week):</h4>
        <ol>
        <li>Assign quarters to unscheduled high-priority tools</li>
        <li>Allocate budget for tools in evaluation phase</li>
        <li>Assign reviewers to unassigned tools</li>
        </ol>
        
        <h4>📅 Short-term (This Month):</h4>
        <ol>
        <li>Resource planning for Q3 2025 deliveries</li>
        <li>Pilot program expansion decisions</li>
        <li>Department capacity assessment</li>
        </ol>
        
        <h4>🎯 Strategic (This Quarter):</h4>
        <ol>
        <li>AI tool portfolio optimization</li>
        <li>Cross-department collaboration planning</li>
        <li>Success metrics definition</li>
        </ol>
        </div>
        """
        st.markdown(recommendations_html, unsafe_allow_html=True)

def create_detailed_analysis(df):
    """Create detailed analysis sections"""
    st.markdown('<div class="section-header">🔬 Detailed Analysis</div>', unsafe_allow_html=True)
    
    # Reviewer workload analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Reviewer Workload")
        reviewer_counts = df['Reviewer'].value_counts()
        st.bar_chart(reviewer_counts)
    
    with col2:
        st.subheader("Technology Focus Areas")
        tech_keywords = []
        for tech in df['Tool_Technology'].dropna():
            if tech and tech != 'TBD':
                tech_keywords.append(tech.split()[0] if tech.split() else 'Other')
        
        if tech_keywords:
            tech_df = pd.DataFrame(tech_keywords, columns=['Technology'])
            tech_counts = tech_df['Technology'].value_counts().head(10)
            st.bar_chart(tech_counts)
        else:
            st.info("Technology information being evaluated")

def main():
    """Main dashboard function"""
    # Header
    st.markdown('<div class="main-header">🚀 AI Tool Pipeline Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Executive Strategic Overview | COO Dashboard</div>', unsafe_allow_html=True)
    st.markdown(f"*Last Updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*")
    
    st.markdown("---")
    
    # Load data
    df = load_data()
    
    # Executive KPIs
    st.markdown("## 📊 Executive Dashboard")
    create_executive_kpis(df)
    
    st.markdown("---")
    
    # Main roadmap heatmap
    pivot_table = create_department_quarter_heatmap(df)
    
    st.markdown("---")
    
    # Quarter breakdown with drill-down
    create_quarter_drill_down(df)
    
    st.markdown("---")
    
    # Priority and status analysis
    col1, col2 = st.columns(2)
    with col1:
        create_priority_analysis(df)
    with col2:
        create_status_pipeline(df)
    
    st.markdown("---")
    
    # Detailed analysis
    create_detailed_analysis(df)
    
    st.markdown("---")
    
    # Executive summary
    create_executive_summary(df)
    
    st.markdown("---")
    
    # Raw data table (collapsible)
    with st.expander("📊 Complete Data Table", expanded=False):
        st.dataframe(
            df[['Name', 'Department', 'Quarter', 'Priority', 'Status', 'Reviewer', 'Tool_Technology']],
            use_container_width=True
        )

if __name__ == "__main__":
    main()
