# 🎓 Student Performance Prediction System

A Python-based Machine Learning application that predicts student academic performance using **attendance, internal marks, study hours, previous marks, assignment marks, and backlogs**.

The project uses a **Random Forest Classifier** for binary classification and provides both a **Tkinter desktop application** and a **Streamlit web application**.

---

## 🌐 Live Demo

👉 **Open Student Performance Prediction System:**  
https://student-performance-prediction007.streamlit.app/

---

## ✨ Features

- 🤖 Student performance prediction using Machine Learning
- 🌲 Random Forest Classifier
- 🔀 Binary Classification — Good / Poor
- 🖥️ Tkinter desktop application
- 🌐 Streamlit web application
- 💾 SQLite database for storing student records
- 📦 Pickle for saving and loading the trained model
- ☁️ Online deployment using Streamlit Community Cloud
- ✅ Input validation for student data

---

## 📊 Dataset

The project uses a **90-record student academic dataset** containing different student performance patterns.

### Dataset Features

| Feature | Description |
|---|---|
| Attendance | 0–100% |
| Internal Marks | 0–100 |
| Study Hours | Hours per day |
| Previous Marks | 0–100 |
| Assignment Marks | 0–100 |
| Backlogs | 0 or more |
| Performance | Good / Poor |

### Dataset Columns

```text
attendance
internal_marks
study_hours
previous_marks
assignment_marks
backlogs
performance
Example Dataset Record
Attendance: 85%
Internal Marks: 75
Study Hours: 4
Previous Marks: 78
Assignment Marks: 82
Backlogs: 0
Performance: Good
 Machine Learning Approach

The project uses a Random Forest Classifier to classify student performance into two categories:

Good
Poor
 Prediction Logic

The application primarily uses the trained Random Forest Classifier to make predictions.

Additional validation rules are included for clearly poor academic conditions.

Rule 1 — Low Academic Performance
Attendance < 40 AND Internal Marks < 40
                    ↓
                  Poor
Rule 2 — Number of Backlogs
Backlogs > 2
      ↓
    Poor

For other cases, the trained Random Forest model makes the prediction.

Student Input
      ↓
Validation Rules
      ↓
Random Forest Classifier
      ↓
Good / Poor

Streamlit Application Flow
                 Trained ML Model
                       │
              ┌────────┴────────┐
              ↓                 ↓
           Tkinter          Streamlit
              ↓                 ↓
        Desktop App        Web Application
                                ↓
                           Online Access

📁Project Structure
Student_Performance_Project/
│
├── app.py                  # Streamlit web application
├── main.py                 # Tkinter desktop application
├── train_model.py          # Machine Learning model training
├── students.csv            # Student dataset
├── student_model.pkl       # Trained Random Forest model
├── label_encoder.pkl       # Label encoder
├── database.db             # SQLite database
├── requirements.txt        # Required Python packages
└── README.md               # Project documentation
