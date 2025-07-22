# 💼 Employee Salary Prediction App

This project is a simple Machine Learning-based web app that helps predict the salary of an employee based on details like age, education, job title, gender, and years of experience. It can make predictions for a single employee or a batch of employees using a CSV file.

---

## 📌 Problem Statement

Many companies struggle to estimate fair salaries for employees based on multiple factors. Manually comparing industry standards and employee attributes can be time-consuming and inaccurate. This app helps automate that process using a trained ML model.

---

## 📂 Project Structure

```
📁 project-root/
│
|
│──salary_predictor.pkl        # Trained XGBoost model
│
├──  salary_app.py               # Streamlit app script
│   
│
├── employee_data.csv           # Source dataset (from Kaggle)
│    
│
├──salary_plot.png             # Screenshot of actual vs predicted graph
│    
│
└── README.md                       # Project overview
```

---

## 🛠️ How It Works

### 1. Input
- You enter employee details using dropdowns and sliders (or upload a CSV).
  
### 2. Processing
- The data is encoded using OneHotEncoder.
- The model predicts the salary using an XGBoost regression model.

### 3. Output
- Shows the predicted salary instantly.
- For CSVs, it returns a downloadable file with predictions.

---

## 📷 Screenshots

They are provided in the ppt

---

## 🚀 How to Run

Make sure you have Python installed (3.8+ recommended).

1. Clone the repo
```bash
git clone https://github.com/your-username/employee-salary-predictor.git
cd employee-salary-predictor
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
```bash
streamlit run app/salary_app.py
```

---

## ✅ Features

- Predict salary for a single employee
- Batch prediction using CSV upload
- Data validation for age and experience
- Clean UI with sidebar info
- R² Score Accuracy ~88.4%

---

## 📚 References

- **Dataset Source:** [Kaggle - Employee Salaries](https://www.kaggle.com/)
- **Course Lectures:** Concepts like preprocessing, encoding, model evaluation learned in class
- **Teacher Resources:** Instructor-shared `.ipynb` notebook helped build model pipeline

---

---

## 🙋‍♂️ Author

- Name: Kolla Venkata Pradeep
- Project | July 2025
- For more information related to the project please refer the ppt.
