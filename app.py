import streamlit as st

# Title
st.title("🏥 Hospital Readmission Prediction and Prevention")

st.write("This demo predicts the risk of 30-day hospital readmission and suggests preventive actions.")

# Input Form
st.header("📋 Patient Information")
age = st.number_input("Age", min_value=0, max_value=120, value=65)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
condition = st.selectbox("Primary Condition", ["Heart", "Diabetes", "COPD", "Other"])
length_of_stay = st.number_input("Length of Stay (days)", min_value=1, max_value=60, value=5)
prev_admissions = st.number_input("Previous Admissions (last 1 year)", min_value=0, max_value=10, value=1)
comorbidities = st.selectbox("Comorbidities", ["None", "Hypertension", "Kidney Disease", "Asthma", "Multiple"])

# Prediction Logic (Simple Rules)
def predict_readmission(age, prev_admissions, length_of_stay, condition):
    score = 0
    if age > 60:
        score += 2
    if prev_admissions > 1:
        score += 3
    if length_of_stay > 7:
        score += 2
    if condition.lower() in ["heart", "copd", "diabetes"]:
        score += 3

    if score >= 6:
        return "🔴 High Risk", 0.82
    elif score >= 3:
        return "🟠 Medium Risk", 0.55
    else:
        return "🟢 Low Risk", 0.20

# Button to Predict
if st.button("🔍 Predict Readmission Risk"):
    risk_category, probability = predict_readmission(age, prev_admissions, length_of_stay, condition)

    st.subheader("📊 Prediction Result")
    st.write(f"**Risk Category:** {risk_category}")
    st.write(f"**Probability of Readmission:** {probability*100:.1f}%")

    # Care Plan Suggestions
    st.subheader("💡 Suggested Post-Discharge Actions")
    if "High" in risk_category:
        st.markdown("- Schedule **follow-up in 3 days**")
        st.markdown("- Arrange **home nurse visit**")
        st.markdown("- Send **daily medication reminders**")
        st.markdown("- Enroll in **telemedicine monitoring**")
    elif "Medium" in risk_category:
        st.markdown("- Schedule **follow-up in 7 days**")
        st.markdown("- Send **SMS reminders for medicines**")
    else:
        st.markdown("- Routine checkup after 30 days")
        st.markdown("- Provide standard discharge instructions")

    # Cost Savings Simulation
    st.subheader("💰 Cost Savings Estimate")
    if "High" in risk_category:
        st.success("Estimated Savings: ₹1,500 (15% reduction in penalty costs)")
    elif "Medium" in risk_category:
        st.success("Estimated Savings: ₹800 (8% reduction in penalty costs)")
    else:
        st.success("Estimated Savings: ₹300 (3% reduction in penalty costs)")
