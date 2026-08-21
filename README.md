# 🎓 Student Performance Prediction System

A Python-based Machine Learning application that predicts student academic performance using **attendance, internal marks, study hours, previous marks, assignment marks, and backlogs**.

The project uses a **Random Forest Classifier** and provides both a **Tkinter desktop application** and a **Streamlit web application**.

## 🌐 Live Demo

👉 [Open Student Performance Prediction System](https://student-performance-prediction007.streamlit.app/)

## ✨ Features

- 🤖 Student performance prediction using Machine Learning
- 🌲 Random Forest Classifier
- 🖥️ Tkinter desktop application
- 🌐 Streamlit web application
- 💾 SQLite database for storing student records
- 📦 Pickle for saving and loading the trained model
- ☁️ Online deployment using Streamlit Community Cloud
- ✅ Input validation for student data

## 📊 Dataset

The project uses **80 student records** with the following features:

| Feature | Range / Description |
|---|---|
| Attendance | 0–100% |
| Internal Marks | 0–100 |
| Study Hours | Hours per day |
| Previous Marks | 0–100 |
| Assignment Marks | 0–100 |
| Backlogs | 0 or more |
| Performance | Good / Poor |

## 🔄 Workflow

```text
Student Dataset
      ↓
Data Processing
      ↓
Random Forest Classifier
      ↓
Model Training
      ↓
Student Input
      ↓
Performance Prediction
      ↓
Good / Poor

Technologies Used

Python | Pandas | NumPy | Scikit-learn | Random Forest | Tkinter | Streamlit | SQLite  | Git | GitHub

📁 Project Structure
Student_Performance_Project/
│
├── app.py                  # Streamlit web application
├── main.py                 # Tkinter desktop application
├── train_model.py          # Machine Learning model training
├── students.csv            # Student dataset
├── student_model.pkl       # Trained ML model
├── label_encoder.pkl       # Label encoder
├── database.db             # SQLite database
├── requirements.txt        # Required Python packages
└── README.md               # Project documentation

📊 Dataset

The project uses a student academic dataset containing 80 student records.

The dataset contains the following columns:

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
Feature Ranges

Attendance       → Maximum 100%
Internal Marks   → Maximum 100
Previous Marks   → Maximum 100
Assignment Marks → Maximum 100
Study Hours      → Hours per day
Backlogs         → 0, 1, 2, 3, ...
Performance      → Good / Poor

🔄 Project Workflow
Student Dataset
      ↓
Data Preparation
      ↓
Feature Selection
      ↓
Label Encoding
      ↓
Train/Test Split
      ↓
Random Forest Classifier
      ↓
Trained Model
      ↓
Student Input
      ↓
Performance Prediction
      ↓
Good / Poor
