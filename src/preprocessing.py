import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_data():

    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "data", "patient_data.csv")

    data = pd.read_csv(data_path)

    return data

def preprocess_data(data):

    # Remove missing values
    data = data.dropna()

    # Separate target first
    y = data["Stages"]

    # Encode target labels
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

    # Remove target from features
    X = data.drop(["Stages", "Severity"], axis=1)
    # Encode categorical features
    X = pd.get_dummies(X)

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled,
        y,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, y_train, y_test, scaler


if __name__ == "__main__":

    data = load_data()

    X_train, X_test, y_train, y_test, scaler = preprocess_data(data)

    print("Training samples:", X_train.shape)
    print("Testing samples:", X_test.shape)

    # PROOF: check relationship between BP and Stage
    print("\nRelationship between BP and Stage:\n")
    print(data.groupby(["Systolic","Diastolic"])["Stages"].unique())