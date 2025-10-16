# 🚔 SF Crime Analysis Project  
### Predicting Crime Patterns in San Francisco & Optimizing Public Safety Resource Allocation  

Uncovering hidden patterns in crime data to help cities deploy resources effectively and improve public safety.  
Using over **500,000+ real-world incident records** from the San Francisco Open Data Portal, this project transforms reactive policing into **proactive, data-driven strategies**.

---

## 👥 Team Members  

### 🧠 **Mokshith Palleboina — Data & Feature Engineering**  
🕵️‍♂️ Passionate about uncovering hidden patterns in data and transforming raw information into actionable insights.  
Experienced in **data cleaning, preprocessing, and feature engineering**, with a focus on supporting predictive models and improving data reliability.  
📧 mokshit.palleboina@colorado.edu | 💼 [LinkedIn](www.linkedin.com/in/mokshith-sreekar-915bb6249) | 🐙 [GitHub](https://github.com/mokshith9500)

---

### 💻 **Siddhi Muni — Data Lead**  
🛠️ Builder and problem-solver, fascinated by generative AI. Leads model development to extract actionable insights from complex datasets, creating **scalable, intelligent systems**.  
📧 siddhimuni1302@gmail.com | 💼 [LinkedIn](#) | 🐙 [GitHub](#)

---

### ⚙️ **Sejal Hukare — ML & Pipeline Engineer**  
⚡ Passionate coder and tech enthusiast, skilled in **building ML pipelines** and optimizing model workflows.  
Ensures smooth data flow from **preprocessing to model deployment**.  
📧 sejal.hukare@colorado.edu | 💼 [LinkedIn](#) | 🐙 [GitHub](#)

---

## 🧩 Project Milestones  

| Phase | Title | Description |
|:------|:------|:-------------|
| 🗃️ **Phase 1** | **Data Collection & Preprocessing** | Connected to the SF OpenData API, retrieved dynamic records, and performed extensive data cleaning. Removed missing and duplicate entries, standardized data types, and validated spatial and temporal accuracy. |
| 🔍 **Phase 2** | **Exploratory Data Analysis & Feature Engineering** | Conducted statistical analysis, feature transformation, and visualization to uncover crime trends, spatial clusters, and temporal patterns. Normalized data, applied PCA for dimensionality reduction, and identified key insights for modeling. |
| 🤖 **Phase 3** | **Machine Learning Modeling & Evaluation** | *(Upcoming)* Predictive modeling to forecast crime hotspots using supervised and geospatial techniques. |
| 📊 **Phase 4** | **Dashboard & Final Presentation** | *(Upcoming)* Development of an interactive dashboard for stakeholders to visualize predictions and insights in real time. |

---

## 📊 Dataset & Coverage  

- **Source:** San Francisco Open Data Portal (SODA API)  
- **Dataset Name:** Police Department Incident Reports  
- **Volume:** 500,000+ incident records (2018–2025)  
- **Geographic Scope:** All 11 police districts in San Francisco  
- **Temporal Coverage:** 7.8 years of crime data  
- **Attributes:** Temporal, spatial, and categorical variables for predictive analytics  

---

## ⚙️ Data Transformation  

Data preprocessing and transformation were vital to ensure analytical quality and consistency:

- Removed incomplete and duplicate entries to maintain data integrity.  
- Dropped non-relevant columns (e.g., row_id, legacy codes) to reduce noise.  
- Standardized numerical and categorical features for consistent interpretation.  
- Applied **Min–Max Normalization** and **Z-score Standardization** to scale data.  
- Performed **Principal Component Analysis (PCA)** to reduce dimensionality from 11 to 4 key components while retaining ~95% variance.  

These steps produced a **structured, scalable, and analysis-ready dataset** for advanced modeling.

---

## 📈 Exploratory Data Analysis (Phase 2 Highlights)

### 🕒 Temporal Insights  
- Crime incidents **dropped sharply in 2020** during COVID-19 lockdowns and gradually increased afterward.  
- **Fridays and Wednesdays** showed the highest crime frequency, while Sundays remained the lowest.  
- Peak activity occurred between **12 PM and 7 PM**, aligning with business hours and evening transit.  

### 🗺️ Spatial Insights  
- **Mission, Tenderloin, and SoMa** emerged as consistent high-crime hotspots.  
- **Southern, Mission, and Central** districts recorded the most incidents, reflecting central business and nightlife density.  

### 🚨 Crime Type Distribution  
- **Larceny/Theft** dominated, followed by **Vehicle Theft** and **Burglary**, confirming property crime as the major challenge.  

### 📜 Resolution Outcomes  
- Many cases concluded with **Citations or Arrests**, while a significant portion remained **Open/Active**, indicating ongoing investigations.  

### 💬 Textual Analysis  
- Word cloud analysis highlighted frequent mentions of terms such as **THEFT**, **VEHICLE**, **LOCKED**, and **AUTO**, emphasizing vehicle-related offenses.  

---

## 🧠 Statistical Insights  

- Identified and removed redundant columns (IDs, codes) that lacked interpretive value.  
- Detected strong spatial relationships between **latitude, longitude, and supervisor district**, validating coherent geographic clustering.  
- Correlation heatmaps confirmed **consistent spatial dependency** among location-based attributes.  

---

## 🧭 Phase 2 Conclusion  

Phase 2 successfully established a **comprehensive understanding of San Francisco’s crime landscape** through structured analysis and visualization.  

**Key Takeaways:**  
- Data is now fully cleaned, normalized, and statistically validated.  
- Clear spatial and temporal patterns have been identified for predictive modeling.  
- The foundation is set for Phase 3, which will focus on **machine learning models to forecast crime hotspots** and **optimize public safety resources**.  

This milestone bridges raw data exploration with advanced analytics, paving the way for a **data-driven approach to crime prevention** in San Francisco.  

---

## 🧰 Tools & Technologies  

| Category | Tools Used |
|:----------|:------------|
| **Programming** | Python (Pandas, NumPy, Scikit-learn, Plotly, Matplotlib) |
| **Data Source** | SF OpenData Portal (SODA API) |
| **Visualization** | Plotly, Seaborn, WordCloud, Streamlit |
| **Version Control** | Git & GitHub |
| **Notebook** | Jupyter / Google Colab |

---

## 🔮 Next Steps  

- Implement **predictive modeling** using geospatial machine learning.  
- Evaluate model performance using RMSE, MAE, and AUC metrics.  
- Integrate results into an **interactive Streamlit dashboard** for public safety decision-making.  

---

## 🔒 Data Science for Public Safety  
Transforming Crime Analysis Through Machine Learning  
**San Francisco Crime Prediction Project • 2024**  

---

