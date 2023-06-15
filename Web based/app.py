import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ["SM_FRAMEWORK"] = "tf.keras"

import pickle
import io
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image
from keras.models import load_model
#from keras.preprocessing import image
import keras.utils as image
from tensorflow.keras.applications.vgg16 import VGG16, decode_predictions

from flask import Flask, request, jsonify, render_template

    # Import model pip 
model = load_model('model_fc.h5')
pre_model = VGG16(include_top=False, weights='imagenet')

    # Prediction function
def predict(x):
    img = image.load_img(x, target_size=(224,224))
    img = image.img_to_array(img)
    img = img.astype(np.float32) / 255
    img = np.expand_dims(img, axis=0)
    bt_prediction = pre_model.predict(img)
    pred= model.predict(bt_prediction)
    return pred

    # Initialize Flask server with error handling
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])

def main():
	return render_template("index.html")

@app.route("/submit", methods=["GET", "POST"])
def get_output():
    if request.method == "POST":
        img = request.files['my_image']
        img_path = "images/" + img.filename	
        img.save(img_path)
        if img is None or img.filename == "":
            return jsonify({"error": "no file"})


        prediction = predict(img_path)
        class_name = ['Butterflies', 'Chickens', 'Daisy', 'Dandelion', 'Duck', 'Elephants', 'Fish', 'Frog', 'Horses', 'Monkey', 'Rose', 'Snake', 'Spider', 'Squirells', 'Sunflower', 'Tulip']
        pred = class_name[np.argmax(prediction)]
        #label = decode_predictions(prediction)
        #label = label[0][0]
        #clas = '%s (%.2f%%)' % (label[1], label[2] * 100)
        return render_template("index.html", prediction = pred, img_path = img_path)


if __name__ == "__main__":
    app.run(debug=True)