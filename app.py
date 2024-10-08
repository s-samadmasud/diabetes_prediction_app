from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
import jinja2

# Load the model
with open('diabetes_analysis_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input
    data = request.form

    # Assuming 'data' is a dictionary
    X = np.array([round(float(data[key]), 4) for key in data.keys()])
    X = X.reshape(1, -1)

    # Make prediction
    prediction = model.predict(X)[0]

    # Get the predicted class label and color based on prediction
    result = "No Diabetes" if prediction == 0 else "Diabetes"
    color = "text-bg-danger" if prediction == 0 else "text-bg-success"  # Use consistent variable name

    return render_template('result.html', prediction=result, color=color)

if __name__ == '__main__':
    app.run(debug=True)