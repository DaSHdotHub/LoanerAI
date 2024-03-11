import streamlit as st


def predict_risk(X_live, risk_features, risk_pipeline_dc_fe, risk_pipeline_model):

    # from live data, subset features related to this pipeline
    X_live_risk = X_live.filter(risk_features)

    # apply data cleaning / feat engine pipeline to live data
    X_live_risk_dc_fe = risk_pipeline_dc_fe.transform(X_live_churn)

    # predict
    risk_prediction = risk_pipeline_model.predict(X_live_churn_dc_fe)
    risk_prediction_proba = risk_pipeline_model.predict_proba(
        X_live_risk_dc_fe)
    # st.write(risk_prediction_proba)

    # Create a logic to display the results
    risk_prob = risk_prediction_proba[0, risk_prediction][0]*100
    if risk_prediction == 1:
        risk_result = 'will not'
    else:
        risk_result = 'will'

    statement = (
        f'### There is {risk_prob.round(1)}% probability '
        f'that this prospect **{risk_result} risk**.')

    st.write(statement)

    return risk_prediction
