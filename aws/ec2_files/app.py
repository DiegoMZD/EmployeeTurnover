from flask import Flask, request, jsonify
import joblib
import pandas as pd

pipeline = joblib.load("p2_bagg_hyp.pkl")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])

    prediction = pipeline.predict(df)
    return jsonify({'turnover_prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
