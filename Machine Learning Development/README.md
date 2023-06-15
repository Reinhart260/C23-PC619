# Flora and Fauna Model
The project is based from Google Colab (due to limited system requirements of our laptop/PC). Using Machine Learning with Tensorflow as framework to Classify the flora and fauna.
      
      https://colab.research.google.com/drive/1Gxl8V5Z4sF0dQ6BoBd-xtKQvbrcddFkf?usp=sharing
## 1. Image Loading from Directory
Load images from Modified Directory that we host to Google Drive
      https://drive.google.com/drive/folders/1V6YU2dqBAmc9COvpMZGoGLjr9sA8yaLS?usp=sharing

## 2. Pre-processing Image
- Rescale and load images using Keras ImageGenerator

* Defining target and feature from existing train, test and validation Directory with Generated
      
      feature, target = (train_data_gen)
      feature, target = (val_data_gen)
      feature, target = (test_data_gen)
      
+ Resizing the entire image into 224x224 

## 3. Modelling
- Using ILSVRC pre-trained models VGG16 to make model accuracy better.
      https://drive.google.com/drive/folders/1T38ALDAgf2wSevWuunrcj_I1JrLimjrH?usp=sharing
- Added more layer too to model.Sequential to make model accuracy more better:
    * Added Flatten layer(input_shape)
    * Added Dense(units=100, activation=keras.layers.LeakyReLU(alpha=0.3)) layer
    * Added Dropout(units=0.5) layer
    * Added more Dense(units=50, activation=keras.layers.LeakyReLU(alpha=0.3)) layer
    * Added Dropout(units=0.3) layer
    * Added output layer Dense(units=num_classes, activation='softmax')

## 4. Training
- Using SparseCategoricalCrossentropy as loss
- Using RMSprop(learning_rate=1e-4) as optimizer
- Training with 100 epochs
- From the result, got:

  - loss: 31%
  - accuracy: 89%
  - val_loss: 66%
  - val_accuracy: 81%

## 5. Saved the Model to Google Drive
Then, saved the model (*.h5 format) to Google Drive (saved only the best model to Google Drive)
