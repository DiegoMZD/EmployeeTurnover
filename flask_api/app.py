from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load Model and Preprocessor
pipeline = joblib.load("models\p2_bagg_hyp.pkl")
# preprocessor = joblib.load("../models/prep2.pkl")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON Data
    data = request.get_json()
    df = pd.DataFrame([data])

    # Apply Preprocessing
    # processed_data = preprocessor.transform(df)

    # Make Prediction
    # prediction = model.predict(processed_data)
    prediction = pipeline.predict(df)
    return jsonify({'turnover_prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
