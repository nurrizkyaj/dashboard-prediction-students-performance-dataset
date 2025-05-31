# Dashboard for predicting student graduation
import streamlit as st
import pandas as pd
import joblib
import pickle
from sklearn.preprocessing import StandardScaler
from datetime import datetime
from typing import Dict, List, Any

# Configuration
CONFIG = {
    'MODEL_PATH': './models/random_forest_model.pkl',
    'PREPROCESSING_PATH': './models/preprocessing.pkl',
    'TARGET_COLUMN': 'Status'
}

# Data mappings
GENDER_OPTIONS = {'Male': 1, 'Female': 0}

MARITAL_STATUS_OPTIONS = {
    'Single': 1,
    'Married': 2,
    'Widower': 3,
    'Divorced': 4,
    'Facto Union': 5,
    'Legally Separated': 6
}

APPLICATION_MODE_OPTIONS = {
    '1st Phase - General Contingent': 1,
    '1st Phase - Azores Island': 5,
    '1st Phase - Madeira Island': 16,
    '2nd Phase - General Contingent': 17,
    '3rd Phase - General Contingent': 18,
    'Ordinance No. 612/93': 2,
    'Ordinance No. 854-B/99': 10,
    'Ordinance 533-A/99 - Item B2': 26,
    'Ordinance 533-A/99 - Item B3': 27,
    'International Student': 15,
    'Over 23 Years Old': 39,
    'Transfer Student': 42,
    'Course Change': 43,
    'Higher Course Holders': 7,
    'Diploma Holders': 53,
    'Specialization Holders': 44,
    'Institution Change': 51,
    'International Change': 57,
}

class StudentPredictor:
    """Class to handle student prediction logic"""
    
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.reference_data = None
        
    def load_model(self) -> bool:
        """Load the trained model"""
        try:
            self.model = joblib.load(CONFIG['MODEL_PATH'])
            return True
        except FileNotFoundError:
            st.error("Model file not found. Please ensure model_rf.joblib exists.")
            return False
        except Exception as e:
            st.error(f"Error loading model: {str(e)}")
            return False
    
    def load_reference_data(self) -> bool:
        """Load reference data from pickle file for scaling"""
        try:
            with open(CONFIG['PREPROCESSING_PATH'], 'rb') as f:
                self.reference_data = pickle.load(f)
            
            # Remove target column if it exists
            if CONFIG['TARGET_COLUMN'] in self.reference_data.columns:
                self.reference_data = self.reference_data.drop(columns=[CONFIG['TARGET_COLUMN']])
            
            st.success(f"Loaded reference data: {self.reference_data.shape[0]} samples, {self.reference_data.shape[1]} features")
            return True
        except FileNotFoundError:
            st.error("Preprocessing data file not found. Please ensure preprocessing.pkl exists in ./models/ directory.")
            return False
        except Exception as e:
            st.error(f"Error loading reference data: {str(e)}")
            return False
    
    def prepare_data(self, student_data: Dict[str, Any]) -> pd.DataFrame:
        """Prepare and scale student data for prediction"""
        # Create DataFrame with correct column order
        feature_columns = [
            'Marital_status', 'Application_mode', 'Previous_qualification_grade',
            'Admission_grade', 'Displaced', 'Debtor', 'Tuition_fees_up_to_date',
            'Gender', 'Scholarship_holder', 'Age_at_enrollment',
            'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_approved',
            'Curricular_units_1st_sem_grade', 'Curricular_units_2nd_sem_enrolled',
            'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
            'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations'
        ]
        
        # Create student DataFrame
        student_df = pd.DataFrame([student_data], columns=feature_columns)
        
        # Combine with reference data for proper scaling
        combined_data = pd.concat([student_df, self.reference_data], ignore_index=True)
        
        # Scale the data
        scaled_data = self.scaler.fit_transform(combined_data)
        
        # Return only the student data (first row)
        return scaled_data[[0]]
    
    def predict(self, scaled_data) -> int:
        """Make prediction using the loaded model"""
        if self.model is None:
            raise ValueError("Model not loaded")
        return self.model.predict(scaled_data)[0]

def create_personal_info_form() -> Dict[str, Any]:
    """Create form for personal information"""
    st.subheader("📋 Personal Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox(
            "Gender",
            options=list(GENDER_OPTIONS.keys()),
            key="gender"
        )
        
        age = st.number_input(
            "Age at Enrollment",
            min_value=17,
            max_value=70,
            value=20,
            key="age"
        )
    
    with col2:
        marital_status = st.selectbox(
            "Marital Status",
            options=list(MARITAL_STATUS_OPTIONS.keys()),
            key="marital"
        )
        
        application_mode = st.selectbox(
            "Application Mode",
            options=list(APPLICATION_MODE_OPTIONS.keys()),
            key="application"
        )
    
    return {
        'gender': GENDER_OPTIONS[gender],
        'age': age,
        'marital_status': MARITAL_STATUS_OPTIONS[marital_status],
        'application_mode': APPLICATION_MODE_OPTIONS[application_mode]
    }

def create_academic_info_form() -> Dict[str, Any]:
    """Create form for academic information"""
    st.subheader("🎓 Academic Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        prev_grade = st.number_input(
            "Previous Qualification Grade",
            min_value=0,
            max_value=200,
            value=100,
            help="Grade range: 0-200"
        )
        
        admission_grade = st.number_input(
            "Admission Grade",
            min_value=0,
            max_value=200,
            value=100,
            help="Grade range: 0-200"
        )
    
    with col2:
        first_sem_enrolled = st.number_input(
            "1st Semester - Units Enrolled",
            min_value=0,
            max_value=26,
            value=6
        )
        
        first_sem_approved = st.number_input(
            "1st Semester - Units Approved",
            min_value=0,
            max_value=26,
            value=6
        )
    
    first_sem_grade = st.number_input(
        "1st Semester - Average Grade",
        min_value=0,
        max_value=20,
        value=10,
        help="Grade range: 0-20"
    )
    
    return {
        'prev_qualification_grade': prev_grade,
        'admission_grade': admission_grade,
        'first_sem_enrolled': first_sem_enrolled,
        'first_sem_approved': first_sem_approved,
        'first_sem_grade': first_sem_grade
    }

def create_second_semester_form() -> Dict[str, Any]:
    """Create form for second semester information"""
    st.subheader("📚 Second Semester Performance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        second_sem_enrolled = st.number_input(
            "2nd Semester - Units Enrolled",
            min_value=0,
            max_value=23,
            value=6
        )
        
        second_sem_approved = st.number_input(
            "2nd Semester - Units Approved",
            min_value=0,
            max_value=20,
            value=6
        )
        
        second_sem_evaluations = st.number_input(
            "2nd Semester - Evaluations",
            min_value=0,
            max_value=33,
            value=6
        )
    
    with col2:
        second_sem_grade = st.number_input(
            "2nd Semester - Average Grade",
            min_value=0,
            max_value=20,
            value=10
        )
        
        second_sem_no_eval = st.number_input(
            "2nd Semester - Units Without Evaluation",
            min_value=0,
            max_value=12,
            value=0
        )
    
    return {
        'second_sem_enrolled': second_sem_enrolled,
        'second_sem_approved': second_sem_approved,
        'second_sem_evaluations': second_sem_evaluations,
        'second_sem_grade': second_sem_grade,
        'second_sem_no_eval': second_sem_no_eval
    }

def create_financial_status_form() -> Dict[str, Any]:
    """Create form for financial and status information"""
    st.subheader("💰 Financial & Status Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        scholarship = st.checkbox("Scholarship Holder", value=False)
        tuition_updated = st.checkbox("Tuition Fees Up to Date", value=True)
    
    with col2:
        displaced = st.checkbox("Displaced Person", value=False)
        debtor = st.checkbox("Debtor Status", value=False)
    
    return {
        'scholarship': int(scholarship),
        'tuition_updated': int(tuition_updated),
        'displaced': int(displaced),
        'debtor': int(debtor)
    }

def combine_form_data(**form_sections) -> Dict[str, Any]:
    """Combine all form sections into final data structure"""
    personal = form_sections['personal']
    academic = form_sections['academic']
    second_sem = form_sections['second_semester']
    financial = form_sections['financial']
    
    return {
        'Marital_status': personal['marital_status'],
        'Application_mode': personal['application_mode'],
        'Previous_qualification_grade': academic['prev_qualification_grade'],
        'Admission_grade': academic['admission_grade'],
        'Displaced': financial['displaced'],
        'Debtor': financial['debtor'],
        'Tuition_fees_up_to_date': financial['tuition_updated'],
        'Gender': personal['gender'],
        'Scholarship_holder': financial['scholarship'],
        'Age_at_enrollment': personal['age'],
        'Curricular_units_1st_sem_enrolled': academic['first_sem_enrolled'],
        'Curricular_units_1st_sem_approved': academic['first_sem_approved'],
        'Curricular_units_1st_sem_grade': academic['first_sem_grade'],
        'Curricular_units_2nd_sem_enrolled': second_sem['second_sem_enrolled'],
        'Curricular_units_2nd_sem_evaluations': second_sem['second_sem_evaluations'],
        'Curricular_units_2nd_sem_approved': second_sem['second_sem_approved'],
        'Curricular_units_2nd_sem_grade': second_sem['second_sem_grade'],
        'Curricular_units_2nd_sem_without_evaluations': second_sem['second_sem_no_eval']
    }

def display_prediction_result(prediction: int) -> None:
    """Display prediction result with appropriate styling"""
    if prediction == 1:
        st.success("🎓 **Prediction: GRADUATE**")
        st.balloons()
        st.info("The model predicts that this student is likely to graduate successfully.")
    else:
        st.error("⚠️ **Prediction: DROPOUT**")
        st.warning("The model predicts that this student is at risk of dropping out. Consider providing additional support.")

def create_sidebar_info():
    """Create sidebar with application information"""
    st.sidebar.title("ℹ️ About")
    st.sidebar.info(
        """
        This application predicts student graduation likelihood based on:
        - Personal demographics
        - Academic performance
        - Financial status
        - Course engagement metrics
        
        Fill in all the required information and click 'Predict' to get results.
        """
    )
    
    st.sidebar.title("📊 Model Info")
    st.sidebar.write("**Algorithm:** Random Forest")
    st.sidebar.write("**Data Source:** Dataset Jaya Jaya Institute Student")
    st.sidebar.write("**Features:** Correlated features (threshold ≥ 0.1)")
    st.sidebar.write("**Output:** Graduate/Dropout prediction")
    st.sidebar.write("**Data Balancing:** SMOTE applied")

def main():
    """Main application function"""
    # Page configuration
    st.set_page_config(
        page_title="Student Success Predictor",
        page_icon="🎓",
        layout="wide"
    )
    
    # Header
    st.title("🎓 Student Success Prediction System")
    st.markdown("---")
    
    # Sidebar
    create_sidebar_info()
    
    # Initialize predictor
    predictor = StudentPredictor()
    
    # Load model and reference data
    if not (predictor.load_model() and predictor.load_reference_data()):
        st.stop()
    
    # Create form
    with st.form("student_prediction_form"):
        # Form sections
        personal_data = create_personal_info_form()
        st.markdown("---")
        
        academic_data = create_academic_info_form()
        st.markdown("---")
        
        second_semester_data = create_second_semester_form()
        st.markdown("---")
        
        financial_data = create_financial_status_form()
        st.markdown("---")
        
        # Submit button
        submitted = st.form_submit_button(
            "🔮 Predict Student Success",
            use_container_width=True,
            type="primary"
        )
    
    # Process form submission
    if submitted:
        try:
            # Combine form data
            student_data = combine_form_data(
                personal=personal_data,
                academic=academic_data,
                second_semester=second_semester_data,
                financial=financial_data
            )
            
            # Prepare data and make prediction
            with st.spinner("Making prediction..."):
                scaled_data = predictor.prepare_data(student_data)
                prediction = predictor.predict(scaled_data)
            
            # Display results
            st.markdown("---")
            st.subheader("📈 Prediction Results")
            display_prediction_result(prediction)
            
        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")
    
    # Footer
    st.markdown("---")
    current_year = datetime.now().year
    st.caption(f"© {current_year} Student Success Prediction System")

if __name__ == "__main__":
    main()