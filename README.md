## Solving the Problems of Jaya Jaya Maju Institute

### Business Understanding

**Jaya Jaya Institute**, a higher education institution operating since 2000, is currently facing serious challenges due to the high number of students dropping out before completing their academic programs. This issue not only threatens the credibility and reputation of the institution but also significantly impacts the students' futures. Considering the importance of academic success for both individual development and institutional sustainability, the management requires a proactive, data-driven approach to anticipate dropout risks as early as possible. This will enable the provision of proper support and guidance to reduce student dropout prevalence.

### Business Problems

* High student dropout rate.
* Lack of a comprehensive monitoring platform to detect potential at-risk students early and identify dropout trends.
* Absence of a predictive system to forecast student status using academic data and personal information such as marital status, age, financial background, etc.

### Project Scope

* Analyze and identify the main factors causing student dropout.
* Build a predictive system using Machine Learning to predict dropout risk based on the most highly correlated factors.
* Develop an interactive dashboard to monitor trends using historical student data.

**Data Sources**:

* [Dicoding GitHub Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)
* [UCI Machine Learning - Predict Students Dropout and Academic Success](https://doi.org/10.24432/C5MC89)

Environment Setup:

```
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt

# Run the prediction model
streamlit run app.py
```
---

### Business Dashboard

The student dropout analysis dashboard developed using **Looker Studio** is an integrated data visualization system specifically designed to monitor and analyze student academic conditions at Jaya Jaya Institute. This dashboard focuses on identifying the factors that influence student dropout rates and provides deep insights to support strategic decision-making in academic management.

The main goal of this dashboard is to offer comprehensive visibility into student profiles, dropout patterns, and contributing factors to academic success or failure.

1. **Institutional Overview (Key Metrics)**
   The dashboard displays 4 key metrics that give an overall picture of the institution's condition:

   * **Total Students**: 3,630 active students
   * **Average Age**: 23.46 years
   * **Average Dropout Rate**: 0.39 (39% dropout rate)
   * **Average Graduation Rate**: 0.61 (61% graduation rate)

2. **Student Status Analysis**
   **Dropout vs Graduate Distribution** shows the comparison between students who graduated (2,209 students) and those who dropped out (1,421 students), providing a baseline for evaluating institutional success.

3. **Financial Factor Analysis**
   **Dropout Distribution by Scholarship Status** analyzes the correlation between scholarship status and dropout rate:

   * Without scholarship: 1,374 graduated vs 1,287 dropped out
   * With scholarship: 835 graduated vs 134 dropped out

4. **Academic Analysis**
   **Top 5 Programs with Highest Dropout Rates** identifies study programs needing special attention:

   * Biofuel Production Technologies: 88.89%
   * Informatics Engineering: 86.79%
   * Equinaculture: 65%
   * Management (Evening Attendance): 63.55%
   * Basic Education: 59.86%

5. **Demographic Analysis**

   * **Dropout Distribution by Average Grades**: Compares students with high grades (748 dropouts) vs low grades (673 dropouts)
   * **Dropout Rate by Age Category**: Shows that students in the "Yes" age category have 3,144 active status compared to 466 in the "No" category

Dashboard Link: [Student Status Analysis Dashboard](https://lookerstudio.google.com/reporting/dbae61fc-6a2e-48fb-a4bd-b5f44fb0a5c3)
![image](nurrizkyarumjatmiko-dashboard.jpg)

---

### Main Functions of the Dashboard:

1. **Integrated Filtering System (Global Control)**
   This control feature allows users to filter data based on key parameters such as **Course**, **Marital Status**, **Attendance**, **Gender**, and **Academic Status**. It provides flexibility for **academic staff** and **management** to perform in-depth analysis of specific student segments, compare group performances, and identify specific patterns across all dashboard components in real time.

2. **Key Performance Indicator Dashboard (KPI)**
   This component serves as the information hub displaying the institution’s key performance indicators, including:

   * **Total Active Students**: **3,630**
   * **Average Student Age**: **23.46** years
   * **Dropout Rate**: **0.39** (39% dropped out)
   * **Graduation Rate**: **0.61** (61% graduated)

   These metrics provide a comprehensive view of the institution’s academic status and serve as the main reference for evaluating performance.

3. **Critical Dropout Factor Analysis**
   The dashboard presents deep visualizations of the critical factors affecting student dropout rates, such as:

   * **Scholarship Impact**: Shows significant correlation between scholarship reception and academic success
   * **Program Analysis**: Identifies 5 programs with the highest dropout rates
   * **Demographic Factors**: Analyzes the relationship between age category and academic status
   * **Academic Grade Correlation**: Evaluates the connection between average grades and dropout rate

   This analysis helps management understand the root causes of dropout and identify students at high risk.

4. **Comprehensive Distribution Visualization**
   This feature shows the proportional composition and distribution of students based on various critical dimensions:

   * **Academic Status Distribution**: Comparison between graduates (2,209) and dropouts (1,421)
   * **Scholarship-Based Segmentation**: Distribution of graduates vs dropouts among scholarship recipients and non-recipients
   * **Grade-Based Classification**: Comparison of dropout rates between students with high vs low grades
   * **Age Categorization**: Analysis of student distribution based on age groups and academic status

   These visualizations allow management to see the relative contribution of each segment to the overall dropout rate, identify demographic trends needing special attention, and design targeted intervention strategies for different student groups.

### Running the Prediction System Prototype

The student status prediction system is built using a **Random Forest** algorithm with an accuracy of **90.72%** based on evaluation results. The prototype's main function is to predict a student’s status (dropout or graduate) based on demographic data including personal, academic, and financial information. Below is the link to access the prediction system via **Streamlit** or **run it locally**.

**Prototype Link:**
[Student Predictions System Streamlit App](https://dashboard-prediction-students-performance-dataset.streamlit.app/)

**Run the Prototype Locally:**

```bash
streamlit run app.py
```

---

### Conclusion

**Key Achievements**:

1. **Accurate Prediction Model**
   The project utilized the **Random Forest** machine learning model, achieving the highest accuracy of **90.72%** in predicting student status, allowing early detection of students at risk of dropping out with high confidence.

2. **Key Factors Influencing Dropout**
   Based on the **Feature Importance** from the Random Forest model, the main factors affecting dropout are: **UKT payment status**, **scholarship status**, **qualification scores**, **age group**, **study program**, **semester grades (1-2)**, **failed subjects**, and **passed subjects**. These findings provide strategic insight for targeted interventions.

3. **Prediction System and Monitoring Dashboard**
   The machine learning model shows good performance in predicting student status. The interactive dashboard provides real-time visualizations to support effective monitoring.

---

### Recommended Action Items

1. **Expand Scholarship and Financial Support Programs**
   Increase scholarship allocation and implement flexible UKT (tuition fee) payment systems. Scholarship recipients have a dropout rate of only 13.8% compared to 48.4% for non-recipients. Introduce emergency financial aid programs for students facing sudden financial hardship.

2. **Targeted Interventions for High-Risk Study Programs**
   Prioritize improvements in study programs with the highest dropout rates: Biofuel Production Technologies (88.89%) and Informatics Engineering (86.79%). Strategies include curriculum revisions, intensive mentoring programs, and better lab or practical facilities.

3. **Integrated Academic Support Programs**
   Implement remedial programs for low-performing students, study skills workshops for early semesters, and one-on-one academic coaching. Provide peer learning groups and easily accessible academic counseling services.
