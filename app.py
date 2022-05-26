from flask import *
from keras.models import load_model
from keras.preprocessing import image
import json
import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

filename = 'chest_model_balanced.h5'
model = keras.models.load_model(filename)

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "This Project Was Designed By The Students of Faculty of Electronic Engineering - Egypt"

if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
