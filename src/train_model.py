import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# -------------------------
# Step 1: Load Dataset
# -------------------------
df = pd.read_csv("dataset/student_scores.csv")

# -------------------------
# Step 2: Select Features (X) and Target (y)
# -------------------------
X = df[["Hours", "Attendance", "Previous", "Sleep"]]
y = df["Score"]

# -------------------------
# Step 3: Split Data
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------
# Step 4: Create Model
# -------------------------
model = LinearRegression()

# -------------------------
# Step 5: Train Model
# -------------------------
model.fit(X_train, y_train)

# -------------------------
# Step 6: Make Predictions
# -------------------------
predictions = model.predict(X_test)

# -------------------------
# Step 7: Evaluate Model
# -------------------------
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model Evaluation")
print("---------------------------")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.2f}")

# -------------------------
# Step 8: Save Model
# -------------------------
joblib.dump(model, "models/score_model.pkl")

print("\nModel saved successfully!")