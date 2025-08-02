from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load('model/titanic_model.pkl')
scaler = joblib.load('model/scaler.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form
        features = [
            float(data['Age']),
            float(data['Fare']),
            int(data['Sex']),
            int(data['sibsp']),
            int(data['Parch']),
            int(data['Pclass']),
            int(data['Embarked'])
        ]
        features_scaled = scaler.transform([features])
        prediction = model.predict(features_scaled)
        result = "Survived" if prediction[0] == 1 else "Did Not Survive"
        return render_template('index.html', prediction=result)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
