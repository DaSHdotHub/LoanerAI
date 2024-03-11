import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Some header**\n"
        f"* An **applicant** is a person who applies for a loan.\n")

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/DaSHdotHub/LoanerAI).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"State the business requirements here:\n"
        f"* 1 - blabla.\n")
        