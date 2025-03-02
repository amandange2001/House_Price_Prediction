from flask import Flask, request, render_template
import numpy as np
import joblib
import os

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__)) 
model_path = os.path.join(project_dir, 'models', 'house_price_model.pkl')


model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        MedInc = float(request.form['MedInc'])
        HouseAge = float(request.form['HouseAge'])
        AveRooms = float(request.form['AveRooms'])
        AveOccup = float(request.form['AveOccup'])
        features = np.array([[MedInc, HouseAge, AveRooms, AveOccup]])
        prediction = model.predict(features)[0]
        return render_template('index.html', prediction_text=f'Predicted House Price: ${prediction * 100000:.2f}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
