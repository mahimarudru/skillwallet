import joblib

from preprocessing import load_data, preprocess_data

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix


# Load dataset
data = load_data()

# Preprocess dataset
X_train, X_test, y_train, y_test, scaler = preprocess_data(data)


# Define models
models = {

    "Logistic Regression": LogisticRegression(max_iter=1000),

    "Decision Tree": DecisionTreeClassifier(),

    "Random Forest": RandomForestClassifier(),

    "SVM": SVC()

}


best_accuracy = 0
best_model = None
best_model_name = ""


print("\nModel Performance:\n")


# Train and evaluate
for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(name, "Accuracy:", round(accuracy, 4))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    if accuracy > best_accuracy:

        best_accuracy = accuracy
        best_model = model
        best_model_name = name


print("\nBest Model:", best_model_name)
print("Best Accuracy:", round(best_accuracy, 4))


# Save best model
joblib.dump(best_model, "model/anemia_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")


print("\nModel saved successfully.")