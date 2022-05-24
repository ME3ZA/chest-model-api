from flask import *
import json
import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

from flask_cors import CORS


filename = 'chest_model_balanced.h5'
model = keras.models.load_model('filename')


app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': "Let's get started and send me your image", 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump
  
if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
