import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_telco_data, load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


def page_predict_risk_body():

    version = 'v1'
    # load needed files
    risk_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_risk/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
    risk_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_risk/{version}/clf_pipeline_model.pkl")
    risk_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_risk/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_risk/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_risk/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_risk/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_risk/{version}/y_test.csv").values

    st.write("### ML Pipeline: Predict Prospect Risk")
    # display pipeline training summary conclusions
    st.info(
        f"* The pipeline was tuned aiming for 0.80 Recall on 'No Risk' class, "
        f"since we are interested in this project in detecting a potential applicant which will default. \n"
        f"* The pipeline performance on train and test set is 0.90 and 0.85, respectively."
    )

    # show pipelines
    st.write("---")
    st.write("#### There are 2 ML Pipelines arranged in series.")

    st.write(" * The first is responsible for data cleaning and feature engineering.")
    st.write(risk_pipe_dc_fe)

    st.write("* The second is for feature scaling and modelling.")
    st.write(riskn_pipe_model)

    # show feature importance plot
    st.write("---")
    st.write("* The features the model was trained and their importance.")
    st.write(X_train.columns.to_list())
    st.image(risk_feat_importance)

    # We don't need to apply dc_fe pipeline, since X_train and X_test
    # were already transformed in the jupyter notebook (Predict Customer Risk.ipynb)

    # evaluate performance on train and test set
    st.write("---")
    st.write("### Pipeline Performance")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=risk_pipe_model,
                    label_map=["Risk", "No Risk"])
