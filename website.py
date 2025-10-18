import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import os

# Page configuration
st.set_page_config(
    page_title="SF Crime Analysis Project",
    page_icon="🚔",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .highlight-box {
        background-color: #f8f9fa;
        color:black;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .stat-box {
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem;
    }
    .team-card {
        background-color: #f5f5f5;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-header">🚔 Predicting Crime Patterns in San Francisco</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Optimizing Public Safety Resource Allocation Through Data Science</p>', unsafe_allow_html=True)

# Create tabs - Added Phase 2 EDA as fourth tab
tab1, tab2, tab3, tab4 = st.tabs(["📊 Introduction", "👥 Team", "📋 Proposal Overview", "🔍 Phase 2 – EDA"])

with tab1:
    st.markdown('<h2 class="sub-header">Research Topic & Significance</h2>', unsafe_allow_html=True)
    
    st.write("""
    Urban crime represents one of the most pressing challenges facing modern cities, directly impacting public safety, economic development, and community well-being. This research focuses on analyzing comprehensive crime data from San Francisco to develop predictive models and identify actionable patterns that can enhance public safety strategies. The significance of this study lies in its potential to transform reactive policing into proactive, data-driven law enforcement that can prevent crimes before they occur. 
    
    By leveraging machine learning algorithms and advanced statistical analysis on over 500,000 crime incidents, this research aims to uncover temporal, spatial, and categorical patterns that have remained hidden in traditional crime analysis approaches. The importance of this work extends beyond academic interest—it directly addresses the critical need for evidence-based public safety policies that can save lives, reduce victimization, and optimize the allocation of limited municipal resources. 
    
    Who benefits from this research includes police departments seeking efficient resource deployment, city planners designing safer communities, businesses making location decisions, and ultimately, every citizen whose safety and quality of life depends on effective crime prevention strategies.
    """)
    
    st.markdown('<h2 class="sub-header">Stakeholders (Who is Affected?)</h2>', unsafe_allow_html=True)
    
    st.write("""
    The primary stakeholders impacted by this research span multiple sectors of urban society. Law enforcement agencies, particularly the San Francisco Police Department, represent the most direct beneficiaries, as predictive crime models can revolutionize patrol deployment strategies, shift scheduling, and tactical resource allocation. City government officials and urban planners will gain critical insights for policy development, budget allocation decisions, and infrastructure planning that considers public safety implications. 
    
    Local businesses and commercial districts are significantly affected, as crime patterns directly influence foot traffic, property values, insurance costs, and overall economic vitality. Residents and community organizations benefit from enhanced safety awareness, enabling informed decisions about housing, transportation, and daily activities. Tourism boards and hospitality industries have substantial stakes in crime reduction, as public safety perceptions directly impact San Francisco's reputation and visitor economy. 
    
    Insurance companies and real estate developers require accurate crime risk assessments for pricing and investment decisions. The real-world implications extend to emergency services, public health organizations, and social service agencies who must respond to crime's broader societal impacts. This research addresses the fundamental challenge of making cities safer while optimizing the use of public resources in an era of budget constraints and increasing urbanization.
    """)
    
    st.markdown('<h2 class="sub-header">Existing Solutions & Gaps</h2>', unsafe_allow_html=True)
    
    st.write("""
    Current crime analysis solutions primarily rely on retrospective statistical reports and basic geographic information systems that identify where crimes have already occurred. Traditional approaches include CompStat systems used by many police departments, which provide historical crime mapping and basic trend analysis, and hot spot policing strategies that deploy officers to areas with historically high crime rates. 
    
    However, these existing solutions face significant limitations and challenges that this research addresses. Most current systems lack predictive capabilities, operating reactively rather than proactively to prevent crimes. Limited temporal analysis represents another gap, as existing tools often fail to capture complex time-based patterns including seasonal variations, day-of-week effects, and hour-specific trends that could inform strategic planning. 
    
    Inadequate integration of multiple data sources prevents comprehensive analysis that could combine crime data with socioeconomic factors, weather patterns, and special events. Insufficient granularity in crime categorization limits the effectiveness of targeted interventions, as broad crime categories may obscure specific patterns that require different prevention strategies. Current solutions also struggle with scalability and real-time processing of large datasets, limiting their utility for dynamic resource allocation decisions. The challenge of translating analytical insights into actionable operational strategies remains largely unsolved in existing systems.
    """)
    
    st.markdown('<h2 class="sub-header">Blueprint for Your Project</h2>', unsafe_allow_html=True)
    
    st.write("""
    This comprehensive data science project will employ a multi-phase analytical approach to transform raw crime data into actionable intelligence for public safety optimization. The project team will explore temporal pattern analysis using time series decomposition and seasonal trend analysis to identify when different types of crimes are most likely to occur, enabling predictive patrol scheduling and resource allocation. 
    
    Spatial analysis techniques including geographic clustering algorithms, hotspot mapping, and geospatial correlation analysis will reveal crime concentration patterns and their relationship to urban infrastructure, demographic factors, and economic indicators. Machine learning classification models will be developed to predict crime types based on temporal, spatial, and contextual features, with particular focus on distinguishing between violent and property crimes to support risk-based policing strategies. 
    
    Predictive modeling approaches will include ensemble methods such as Random Forest and Gradient Boosting, as well as deep learning techniques for complex pattern recognition in high-dimensional crime data. The team will also implement clustering analysis to identify distinct crime patterns and criminal behavior profiles that may not be apparent through traditional analysis methods. 
    
    Feature engineering will create new variables combining temporal, geographical, and categorical data to enhance model performance and interpretability. The project will consider multiple datasets including the primary San Francisco Crime dataset (500K+ records), supplemented by weather data, economic indicators, and demographic information to create a comprehensive analytical framework. 
    
    Evaluation metrics will focus on both statistical accuracy and practical utility, ensuring that models not only perform well mathematically but also provide actionable insights for real-world implementation. The final deliverable will include interactive dashboards, predictive models, and strategic recommendations that can be directly implemented by law enforcement and city planning agencies.
    """)

with tab2:
    st.markdown('<h2 class="sub-header">👥 Meet Our Team</h2>', unsafe_allow_html=True)
    
    st.info("🎯 **Team Mission Statement**\n\n*To leverage cutting-edge data science and machine learning techniques to transform public safety in San Francisco, creating predictive solutions that protect communities while optimizing resource allocation for maximum societal impact.*")
    
    st.markdown("---")
    
    # Team members (Siddhi, Sejal, Mokshith)
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("formal.jpg", width=500)
    with col2:
        st.subheader("Siddhi Muni- Data Lead")
        st.write("**Brief Bio:** I'm a builder and a problem-solver, with a particular fascination for generative AI...")
        st.write("**Team Role/Responsibilities:**\n• Data preprocessing and feature engineering\n• Leading machine learning model development and validation")
        st.write("**Portfolio Links:**\n📧 siddhimuni1302@gmail.com | 💼 [LinkedIn](www.linkedin.com/in/siddhimuni) | 🐙 [GitHub](https://github.com/siddhimuni) | 🌐 [Google Scholar](https://scholar.google.com/citations?user=pSDJxbQAAAAJ&hl=en)")

    st.markdown("---")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('<div class="team-card">', unsafe_allow_html=True)
        st.image("portfolio.jpg", caption="Sejal Hukare")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.subheader("Sejal Hukare - Pipeline and ML")
        st.write("**Brief Bio:** I'm a passionate coding and tech enthusiast...")
        st.write("**Team Role/Responsibilities:**\n• Machine learning model architecture and optimization\n• Data pipeline development and deployment")
        st.write("**Portfolio Links:**\n📧 sejal.hukare@colorado.edu | 💼 [LinkedIn](www.linkedin.com/in/sejal-hukare) | 🐙 [GitHub](https://github.com/sezol)")

    st.markdown("---")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('<div class="team-card">', unsafe_allow_html=True)
        st.image("profile (2).jpg", caption="Mokshith")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.subheader("Mokshith - Data & Feature Engineer")
        st.write("**Brief Bio:** I'm passionate about uncovering hidden patterns in data...")
        st.write("**Team Role/Responsibilities:**\n• Data preprocessing and feature engineering\n• Supporting machine learning model development")
        st.write("**Portfolio Links:**\n📧 mokshit.Palleboina@colorado.edu | 💼 [LinkedIn](www.linkedin.com/in/mokshith-sreekar-915bb6249) | 🐙 [GitHub](https://github.com/mokshith9500) | 🌐 [IEEE Explore](https://ieeexplore.ieee.org/author/220685108923536)")

    st.markdown("---")

with tab3:
    st.markdown('<h2 class="sub-header">📋 Quick Reference Summary</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3>🔬 Research Topic</h3>
        <p><strong>Predicting Crime Patterns and Optimizing Public Safety Resource Allocation in San Francisco</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h3 class="sub-header">📊 Project Scope</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Dataset & Coverage:**  
        • **Dataset:** San Francisco Crime Data  
        • **Volume:** 500,000+ incident records  
        • **Time Period:** Multi-year historical analysis  
        • **Geographic Focus:** All SF neighborhoods and police districts  
        """)
    with col2:
        st.markdown("""
        **Analysis Approach:**  
        • **Crime Categories:** Violent, property, quality-of-life violations  
        • **Methods:** Machine learning, statistical modeling  
        • **Techniques:** Geospatial analysis, predictive modeling  
        • **Output:** Interactive dashboards and recommendations  
        """)

    # Mock Data Generation
    np.random.seed(0)
    dates = pd.to_datetime(pd.date_range('2021-01-01', '2024-12-31', freq='D'))
    data_points = len(dates)
    crime_categories = ['Vehicle Theft', 'Robbery', 'Burglary', 'Assault', 'Vandalism']
    districts = ['Central', 'Southern', 'Northern', 'Bayview', 'Mission', 'Richmond', 'Ingleside', 'Park', 'Taraval', 'Tenderloin']
    df = pd.DataFrame({
        'Date': np.random.choice(dates, data_points * 5, replace=True),
        'Category': np.random.choice(crime_categories, data_points * 5, replace=True),
        'District': np.random.choice(districts, data_points * 5, replace=True),
        'Incidents': np.random.randint(1, 10, data_points * 5)
    })

    st.markdown("### Interactive Crime Dashboard (Mock Data)")
    st.markdown('<div class="text-block">Use the sliders and filters below to explore how crime trends change over time, by category, and by district.</div>', unsafe_allow_html=True)
    col_filters1, col_filters2 = st.columns(2)
    with col_filters1:
        selected_years = st.slider("Select Year Range:", 2021, 2024, (2022, 2024))
        selected_categories = st.multiselect("Select Crime Categories:", options=crime_categories, default=crime_categories)
    with col_filters2:
        selected_districts = st.multiselect("Select Districts:", options=districts, default=districts)
    filtered_df = df[
        (df['Date'].dt.year >= selected_years[0]) &
        (df['Date'].dt.year <= selected_years[1]) &
        (df['Category'].isin(selected_categories)) &
        (df['District'].isin(selected_districts))
    ]

    # Display statistics
    st.markdown('<h3 class="sub-header">Key Statistics</h3>', unsafe_allow_html=True)
    col_stats1, col_stats2, col_stats3 = st.columns(3)
    with col_stats1:
        st.metric("Total Incidents (in range)", f"{filtered_df['Incidents'].sum():,}")
    with col_stats2:
        st.metric("Average Daily Incidents", f"{filtered_df['Incidents'].sum() / (filtered_df['Date'].nunique()):.2f}")
    with col_stats3:
        st.metric("Most Common Crime", filtered_df['Category'].mode()[0] if not filtered_df.empty else "N/A")

    # Crime Trends Over Time
    st.markdown('<h3 class="sub-header">Crime Trends Over Time</h3>', unsafe_allow_html=True)
    trend_data = filtered_df.groupby(filtered_df['Date'].dt.to_period('M'))['Incidents'].sum().reset_index()
    trend_data['Date'] = trend_data['Date'].astype(str)
    fig_time = px.line(trend_data, x='Date', y='Incidents', title='Monthly Crime Incidents Trend')
    st.plotly_chart(fig_time, use_container_width=True)

    # Crime Distribution by District
    st.markdown('<h3 class="sub-header">Crime Distribution by District</h3>', unsafe_allow_html=True)
    district_data = filtered_df.groupby('District')['Incidents'].sum().reset_index()
    fig_district = px.bar(district_data, x='District', y='Incidents', title='Total Incidents by District')
    st.plotly_chart(fig_district, use_container_width=True)

    # Key Research Questions
    st.markdown('<h3 class="sub-header">❓ Key Research Questions</h3>', unsafe_allow_html=True)
    questions = [
        "🕐 Temporal Analysis: When do specific crime types peak?",
        "📍 Spatial Analysis: Where are crime hotspots located and why?",
        "🔮 Predictive Modeling: Can we predict crime type and likelihood by location/time?",
        "🚔 Resource Optimization: How should police allocate patrol resources?",
        "🏘️ Comparative Analysis: How do different neighborhoods compare in crime patterns?",
        "🔗 Causal Relationships: What factors drive crime rate fluctuations?"
    ]
    for i, question in enumerate(questions, 1):
        st.markdown(f"{i}. {question}")

    # Phase 2 Conclusion
    st.markdown('<h2 class="sub-header">📌 Phase 2 Conclusion</h2>', unsafe_allow_html=True)
    st.write("""
    Phase 2 focused on exploring and understanding the San Francisco crime dataset to extract meaningful insights across time, space, and crime categories.

    **Key Insights:**
    - **Spatial Concentration:** Mission, Tenderloin, and SoMa are high-crime neighborhoods.
    - **Temporal Patterns:** Peak incidents occur on Fridays and Wednesdays, primarily between 12 PM–7 PM.
    - **Dominant Crime Types:** Larceny/Theft and vehicle-related crimes dominate.
    - **District-Level Patterns:** Southern, Mission, and Central districts report the highest number of incidents.
    - **Resolution Insights:** Many cases result in citations or arrests, while a notable number remain open or active.

    This analysis establishes a clean, structured, and interpretable dataset, enabling stakeholders to explore trends and form the foundation for predictive modeling and strategic recommendations in Phase 3.
    """)

# Phase 2 EDA Tab
with tab4:
    st.markdown('<h2 class="sub-header">🧠 Phase 2 – Exploratory Data Analysis (EDA)</h2>', unsafe_allow_html=True)

    st.write("""
    Phase 2 focuses on **deep exploratory data analysis (EDA)** to extract meaningful insights
    from the San Francisco crime dataset. This phase emphasizes cleaning, transformation,
    and visualization to identify underlying trends and relationships between crime variables.
    """)

    # --- Data Cleaning & Transformation ---
    st.markdown('<h3 class="sub-header">🧹 Data Cleaning & Transformation</h3>', unsafe_allow_html=True)
    st.write("""
    Before analysis, the dataset underwent essential preprocessing steps:
    - **Missing Values Handling:** Removed or imputed missing records.
    - **Duplicate Removal:** Cleaned redundant entries ensuring unique crime incidents.
    - **Feature Refinement:** Dropped irrelevant columns and encoded categorical data.
    - **Outlier Detection:** Identified anomalies using z-scores and IQR methods.
    - **Normalization:** Standardized data to improve model consistency.
    - **Date-Time Extraction:** Extracted features like `Year`, `Month`, `Day of Week`, and `Hour`.
    """)

    # --- Correlation Heatmaps ---
    st.markdown('<h3 class="sub-header">📊 Correlation Analysis</h3>', unsafe_allow_html=True)
    for img_name, caption in [
        ("coorelation_heatmap", "Correlation Heatmap (Before Cleaning)"),
        ("coorelation_heatmap_cleaned", "Correlation Heatmap (After Cleaning)")
    ]:
        if os.path.exists(f"{img_name}.png"):
            st.image(f"{img_name}.png", caption=caption, use_container_width=True)
        else:
            st.warning(f"⚠️ {img_name}.png not found in directory.")

    st.write("""
    The correlation heatmaps help in identifying **relationships between variables**
    and highlight **redundant or highly correlated features** that can be removed
    to improve model interpretability and reduce overfitting.
    """)

    # --- Visualization Analysis ---
    st.markdown('<h3 class="sub-header">📈 Visualization Insights</h3>', unsafe_allow_html=True)
    st.write("""
    The following visualizations represent the core findings of our EDA process.
    Each chart uncovers temporal, spatial, and categorical crime patterns.
    """)

    visualizations = [
        ("crime_type_distribution", "Crime Type Distribution",
         "Displays frequency of different crime categories, showing dominance of larceny/theft and vehicle crimes."),
        ("monthly_trend", "Monthly Trend of Crimes",
         "Shows seasonal variations in crime rates across different months."),
        ("day_of_week", "Crimes by Day of the Week",
         "Highlights how crime frequency peaks around Fridays and weekends."),
        ("hourly_pattern", "Hourly Crime Pattern",
         "Depicts the time-of-day effect — showing concentration between 12 PM and 7 PM."),
        ("neighborhood_hotspots", "Neighborhood Crime Hotspots",
         "Displays areas with highest incident density — Tenderloin, Mission, and SoMa."),
        ("district_comparison", "District-Level Comparison",
         "Compares total incidents across all SF police districts."),
        ("wordcloud", "Crime Type Wordcloud",
         "Visual representation of the most frequent crime types using text prominence.")
    ]

    for img_name, title, desc in visualizations:
        st.markdown(f'<h4 style="color:#1f77b4;">📍 {title}</h4>', unsafe_allow_html=True)
        if os.path.exists(f"{img_name}.png"):
            st.image(f"{img_name}.png", caption=title, use_container_width=True)
        else:
            st.warning(f"⚠️ {img_name}.png not found.")
        st.write(desc)
        st.markdown("---")

    # --- Phase 2 Summary ---
    st.markdown('<h3 class="sub-header">📌 Phase 2 Summary & Conclusion</h3>', unsafe_allow_html=True)
    st.write("""
    Phase 2 provided valuable insights into crime behavior across spatial, temporal, and categorical dimensions.

    **Key Insights:**
    - **Spatial Concentration:** Mission, Tenderloin, and SoMa remain high-crime neighborhoods.
    - **Temporal Patterns:** Crime peaks on Fridays and Wednesdays, primarily between 12 PM–7 PM.
    - **Dominant Crime Types:** Larceny/Theft and vehicle-related crimes dominate incident counts.
    - **District Patterns:** Southern, Mission, and Central districts record the most cases.
    - **Resolution Rates:** A notable percentage of cases remain unresolved, indicating improvement opportunities.

    These insights lay a solid foundation for **Phase 3**, which will focus on **predictive modeling,
    feature importance analysis, and resource allocation optimization**.
    """)

    st.success("✅ Phase 2 EDA successfully completed and integrated with visual insights.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>🔒 <strong>Data Science for Public Safety</strong> | Transforming Crime Analysis Through Machine Learning</p>
    <p>San Francisco Crime Prediction Project • 2024</p>
</div>
""", unsafe_allow_html=True)