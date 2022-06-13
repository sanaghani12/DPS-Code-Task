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


if __name__ == "__main__":
    app.run(debug=True)