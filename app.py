import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('voting_classifier_model.pkl')

st.title('Student Status Prediction')

# Buat input form sesuai kolom fitur lo

Marital_status = st.number_input(
    'Marital Status (int)', min_value=0, max_value=10, value=0)
Application_mode = st.number_input(
    'Application Mode (int)', min_value=0, max_value=10, value=0)
Application_order = st.number_input(
    'Application Order (int)', min_value=0, max_value=10, value=1)
Course = st.number_input('Course (int)', min_value=0, max_value=20, value=1)
Daytime_evening_attendance = st.number_input(
    'Daytime/Evening Attendance (int)', min_value=0, max_value=10, value=0)
Previous_qualification = st.number_input(
    'Previous Qualification (int)', min_value=0, max_value=20, value=1)
Previous_qualification_grade = st.number_input(
    'Previous Qualification Grade (float)', min_value=0.0, max_value=20.0, value=10.0)
Mothers_occupation = st.number_input(
    'Mother\'s Occupation (int)', min_value=0, max_value=20, value=0)
Fathers_occupation = st.number_input(
    'Father\'s Occupation (int)', min_value=0, max_value=20, value=0)
Admission_grade = st.number_input(
    'Admission Grade (float)', min_value=0.0, max_value=20.0, value=10.0)
Displaced = st.number_input(
    'Displaced (int)', min_value=0, max_value=1, value=0)
Debtor = st.number_input('Debtor (int)', min_value=0, max_value=1, value=0)
Tuition_fees_up_to_date = st.number_input(
    'Tuition Fees Up To Date (int)', min_value=0, max_value=1, value=1)
Gender = st.number_input('Gender (int)', min_value=0, max_value=1, value=0)
Scholarship_holder = st.number_input(
    'Scholarship Holder (int)', min_value=0, max_value=1, value=0)
Age_at_enrollment = st.number_input(
    'Age At Enrollment (int)', min_value=10, max_value=100, value=20)
Curricular_units_1st_sem_credited = st.number_input(
    'Curricular Units 1st Sem Credited (int)', min_value=0, max_value=100, value=0)
Curricular_units_1st_sem_enrolled = st.number_input(
    'Curricular Units 1st Sem Enrolled (int)', min_value=0, max_value=100, value=0)
Curricular_units_1st_sem_evaluations = st.number_input(
    'Curricular Units 1st Sem Evaluations (int)', min_value=0, max_value=100, value=0)
Curricular_units_1st_sem_approved = st.number_input(
    'Curricular Units 1st Sem Approved (int)', min_value=0, max_value=100, value=0)
Curricular_units_1st_sem_grade = st.number_input(
    'Curricular Units 1st Sem Grade (float)', min_value=0.0, max_value=20.0, value=0.0)
Curricular_units_2nd_sem_credited = st.number_input(
    'Curricular Units 2nd Sem Credited (int)', min_value=0, max_value=100, value=0)
Curricular_units_2nd_sem_enrolled = st.number_input(
    'Curricular Units 2nd Sem Enrolled (int)', min_value=0, max_value=100, value=0)
Curricular_units_2nd_sem_evaluations = st.number_input(
    'Curricular Units 2nd Sem Evaluations (int)', min_value=0, max_value=100, value=0)
Curricular_units_2nd_sem_approved = st.number_input(
    'Curricular Units 2nd Sem Approved (int)', min_value=0, max_value=100, value=0)
Curricular_units_2nd_sem_grade = st.number_input(
    'Curricular Units 2nd Sem Grade (float)', min_value=0.0, max_value=20.0, value=0.0)
Curricular_units_2nd_sem_without_evaluations = st.number_input(
    'Curricular Units 2nd Sem Without Evaluations (int)', min_value=0, max_value=100, value=0)
GDP = st.number_input('GDP (float)', min_value=0.0,
                      max_value=100000.0, value=10000.0)

# Masukin ke dataframe
input_dict = {
    'Marital_status': [Marital_status],
    'Application_mode': [Application_mode],
    'Application_order': [Application_order],
    'Course': [Course],
    'Daytime_evening_attendance': [Daytime_evening_attendance],
    'Previous_qualification': [Previous_qualification],
    'Previous_qualification_grade': [Previous_qualification_grade],
    'Mothers_occupation': [Mothers_occupation],
    'Fathers_occupation': [Fathers_occupation],
    'Admission_grade': [Admission_grade],
    'Displaced': [Displaced],
    'Debtor': [Debtor],
    'Tuition_fees_up_to_date': [Tuition_fees_up_to_date],
    'Gender': [Gender],
    'Scholarship_holder': [Scholarship_holder],
    'Age_at_enrollment': [Age_at_enrollment],
    'Curricular_units_1st_sem_credited': [Curricular_units_1st_sem_credited],
    'Curricular_units_1st_sem_enrolled': [Curricular_units_1st_sem_enrolled],
    'Curricular_units_1st_sem_evaluations': [Curricular_units_1st_sem_evaluations],
    'Curricular_units_1st_sem_approved': [Curricular_units_1st_sem_approved],
    'Curricular_units_1st_sem_grade': [Curricular_units_1st_sem_grade],
    'Curricular_units_2nd_sem_credited': [Curricular_units_2nd_sem_credited],
    'Curricular_units_2nd_sem_enrolled': [Curricular_units_2nd_sem_enrolled],
    'Curricular_units_2nd_sem_evaluations': [Curricular_units_2nd_sem_evaluations],
    'Curricular_units_2nd_sem_approved': [Curricular_units_2nd_sem_approved],
    'Curricular_units_2nd_sem_grade': [Curricular_units_2nd_sem_grade],
    'Curricular_units_2nd_sem_without_evaluations': [Curricular_units_2nd_sem_without_evaluations],
    'GDP': [GDP]
}

input_df = pd.DataFrame(input_dict)

if st.button('Predict'):
    pred = model.predict(input_df)
    pred_proba = model.predict_proba(input_df)

    status_map = {0: 'Graduate', 1: 'Dropout', 2: 'Enrolled'}
    st.write(f'Prediction: **{status_map.get(pred[0], "Unknown")}**')
    st.write(f'Probabilities: {pred_proba[0]}')
