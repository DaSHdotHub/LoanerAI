import streamlit as st
import pandas as pd
from src.data_management import load_risk_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import (
    predict_risk,
)


def page_applicant_body():
    # Load predict risk files
    version = 'v1'
    risk_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_risk/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
    risk_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_risk/{version}/clf_pipeline_model.pkl")
    risk_features = (pd.read_csv(f"outputs/ml_pipeline/predict_risk/{version}/X_train.csv")
                     .columns
                     .to_list()
                     )

    st.write("### Applicant Risk-O-Meter")
    st.info(
        f"* The client is interested in determining the risk level of a given loan applicant. "
        f"This includes assessing the likelihood of default and identifying potential factors "
        f"that could influence an applicant's risk profile. Based on this analysis, strategies "
        f"can be developed to mitigate risk and support decision-making in loan approval processes."
    )
    st.write("---")

    # Generate Live Data
    X_live = DrawInputsWidgets()

    # Predict on live data
    if st.button("Run Predictive Analysis"):
        risk_prediction = predict_risk(
            X_live, risk_features, risk_pipe_dc_fe, risk_pipe_model)

        st.write(
            f"Risk Prediction: {'High Risk' if risk_prediction == 1 else 'Low Risk'}")


def DrawInputsWidgets():
    # Create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # Assuming the use of columns for layout.
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    col7, col8 = st.columns(2)
    col9, col10 = st.columns(2)

    with col1:
        age = st.number_input('Age', min_value=18,
                              max_value=100, value=30, step=1)
        X_live['Age'] = age

    with col2:
        sex = st.selectbox('Sex', ['male', 'female'])
        X_live['Sex'] = sex

    with col3:
        job = st.select_slider('Job', options=[0, 1, 2, 3], format_func=lambda x: {
                               0: 'unskilled and non-resident', 1: 'unskilled and resident', 2: 'skilled', 3: 'highly skilled'}[x])
        X_live['Job'] = job

    with col4:
        housing = st.selectbox('Housing', ['own', 'rent', 'free'])
        X_live['Housing'] = housing

    with col5:
        saving_accounts = st.selectbox(
            'Saving accounts', ['little', 'moderate', 'quite rich', 'rich'])
        X_live['Saving accounts'] = saving_accounts

    with col6:
        # Assuming checking account values are input as numeric. Adjust the range as necessary.
        checking_account = st.number_input(
            'Checking account (in DM)', min_value=0, value=500, step=100)
        X_live['Checking account'] = checking_account

    with col7:
        credit_amount = st.number_input(
            'Credit amount (in DM)', min_value=0, value=2500, step=100)
        X_live['Credit amount'] = credit_amount

    with col8:
        duration = st.number_input(
            'Duration (in months)', min_value=1, max_value=72, value=12, step=1)
        X_live['Duration'] = duration

    with col9:
        purpose = st.selectbox('Purpose', ['car', 'furniture/equipment', 'radio/TV',
                               'domestic appliances', 'repairs', 'education', 'business', 'vacation/others'])
        X_live['Purpose'] = purpose

    # st.write(X_live) can be used to display the DataFrame on the UI for debugging

    return X_live
