import os



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import keras
import io
import numpy as np
from PIL import Image

from flask import Flask, request, jsonify

# Import model


model = keras.models.load_model("model_fc.h5")

# Prediction function
def predict(x):
    predictions = model(x)
    pred = np.argmax(predictions, axis=1)
    return pred

    # Initialize Flask server with error handling


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({"error": "no file"})

        try:
            image_bytes = file.read()
            img = Image.open(io.BytesIO(image_bytes))
            prediction = predict(img)
            data = {"prediction": str(prediction)}
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)})




if __name__ == "__main__":
    app.run(debug=True)
