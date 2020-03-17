from flask import Flask, render_template, request
from PIL import Image
import sys
import os
import re
import base64
from flask_cors import CORS
import numpy as np
import json

app = Flask(__name__)
CORS(app)

# Path to the saved object detection model
sys.path.append(os.path.abspath("./detect_object")) ##
#Initialize some global variables
import detect_object

@app.route("/get_picture/", methods=['GET', 'POST']) #suppose you have a get_picture button
def p1():
    return getpicture(1)

def getpicture(myid):
    rdata = request.get_data()
    image_name = 'image' + str(myid) + '.jpg' #how to we get the raw data ?
    save_uri_as_jpeg(rdata, image_name)
    print("screenshot saved as %s" % image_name)

    # Upload in S3  - optional
    #upload_to_S3(image_name)

    # Launch detect objects
    myjson = detect_object(image_name)

    # Extract Json infos
    answer = get_features_from_json(myjson)

    return answer

def save_uri_as_jpeg(uri, imagename):
    imgData = str(uri)
    imgData64 = imgData[imgData.find(',') + 1:]
    binary_data = a2b_base64(imgData64)
    with open(imagename, 'wb') as fd:
        fd.write(binary_data)
    
def detect_object(imagename):
    #we call back the yolo program
    #yolo
    response = yolo(imagename)
    return response

def get_features_from_json(myjson):
    mystr = ""
    nb_detections=myjson.shape[0]
    if nb_detections>= 1:
        face = facedetails[0]
        my_output_data=pd.read_csv(myjson, sep=',')
        mystr += '<table class="table table-sm table-striped bg-light m-2">'
        for i in range(my_output_data.shape[0]):
            my_region_id=my_output_data.iloc[i,4]
            my_box_json=json.loads(np.str(my_output_data.iloc[i,5]))
            my_attribute_json=json.loads(np.str(my_output_data.iloc[i,6]))
            my_str=np.str(my_attribute_json['clothe'])
            mystr += "</tr>"
            mystr += "</table>"
    else:
        mystr += "No clothe in picture...\n"
    return mystr

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
# run the app locally on the given port
    app.run(host='0.0.0.0', port=5000) #to run on the back end
