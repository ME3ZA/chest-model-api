from flask import *
import json
import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

from flask_cors import CORS


filename = 'chest_model_balanced.h5'
model = keras.models.load_model(filename)


app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def main():
	return render_template("index.html")
  
if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
