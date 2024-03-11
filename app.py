import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_german_credit_study import page_german_credit_study_body
# from app_pages.page_applicant import page_applicant_body
# from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_risk import page_predict_risk_body

app = MultiPage(app_name= "LoanerAI") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("German Credit Data Study", page_german_credit_study_body)
# app.add_page("Applicant Risk calculator", page_applicant_body)
# app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Applicant Risk", page_predict_risk_body)


app.run() # Run the  app
