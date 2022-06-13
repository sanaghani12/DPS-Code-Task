import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    year = int(request.form.get('year'))
    month = int(request.form.get('month'))
    category = int(request.form.get('category'))
    type = int(request.form.get('type'))
    features = [[category, type, year, month]]
    prediction = int(model.predict(features)[0])

    return render_template(
        'index.html',
        prediction_text='prediction value is {}'.format(prediction))

@app.route("/postapi/predict", methods=["POST"])
def apiPredict():
    if "year" not in request.get_json() or "month" not in request.get_json():
        return {"Error": "Year and month is required"}, 400

    data = request.get_json()
    year = int(data['year'])
    month = int(data['month'])
    category = 0
    type = 0

    features = [[category, type, year, month]]
    prediction = int(model.predict(features)[0])

    return {'prediction': prediction}


if __name__ == "__main__":
    app.run(debug=True)
