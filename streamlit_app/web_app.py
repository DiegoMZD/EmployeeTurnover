import streamlit as st
import joblib
import pandas as pd

# Load Model and Preprocessor
pipeline = joblib.load("p2_bagg_hyp.pkl")
# preprocessor = joblib.load('preprocessor.pkl')

st.title("Employee Turnover Prediction")

# Create input fields
stag = st.number_input("Stag", min_value = 0, max_value = 360)
gender = st.selectbox("Gender", ["f", "m"])
age = st.number_input("Age", min_value = 18, max_value = 65)
industry = st.selectbox("Industry", ["Retail", "manufacture","IT", "Banks", "etc", "Consult", "State", "Building",
                                     "PowerGeneration", "transport", "Telecom", "Mining", "Pharma", "Agriculture", "RealEstate", "HoReCa"])
profession = st.selectbox("Profession", ["HR", "IT", "Sales", "etc", "Marketing", "BusinessDevelopment", "Consult",
                                         "Commercial", "manage", "Finance", "Engineer", "Teaching", "Accounting", "Law", "PR"])
traffic = st.selectbox("Traffic", ["youjs", "empjs", "rabrecNErab", "friends", "referal", "KA", "recNErab", "advert"])
coach = st.selectbox("Coach", ["no", "yes", "my head"])
head_gender = st.selectbox("Head Gender", ["f", "m"])
greywage = st.selectbox("Greywage", ["white", "grey"])
way = st.selectbox("Way", ["bus", "car", "foot"])
extraversion = st.number_input("Extraversion", min_value = 0, max_value = 10)
independ = st.number_input("Independ", min_value = 0, max_value = 10)
selfcontrol = st.number_input("Self Control", min_value = 0, max_value = 10)
anxiety = st.number_input("Anxiety", min_value = 0, max_value = 10)
novator = st.number_input("Novator", min_value = 0, max_value = 10)

if st.button("Predict Turnover"):
    data = pd.DataFrame([[stag, gender, age, industry, profession, traffic, coach, head_gender, greywage, way, extraversion,
                          independ, selfcontrol, anxiety, novator]],
                        columns=["stag", "gender", "age", "industry", "profession", "traffic", "coach", "head_gender", "greywage",
                                 "way", "extraversion", "independ", "selfcontrol", "anxiety", "novator"])
    
    # Apply Preprocessing
    # processed_data = preprocessor.transform(data)

    # Make Prediction
    # prediction = model.predict(processed_data)[0]
    prediction = pipeline.predict(data)[0]
    
    if prediction == 1:
        st.error("🚨 High risk of employee leaving!")
    else:
        st.success("✅ Employee likely to stay!")
