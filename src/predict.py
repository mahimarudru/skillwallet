import os
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Get project root directory
base_dir = os.path.dirname(os.path.dirname(__file__))

# Paths to saved model and scaler
model_path = os.path.join(base_dir, "model", "anemia_model.pkl")
scaler_path = os.path.join(base_dir, "model", "scaler.pkl")

# Load trained model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)


def predict_stage(input_data):

    # Convert input dictionary to dataframe
    df = pd.DataFrame([input_data])

    # One-hot encode categorical features
    df = pd.get_dummies(df)

    # Load training dataset to get correct feature columns
    training_data = pd.read_csv(os.path.join(base_dir, "data", "patient_data.csv"))

    # Separate features from training dataset
    X_train = training_data.drop(["Stages", "Severity"], axis=1)

    # Apply same encoding as training
    X_train = pd.get_dummies(X_train)

    # Align prediction features with training features
    df = df.reindex(columns=X_train.columns, fill_value=0)

    # Scale features
    df_scaled = scaler.transform(df)

    # Predict
    prediction = model.predict(df_scaled)

    # Decode predicted label back to stage name
    label_encoder = LabelEncoder()
    label_encoder.fit(training_data["Stages"])

    stage = label_encoder.inverse_transform(prediction)

    return stage[0]


# Example test input
if __name__ == "__main__":

    sample_patient = {
        "C": "Female",
        "Age": "51-64",
        "History": "Yes",
        "Patient": "Yes",
        "TakeMedication": "Yes",
        "BreathShortness": "Yes",
        "VisualChanges": "No",
        "NoseBleeding": "No",
        "Whendiagnoused": "Long ago",
        "Systolic": "130+",
        "Diastolic": "100+",
        "ControlledDiet": "No"
    }

    result = predict_stage(sample_patient)

    print("Predicted Stage:", result)