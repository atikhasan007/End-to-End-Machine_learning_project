from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd

from mlProject.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "training successful"


@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        try:
            fixed_acidity = float(request.form['fixed acidity'])
            volatile_acidity = float(request.form['volatile acidity'])
            citric_acid = float(request.form['citric acid'])
            residual_sugar = float(request.form['residual sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free sulfur dioxide'])
            total_sulfur_dioxide = float(request.form['total sulfur dioxide'])
            density = float(request.form['density'])
            ph = float(request.form['ph'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data = [[
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                ph,
                sulphates,
                alcohol
            ]]

            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction=str(predict))

        except Exception as e:
            print("Exception:", e)
            return "Something is wrong"

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)