import os
import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# --- PATH SETUP ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'anemia_model.pkl')
scaler_path = os.path.join(BASE_DIR, 'scaler.pkl')

# --- LOAD ASSETS ---
try:
    model = pickle.load(open(model_path, 'rb'))
    scaler = pickle.load(open(scaler_path, 'rb'))
except Exception as e:
    print(f"Error: Ensure pkl files are in the same folder as app.py. Details: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Mapping Text Inputs to Numbers
        gender = 1 if request.form.get('gender') == 'Male' else 0
        family_hist = 1 if request.form.get('family_hist') == 'Yes' else 0
        med_care = 1 if request.form.get('med_care') == 'Yes' else 0
        bp_meds = 1 if request.form.get('bp_meds') == 'Yes' else 0
        breath = 1 if request.form.get('breath') == 'Yes' else 0
        vision = 1 if request.form.get('vision') == 'Yes' else 0
        nosebleed = 1 if request.form.get('nosebleed') == 'Yes' else 0
        diet = 1 if request.form.get('diet') == 'Yes' else 0

        # Mapping Scales
        age_map = {'18-35': 1, '36-55': 2, '65+ years': 3}
        age = age_map.get(request.form.get('age'), 1)
    

        sys = float(request.form.get('sys'))
        dia = float(request.form.get('dia'))
        # Define data structures for each scenario
        if sys >= 180 or dia >= 120:
            category, color, risk = "Hypertensive Crisis", "danger", "Emergency"
            recs = [
                ("Seek Emergency Care", "🏥 Go to the nearest emergency room immediately or call 911."),
                ("Monitor Symptoms", "⚠️ Watch for chest pain, shortness of breath, or numbness."),
                ("Medication List", "📝 Prepare a list of all current medications for responders."),
                ("Avoid Exertion", "🪑 Sit or lie down; do not attempt any physical activity.")
            ]
        elif sys >= 140 or dia >= 90:
            category, color, risk = "Stage 2 Hypertension", "danger", "High"
            recs = [
                ("Urgent Consultation", "👨‍⚕️ Schedule a visit with your physician within 1-2 days."),
                ("Daily Monitoring", "⌚ Check BP every morning and evening at the same time."),
                ("Sodium Restriction", "🥗 Limit salt intake to less than 1,500mg per day."),
                ("Medication Therapy", "💊 Be prepared to discuss starting or adjusting medications.")
            ]
        elif (130 <= sys <= 139) or (80 <= dia <= 89):
            category, color, risk = "Stage 1 Hypertension", "warning", "Moderate"
            recs = [
                ("DASH Diet Plan", "🍎 Focus on fruits, vegetables, and low-fat dairy."),
                ("Physical Activity", "🏃 Aim for 150 minutes of moderate aerobic activity weekly."),
                ("Stress Management", "🧘 Practice daily meditation or deep breathing exercises."),
                ("Bi-weekly Monitoring", "📊 Log your readings twice a week to track trends.")
            ]
        else:
            category, color, risk = "Normal Blood Pressure", "success", "Low"
            recs = [
                ("Healthy Lifestyle", "✅ Continue your current diet and activity levels."),
                ("Regular Exercise", "🚴 Maintain at least 30 minutes of activity daily."),
                ("Low-Sodium Diet", "🥗 Keep sodium intake below 2,300mg per day."),
                ("Annual Check-up", "🏥 Schedule your yearly physical to monitor health.")
            ]

        return render_template('index.html', 
                               prediction_text=category, 
                               color_class=color, 
                               risk_level=risk,
                               recommendations=recs,
                               show_modal=True)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)