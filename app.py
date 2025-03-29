import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, render_template, request
from sklearn.preprocessing import LabelEncoder

# Load the saved model
model_path = "./model/improved_tcn_model.h5"
model = tf.keras.models.load_model(model_path)

# Initialize Flask app
app = Flask(__name__)

# Define the classes
classes = ['heavy', 'high', 'low', 'normal']
label_encoder = LabelEncoder()
label_encoder.fit(classes)

# Home route to render the web page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse inputs from the form
        input_values = [request.form.get(f'input_{i}') for i in range(1, 7)]

        if any(value is None or value.strip() == '' for value in input_values):
            return jsonify({'error': 'All six inputs are required'}), 400

        # Convert input values to integers
        input_list = list(map(int, input_values))

        # Input validation
        if not (1 <= input_list[0] <= 24):
            return jsonify({'error': 'Invalid input: The first value must be between 1 and 24'}), 400
        if not (0 <= input_list[1] <= 6):
            return jsonify({'error': 'Invalid input: The second value must be between 0 and 6'}), 400

        # Reshape input for the model
        X_new = np.array([input_list]).reshape((1, 6, 1))

        # Predict
        predicted_class = model.predict(X_new)
        predicted_label = label_encoder.inverse_transform([np.argmax(predicted_class)])[0]

        # Return result
        return jsonify({'prediction': predicted_label})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
