import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle


# =========================================================
# LOAD DATASET
# =========================================================

data = pd.read_csv("students.csv")

print("========================================")
print("   STUDENT PERFORMANCE MODEL TRAINING")
print("========================================")

print("\nTotal records:", len(data))

print("\nPerformance counts:")
print(data["performance"].value_counts())

print("\nDuplicate rows:", data.duplicated().sum())


# =========================================================
# SEPARATE FEATURES AND TARGET
# =========================================================

X = data.drop("performance", axis=1)
y = data["performance"]


# =========================================================
# ENCODE GOOD / POOR
# =========================================================

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

print("\nPerformance classes:")
print(list(encoder.classes_))


# =========================================================
# TRAIN / TEST SPLIT
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# =========================================================
# RANDOM FOREST MODEL
# =========================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# =========================================================
# TRAIN MODEL
# =========================================================

model.fit(X_train, y_train)

print("\nModel trained successfully!")


# =========================================================
# TEST MODEL
# =========================================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)


# =========================================================
# DISPLAY ACCURACY
# =========================================================

print("\n========================================")
print("           MODEL EVALUATION")
print("========================================")

print(
    "Test Accuracy:",
    round(accuracy * 100, 2),
    "%"
)


# =========================================================
# SAVE TRAINED MODEL
# =========================================================

with open("student_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nstudent_model.pkl created successfully!")


# =========================================================
# SAVE LABEL ENCODER
# =========================================================

with open("label_encoder.pkl", "wb") as file:
    pickle.dump(encoder, file)

print("label_encoder.pkl created successfully!")


# =========================================================
# FINAL MESSAGE
# =========================================================

print("\n========================================")
print("       TRAINING COMPLETED SUCCESSFULLY")
print("========================================")