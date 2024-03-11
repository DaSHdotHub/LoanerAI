import plotly.express as px
import numpy as np
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import load_risk_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_german_credit_study_body():

    # load data
    df = load_risko_data()

    # hard copied from risk customer study notebook
    vars_to_study = [col for col in df.columns if col != 'Risk']

    st.write("### German Credit Data Study")
    st.info(
        f"* An organization is interested in understanding the patterns from the applicant base "
        f"so that the client can learn the most relevant variables correlated "
        f"to an applicant.")

    # inspect data
    if st.checkbox("Inspect Applicants"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to Risk levels. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # Text based on "G1_GermanCreditData" notebook - "Conclusions" section
    st.info(
        f"The analysis of correlations within the dataset has primarily revealed only weak correlations. "
        f"However, a closer look at both bi-variate and multi-variate analyses leads us to the following assumptions:\n\n"
        f"* **Homeownership and Loan Applications:** Homeowners are more likely to take out loans than renters or "
        f"those without rental expenses. This could be attributed to homeowners feeling more financially secure or "
        f"needing loans for home maintenance and improvements.\n"
        f"* **Purpose of Loans - Cars:** A notable number of loans are taken for purchasing vehicles, indicating the "
        f"popularity of car loans. This could be due to the essential role of cars in personal transportation or attractive "
        f"financing options available for these purchases.\n"
        f"* **Savings Accounts and Loan Behavior:** Individuals with smaller savings accounts are more inclined to apply "
        f"for loans, possibly due to greater financial needs. Conversely, those with larger savings tend to apply for fewer "
        f"loans and have a higher repayment rate, suggesting better financial stability and more prudent borrowing and "
        f"repayment practices."
    )

    st.markdown("#### Conclusion from Hypothesis 1")
    st.markdown(
        "A positive coefficient for age, such as 0.0291, implies that as individuals age, they are slightly more likely to "
        "be perceived as having a lower risk of defaulting on loans. This supports the notion that older applicants might "
        "be considered safer bets for lenders. Essentially, the older you are, the better your chances might be of being "
        "deemed a good risk for a loan, although this effect appears to be relatively modest."
    )

    st.markdown("#### Conclusions from Hypothesis 2")
    st.markdown(
        "An accuracy of, for example, 0.705 means that the logistic regression model correctly predicted the risk classification "
        "for approximately 70.5% of the test instances. In the realm of credit risk assessment, this accuracy level indicates "
        "how effectively the model can classify applicants into 'good' or 'bad' credit risks based on their savings and checking "
        "account balances. Further validation of this hypothesis could be achieved through an ANOVA test or other statistical methods."
    )

    # Code copied from "G1_GermanCreditData" notebook - "EDA on selected variables" section
    df_eda = df.filter(vars_to_study + ['Risk'])

    # Individual plots per variable
    if st.checkbox("Risk per Variable"):
        risk_per_variable(df_eda)

    # Parallel plot
    if st.checkbox("Parallel Plot"):
        st.write(
            f"* Information in yellow indicates the profile from a defaulted applicant")
        parallel_plot_risk(df_eda)


# function created using "G1_GermanCreditData" notebook code - "Variables Distribution by Risk" section
def risk_per_variable(df_eda):
    target_var = 'Risk'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical(df_eda, col, target_var)


# code copied from "G1_GermanCreditData" notebook - "Variables Distribution by Risk" section
def plot_categorical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var,
                  order=df[col].value_counts().index)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


# code copied from "G1_GermanCreditData" notebook - "Variables Distribution by Risk" section
def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()
