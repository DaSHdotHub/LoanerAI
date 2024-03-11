import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_risk_data, load_pkl_file
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
    f"* The training set showed high accuracy (93%) with excellent recall on both 'Risk' (91%) and 'No Risk' (94%) classes, "
    f"demonstrating the model's ability to correctly identify both risky and safe applicants in the training phase. \n"
    f"* However, the performance on the test set dropped significantly, with an overall accuracy of 64%. Specifically, "
    f"the recall for 'Risk' and 'No Risk' classes in the test set was 0.41 and 0.76, respectively. This indicates the model's "
    f"reduced effectiveness at generalizing to new, unseen data, suggesting overfitting during the training process. \n"
    f"* The noticeable performance discrepancy between training and test sets underscores the need for model improvements. "
    f"Enhancing the model's generalization capabilities could involve techniques such as cross-validation, regularization, "
    f"and exploring different model architectures or algorithms. \n"
    f"* Given the project's focus on minimizing the risk of default by accurately identifying 'No Risk' applicants, future "
    f"efforts should also explore methods to boost the recall for 'No Risk' class in unseen data, potentially through adjusting "
    f"the model's decision threshold, employing cost-sensitive learning, or addressing class imbalance. \n"
    f"* Enhancements are indeed warranted to better align the model's performance with the project objectives, particularly "
    f"in improving its ability to generalize from training to real-world applications."
)

    # show pipelines
    st.write("---")
    st.write("#### There are 2 ML Pipelines arranged in series.")

    st.write(" * The first is responsible for data cleaning and feature engineering.")
    st.write(risk_pipe_dc_fe)

    st.write("* The second is for feature scaling and modelling.")
    st.write(risk_pipe_model)

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
