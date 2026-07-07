from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load("floods.save")
scaler = joblib.load("scaler.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = []

        for i in range(20):
            value = float(request.form[f"feature{i}"])
            features.append(value)

        features = np.array(features).reshape(1, -1)

        features = scaler.transform(features)

        prediction = model.predict(features)

        if prediction[0] == 1:
            result = "High Flood Risk"
        else:
            result = "Low Flood Risk"

        return render_template("result.html", prediction=result)

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)