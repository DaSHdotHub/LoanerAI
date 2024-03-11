import streamlit as st

def page_summary_body():
    st.title("LoanerAI Project Summary")

    st.image('src/images/logo.webp',
        use_column_width='auto')

    # Quick Project Summary
    st.write("### Quick Project Summary")
    st.info(
        "**Project Overview**\n\n"
        "LoanerAI is designed to evaluate loan applications using machine learning techniques. "
        "The aim is to assess whether an applicant is eligible for a loan based on the risk of default. "
        "This process involves data collection, analysis, cleaning, feature engineering, model development, and evaluation."
    )

    # Dataset Summary
    st.write("### Dataset Summary")
    st.write(
        "The dataset comprises various features that help in assessing the risk associated with loan applicants. "
        "Here is a quick overview of the dataset variables:"
    )
    st.table(data={
        "Variable": ["Age", "Sex", "Job", "Housing", "Saving accounts", "Checking account", "Credit amount", "Duration", "Purpose", "Risk"],
        "Meaning": ["Applicant age", "Applicant gender", "Applicant job level", "Applicant living situation", "Applicant savings", "Applicant has dependents or not", "Applied loan", "Applied loan period", "Loan purpose", "Loan risk assessment"],
        "Units": ["numerical", "categorical: male, female", "numeric: 0-3", "categorical: own, rent, free", "categorical: little, moderate, quite rich, rich", "numerical", "numerical", "numerical: 0-72", "categorical: various", "Value target - Good or Bad Risk"]
    })

    # Project Documentation Link
    st.write(
        "* For additional information, please visit and **read** the "
        "[Project README file](https://github.com/DaSHdotHub/LoanerAI)."
    )

    # Business Requirements
    st.write("### Business Requirements")
    st.success(
        "The project is guided by the following business requirements:\n\n"
        "* Requirement 1: Improve Loan Approval Process.\n"
        "* Requirement 2: Identify Key Factors Influencing Credit Risk.\n\n"
        "These requirements ensure that the project aligns with the strategic goals and addresses the specific needs of evaluating loan applications efficiently and accurately."
    )

    # Project Course
    st.write("### Project Course")
    st.info(
        "**1. Data Collection**\n\n"
        "The initial phase involves gathering data relevant to loan applications. This includes demographic, financial, and employment information of applicants.\n\n"
        "**2. Data Study**\n\n"
        "This phase focuses on understanding the dataset's characteristics, including distribution of variables, presence of missing values, and potential correlations among variables.\n\n"
        "**3. Data Cleaning**\n\n"
        "Data cleaning efforts aim to address issues like missing values, outliers, and incorrect data entries to improve the quality of the dataset for analysis.\n\n"
        "**4. Feature Engineering**\n\n"
        "Feature engineering involves creating new variables from existing ones to better capture the nuances of the loan application process and improve the model's predictive power.\n\n"
        "**5. Model Creation and Evaluation**\n\n"
        "The final phase involves developing a machine learning model to predict loan eligibility based on the cleaned and engineered dataset. Models are evaluated based on their accuracy, precision, and recall, among other metrics."
    )

    # Hypotheses
    st.write("### Hypotheses")
    st.write(
        "Several hypotheses guide the analysis and modeling efforts in this project, including:\n\n"
        "* Hypothesis 1: Age and Credit Risk.\n"
        "* Hypothesis 2: Relationship Between Job Skill Level and Credit Risk.\n"
        "* Hypothesis 3: Impact of Savings and Checking Account Balances on Credit Risk. \n\n"
        "These hypotheses are tested through exploratory data analysis and model evaluation to inform the project's direction and conclusions."
    )

    # Concluding Remarks
    st.write("### Concluding Remarks")
    st.markdown(
        "LoanerAI aims to streamline the loan approval process by leveraging machine learning to accurately assess applicant risk. "
        "Through careful analysis and model development, this project seeks to improve the efficiency and reliability of loan issuance."
    )