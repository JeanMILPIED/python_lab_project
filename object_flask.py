from flask import Flask, render_template, request
from PIL import Image
from keras.preprocessing import image
import sys
import os
import re
import base64
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

# Path to the saved object detection model
sys.path.append(os.path.abspath("./cnn-mnist"))
#Initialize some global variables
global detect_object
detect_object = load_function(detect_object.py)

@app.route('/')
def index():
    return render_template("index.html")

def convertImage(image_proper):
  #if needed to make the image in the same file we are detecting from named output.png
  return output.png

def loadImage(filename):
  #we are using this to load from the "output.png" file in proper format
  return image_proper

@app.route('/detect/', methods=['GET', 'POST'])
def detect object():
    imgData = request.get_data() #we get daat from the API
    convertImage(imgData) # we convert to output.png
    img = loadImage("output.png") # we load output .png
    my_objects = detect_object(img) # we detect object from image
    return my_objects # we return the objects detected + some features on the same image

if __name__ == "__main__":
# run the app locally on the given port
    app.run(host='0.0.0.0', port=5000) #to run on the back end
