# student_academic_risk
# 🎓 Student Academic Risk Early Warning System

A data science and Streamlit-based dashboard designed to identify students who may be academically at risk using **attendance, assignment scores, and quiz performance**.

The system combines student data from multiple sources, processes and analyzes the data, and presents the results through an interactive dashboard.

## 🚀 Features

* 📊 Student academic performance dashboard
* 🧑‍🎓 Student-wise performance analysis
* 📈 Attendance and marks visualization
* 📝 Assignment and Mid-term performance analysis
* ⚠️ Academic risk identification
* 🔍 Student filtering
* 📉 Interactive charts and graphs
* 🗃️ SQLite database integration
* 🧹 Missing-data handling
* 💡 Early-warning recommendations

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data processing and analysis
* **Streamlit** – Interactive web dashboard
* **Matplotlib** – Data visualization
* **OpenPyXL** – Excel file processing
* **SQLite** – Local database

## 📁 Project Structure

```text
academic-analyzer/
│
├── app.py
├── data_processing.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── attendance.xlsx
│   ├── assignments.xlsx
│   └── quizzes.xlsx
│
└── student_risk.db(it is automatically generated)
    
```

> The exact files and folders may vary depending on the project configuration.
## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Tanish-21/student_academic_risk
```

### 2. Open the project folder

```bash
cd academic-analyzer
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually, Streamlit runs at:

```text
http://localhost:8501
```

## 🔄 How the System Works

```text
Student Data
     ↓
Data Collection
     ↓
Data Cleaning
     ↓
Data Merging
     ↓
Performance Analysis
     ↓
Risk Calculation
     ↓
Streamlit Dashboard
     ↓
Early Warning
```

## 📊 Data Analysis

The system analyzes important academic factors such as:

* Attendance percentage
* Assignment performance
* Quiz performance
* Overall academic performance

Missing values are handled during the data-processing stage to improve the reliability of the analysis.

## ⚠️ Academic Risk

Students can be categorized according to their academic performance, such as:

```text
Low Risk
Medium Risk
High Risk
```

This allows faculty to identify students who may need additional academic support.

## 🎯 Project Objective

The main objective of this project is to provide an **early-warning mechanism** that helps faculty identify students who may be struggling academically before major examinations.

## 📌 Future Enhancements

* Machine-learning-based risk prediction
* Faculty login and authentication
* Student profile pages
* Email/SMS notifications
* Attendance trend prediction
* Automated intervention recommendations
* Cloud database integration
* Deployment to a cloud platform

## 👨‍💻 Author

**Tanish**

## 📄 License

This project is developed for **educational and academic purposes**.
