from flask import *
import json
import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from flask_cors import CORS

from tensorflow.keras.preprocessing import image
from flask import Flask, render_template, request
#from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_html():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #f.save(secure_filename(f.filename))
      return f
		
#if __name__ == '__main__':
 #  app.run(debug = True)


filename = 'chest_model_balanced.h5'
model = keras.models.load_model(filename)

y=model.predict(upload_file())
ans=np.argmax(y,axis=1)
print(ans)
if (ans==0):
    print("covid")
elif (ans==1):
    print("healthy")
elif (ans==2):
    print("Lung Tumor")
else :
    print("Pneumonia")


#@app.route('/', methods = ['GET'])
#def home_page():
 #   data_set = {'Page': 'Home', 'Message': "Let's get started and send me your image"}
  #  json_dump = json.dumps(data_set)
   # return json_dump
  
if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
