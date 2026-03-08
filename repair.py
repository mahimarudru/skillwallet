import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Create dummy data matching your 6 medical features: 
# Gender, Age, Family_Hist, Med_Care, Sys, Dia
X_train = np.array([[1, 2, 0, 0, 120, 80], [0, 3, 1, 1, 150, 95]])
y_train = np.array([0, 1])

# Train a temporary model and scaler
model = LogisticRegression().fit(X_train, y_train)
scaler = StandardScaler().fit(X_train)

# Save them correctly as binary files
with open('anemia_model.pkl', 'wb') as f:
    pickle.dump(model, f)
    
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("✅ Files Repaired! You can now run your app.py.")