from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load('random_forest_model.pkl')  # Make sure the model file is in the same directory

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get the JSON data from POST request
    input_features = np.array(data['features']).reshape(1, -1)  # Convert the input to a numpy array
    prediction = model.predict(input_features)  # Make a prediction using the trained model
    return jsonify({'prediction': int(prediction[0])})  # Return prediction as a JSON response

if __name__ == "__main__":
    app.run(debug=True)
