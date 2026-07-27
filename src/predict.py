import joblib

# Load the trained model
model = joblib.load("models/score_model.pkl")

print("===== Student Score Prediction =====")

# Take input from the user
hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))
previous = float(input("Enter previous exam marks: "))
sleep = float(input("Enter sleep hours: "))

# Create input for prediction
student = [[hours, attendance, previous, sleep]]

# Predict score
predicted_score = model.predict(student)

print("\n==============================")
print(f"Predicted Exam Score: {predicted_score[0]:.2f}")
print("==============================")