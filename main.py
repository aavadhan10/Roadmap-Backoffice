import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
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
    .stMetric {
        background-color: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
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
    """Load and process the AI tool pipeline data"""
    # Sample data structure based on your Excel file
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
    """Create the main department x quarter heatmap"""
    st.markdown('<div class="section-header">🗓️ Department × Quarter Roadmap</div>', unsafe_allow_html=True)
    
    # Create pivot table for heatmap
    pivot_data = df.groupby(['Department', 'Quarter_Clean']).size().reset_index(name='Tool_Count')
    pivot_table = pivot_data.pivot(index='Department', columns='Quarter_Clean', values='Tool_Count').fillna(0)
    
    # Create heatmap
    fig = px.imshow(
        pivot_table,
        labels=dict(x="Target Quarter", y="Department", color="Number of Tools"),
        title="AI Tool Distribution by Department and Quarter",
        color_continuous_scale="Blues",
        aspect="auto"
    )
    
    # Add text annotations
    for i, dept in enumerate(pivot_table.index):
        for j, quarter in enumerate(pivot_table.columns):
            value = pivot_table.loc[dept, quarter]
            if value > 0:
                fig.add_annotation(
                    x=j, y=i,
                    text=str(int(value)),
                    showarrow=False,
                    font=dict(color="white" if value > 2 else "black", size=14)
                )
    
    fig.update_layout(
        height=500,
        font_size=12,
        title_font_size=16
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
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
            
            # Department breakdown
            st.subheader(f"Tools by Department - {quarter}")
            dept_breakdown = quarter_data.groupby('Department').agg({
                'Name': 'count',
                'Priority': lambda x: (x == 'P1').sum()
            }).rename(columns={'Name': 'Total_Tools', 'Priority': 'High_Priority'})
            
            # Create bar chart
            fig = px.bar(
                dept_breakdown.reset_index(),
                x='Department',
                y='Total_Tools',
                title=f"Tool Distribution by Department - {quarter}",
                color='High_Priority',
                color_continuous_scale='Reds',
                labels={'Total_Tools': 'Number of Tools', 'High_Priority': 'P1 Tools'}
            )
            fig.update_layout(height=400, xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)
            
            # Detailed table
            st.subheader("Detailed Tool List")
            display_cols = ['Name', 'Department', 'Priority', 'Status', 'Reviewer', 'Tool_Technology']
            quarter_display = quarter_data[display_cols].copy()
            
            # Color code priorities
            def color_priority(val):
                if val == 'P1':
                    return 'background-color: #e74c3c; color: white'
                elif val == 'P2':
                    return 'background-color: #f39c12; color: white'
                else:
                    return 'background-color: #27ae60; color: white'
            
            styled_df = quarter_display.style.applymap(color_priority, subset=['Priority'])
            st.dataframe(styled_df, use_container_width=True)

def create_priority_analysis(df):
    """Create priority distribution and analysis"""
    st.markdown('<div class="section-header">🎯 Priority Analysis</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Priority distribution pie chart
        priority_counts = df['Priority'].value_counts()
        fig = px.pie(
            values=priority_counts.values,
            names=priority_counts.index,
            title="Priority Distribution",
            color_discrete_map={'P1': '#e74c3c', 'P2': '#f39c12', 'P0': '#27ae60'}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Priority by department
        priority_dept = df.groupby(['Department', 'Priority']).size().reset_index(name='count')
        fig = px.bar(
            priority_dept,
            x='Department',
            y='count',
            color='Priority',
            title="Priority Distribution by Department",
            color_discrete_map={'P1': '#e74c3c', 'P2': '#f39c12', 'P0': '#27ae60'}
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

def create_status_pipeline(df):
    """Create status pipeline analysis"""
    st.markdown('<div class="section-header">⚡ Status Pipeline</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Status distribution
        status_counts = df['Status'].value_counts()
        fig = px.bar(
            x=status_counts.index,
            y=status_counts.values,
            title="Current Status Distribution",
            color=status_counts.values,
            color_continuous_scale='Blues'
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Status by quarter
        status_quarter = df.groupby(['Quarter_Clean', 'Status']).size().reset_index(name='count')
        fig = px.bar(
            status_quarter,
            x='Quarter_Clean',
            y='count',
            color='Status',
            title="Status Distribution by Quarter",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

def create_timeline_gantt(df):
    """Create a Gantt-style timeline"""
    st.markdown('<div class="section-header">📅 Executive Timeline</div>', unsafe_allow_html=True)
    
    # Filter out unscheduled items for timeline
    timeline_df = df[~df['Quarter'].str.contains('Not Assigned', na=False)].copy()
    
    if len(timeline_df) == 0:
        st.warning("No tools have been scheduled with specific quarters yet.")
        return
    
    # Create a simplified timeline visualization
    timeline_summary = timeline_df.groupby(['Quarter_Clean', 'Department']).agg({
        'Name': lambda x: ', '.join(x.head(3)) + ('...' if len(x) > 3 else ''),
        'Priority': lambda x: list(x)
    }).reset_index()
    
    # Create timeline chart
    fig = go.Figure()
    
    departments = timeline_summary['Department'].unique()
    colors = px.colors.qualitative.Set3
    
    for i, dept in enumerate(departments):
        dept_data = timeline_summary[timeline_summary['Department'] == dept]
        fig.add_trace(go.Scatter(
            x=dept_data['Quarter_Clean'],
            y=[dept] * len(dept_data),
            mode='markers+text',
            marker=dict(size=20, color=colors[i % len(colors)]),
            text=[f"{len(p)} tools" for p in dept_data['Priority']],
            textposition="middle center",
            name=dept,
            hovertemplate=f"<b>{dept}</b><br>Quarter: %{{x}}<br>Tools: %{{text}}<extra></extra>"
        ))
    
    fig.update_layout(
        title="Executive Timeline Overview",
        xaxis_title="Quarter",
        yaxis_title="Department",
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)

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
        
        insights = f"""
        **Critical Actions Needed:**
        - 🚨 {unscheduled} tools need quarter assignment
        - 🔥 {high_priority} high-priority tools require immediate attention
        - 📊 {top_dept} has the heaviest pipeline ({top_dept_count} tools)
        
        **Pipeline Health:**
        - {len(df[df['Status'].str.contains('Budget', na=False)])} tools awaiting budget approval
        - {len(df[df['Status'].str.contains('Pilot', na=False)])} tools in pilot phase
        - {len(df[df['Reviewer'].str.contains('TBD', na=False)])} tools need reviewer assignment
        """
        st.markdown(insights)
    
    with col2:
        st.markdown("### 📋 Recommended Actions")
        
        recommendations = """
        **Immediate (This Week):**
        1. Assign quarters to unscheduled high-priority tools
        2. Allocate budget for tools in evaluation phase
        3. Assign reviewers to unassigned tools
        
        **Short-term (This Month):**
        1. Resource planning for Q3 2025 deliveries
        2. Pilot program expansion decisions
        3. Department capacity assessment
        
        **Strategic (This Quarter):**
        1. AI tool portfolio optimization
        2. Cross-department collaboration planning
        3. Success metrics definition
        """
        st.markdown(recommendations)

def main():
    """Main dashboard function"""
    # Header
    st.markdown('<div class="main-header">🚀 AI Tool Pipeline Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Executive Strategic Overview | COO Dashboard</div>', unsafe_allow_html=True)
    st.markdown(f"*Last Updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*")
    
    # Load data
    df = load_data()
    
    # Executive KPIs
    create_executive_kpis(df)
    
    # Main roadmap heatmap
    pivot_table = create_department_quarter_heatmap(df)
    
    # Quarter breakdown with drill-down
    create_quarter_drill_down(df)
    
    # Additional analysis sections
    col1, col2 = st.columns(2)
    
    with col1:
        create_priority_analysis(df)
    
    with col2:
        create_status_pipeline(df)
    
    # Timeline visualization
    create_timeline_gantt(df)
    
    # Executive summary
    create_executive_summary(df)
    
    # Raw data table (collapsible)
    with st.expander("📊 Complete Data Table", expanded=False):
        st.dataframe(
            df[['Name', 'Department', 'Quarter', 'Priority', 'Status', 'Reviewer', 'Tool_Technology']],
            use_container_width=True
        )

if __name__ == "__main__":
    main()
