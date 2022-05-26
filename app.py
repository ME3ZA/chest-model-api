import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import json
import os

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def home_page():
    data_set = {'Page': 'Home', 'Message': "Let's get started and send me your image"}
    json_dump = json.dumps(data_set)
    return json_dump

#@flask_app.route("/predict", methods = ["POST"])
#def predict():
    #float_features = [float(x) for x in request.form.values()]
    #features = [np.array(float_features)]
    #prediction = model.predict(features)
    #return render_template("index.html", prediction_text = "The flower species is {}".format(prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)
