<p align="center"> <img src="https://github.com/Reinhart260/C23-PC619/assets/121779270/85f0f1a3-42d1-470d-8f21-06c2209291fe.png)" width="250" height="250"></p>
<p align="center"><b>FEDU App</b></p>
<p align="center">“Application for Introducing Flora and Fauna to Help Children Explore the Surrounding Environment using Game Based Learning Method” </P>

# About
Fedu App is application for introducing Flora and Fauna to help children explore the surrounding environment using Game Based learning method

# Machine Learning Documentation
The project is based from Google Colab (due to limited system requirements of our laptop/PC). Using Machine Learning with Tensorflow as framework to Classify the flora and fauna.
      
      https://colab.research.google.com/drive/1Gxl8V5Z4sF0dQ6BoBd-xtKQvbrcddFkf?usp=sharing
- ## 1. Image Loading from Directory
     Load images from Modified Directory that we host to Google Drive
        https://drive.google.com/drive/folders/1V6YU2dqBAmc9COvpMZGoGLjr9sA8yaLS?usp=sharing

- ## 2. Pre-processing Image
     - Rescale and load images using Keras ImageGenerator

    * Defining target and feature from existing train, test and validation Directory with Generated
      
      feature, target = (train_data_gen)
      feature, target = (val_data_gen)
      feature, target = (test_data_gen)
      
    + Resizing the entire image into 224x224 

- ## 3. Modelling
     - Using ILSVRC pre-trained models VGG16 to make model accuracy better.
      https://drive.google.com/drive/folders/1T38ALDAgf2wSevWuunrcj_I1JrLimjrH?usp=sharing
     - Added more layer too to model.Sequential to make model accuracy more better:
      * Added Flatten layer(input_shape)
      * Added Dense(units=100, activation=keras.layers.LeakyReLU(alpha=0.3)) layer
      * Added Dropout(units=0.5) layer
      * Added more Dense(units=50, activation=keras.layers.LeakyReLU(alpha=0.3)) layer
      * Added Dropout(units=0.3) layer
      * Added output layer Dense(units=num_classes, activation='softmax')

- ## 4. Training
     - Using SparseCategoricalCrossentropy as loss
     - Using RMSprop(learning_rate=1e-4) as optimizer
     - Training with 100 epochs
     - From the result, got:

        - loss: 31%
        - accuracy: 89%
        - val_loss: 66%
      - val_accuracy: 81%

- ## 5. Saved the Model to Google Drive
     Then, saved the model (*.h5 format) to Google Drive (saved only the best model to Google Drive)
     https://drive.google.com/drive/folders/1tFEo7ULzmIuvABx_LBXwAxO7mdN50mFD?usp=sharing

# Cloud Computing Documentation

# Our Team
<p>Team ID		: C23-PC619</P>
<p>Team Member		: </P>
<li>(ML) M251DSX0157 	- Azka Faza Dzulqarnain</li>   		
(ML) M304DSY0547 	- [Yaasintha La Jopin Arisca Corpputy](https://github.com/yaasinthariesca)
<li>(ML) M132DKX4965	- Arief Rizqie Putrananda 			</li>
<li>(CC) C303DSX2003 	- Reinhart Untoro 				</li>
<li>(CC) C038DSX4841	- Fikra Agha Rabbani Asayanda 	</li>
<li>(MD) A033DSX3250	- Muhammad Farhan Ramadhan 	</li>	
