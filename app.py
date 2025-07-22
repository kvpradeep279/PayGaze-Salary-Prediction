import streamlit as st
import pandas as pd
import joblib

# Loading the trained model
model = joblib.load("best_salary_model.pkl")

# Loading job titles from training data
@st.cache_data
def load_job_titles():
    df = pd.read_csv("cleaned_salary_data.csv")  # exported training file
    return sorted(df["Job Title"].unique())

job_titles = load_job_titles()

# Page setup
st.set_page_config(page_title="Salary Prediction App", layout="wide", page_icon="💼")

# Custom header using markdown
st.markdown("""
    <h1 style='text-align: center; white-space: nowrap; font-size: 45px; font-family: Arial, sans-serif; color: ##ADD8E6;'>
         PayGaze
    </h1>
""", unsafe_allow_html=True)

st.markdown("---")

# Sidebar styling
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3062/3062634.png", width=100)
    st.subheader("Customize Theme")
    st.markdown("Try dark/light mode toggle from Streamlit settings.")
    st.markdown("---")


    st.markdown("**Model Info**")
    st.text("Version: 1.0.0")
    st.text("Trained on: 2025-07-21")
    st.text("Accuracy: 88.4% (R² Score)")
    st.caption("Made using Streamlit")
    

# One employee prediction
st.header("🔍 Predict Salary for One Employee")

col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.number_input("Age", min_value=18, max_value=60, value=25)
with col2:
    education = st.selectbox("Education Level", [ "Bachelor's", "Master's", "PhD"])
    experience = st.number_input("Years of Experience", min_value=0, max_value=40, value=1)

job_title = st.selectbox("Job Title", job_titles)

if st.button("Predict Salary"):
    row = pd.DataFrame([{
        "Gender": gender,
        "Age": age,
        "Education Level": education,
        "Job Title": job_title,
        "Years of Experience": experience
    }])
    salary = model.predict(row)[0]
    st.success(f"💰 Estimated Salary: ₹{salary:,.2f}")

# Spacing before batch section
st.markdown("<br><hr><br>", unsafe_allow_html=True)

# Batch upload section
st.subheader("📂 Upload CSV for Batch Prediction")
uploaded_file = st.file_uploader("Upload a CSV file with employee details", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    try:
        predictions = model.predict(df)
        df["Predicted Salary"] = predictions
        st.dataframe(df)

        # Download results
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download Predicted Results", csv, "salary_predictions.csv", "text/csv")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

# To visualize the model prediction graph
# Spacing
st.markdown("<br><hr><br>", unsafe_allow_html=True)
st.subheader("📊 Model Accuracy Visualization")

# URL parameter to persist state across reruns
show_image = st.query_params.get("show_image", "false") == "true"

if not show_image:
    if st.button("Show Model Accuracy Graph"):
        st.query_params["show_image"] = "true"
        st.rerun()
else:
    st.image("model_accuracy.png", caption="Model Accuracy vs Epochs", use_container_width=True)
    if st.button("Hide Model Accuracy Graph"):
        st.query_params["show_image"] = "false"
        st.rerun()

# To take feedback from the user
# Spacing
st.markdown("<br><hr><br>", unsafe_allow_html=True)
st.subheader("📣 Feedback")
feedback = st.text_area("Share your thoughts or suggestions...")
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")

# The icons used above in the code are taken from google fonts.
# To run app.py enter: streamlit run app.py in the command prompt at the location of the file.
