from typing import Optional,Any
import os
import cv2
import json
import pathlib
import numpy as np
import pandas as pd
import tensorflow as tf
import os
# View an image
import random
import requests

from fastapi import FastAPI,Body,File, UploadFile
from datetime import timedelta, date, datetime
import uuid
from fastapi.param_functions import Query

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout

model_1 = Sequential([
  Conv2D(32, 5, activation='relu', input_shape=(300, 300, 3)),
  MaxPool2D(),
  Conv2D(32, 5, activation='relu'),
  MaxPool2D(),
  Conv2D(64, 5, activation='relu'),
  MaxPool2D(),
  Conv2D(64, 5, activation='relu'),
  MaxPool2D(),
  Flatten(),
  Dense(512, activation='relu'),
  Dense(128, activation='relu'),
  Dense(64, activation='relu'),
  Dense(17, activation='softmax') 
])

# model_1 = Sequential([
#   Conv2D(32, 5, activation='relu', input_shape=(300, 300, 3)),
#   MaxPool2D(),
#   Conv2D(32, 5, activation='relu'),
#   MaxPool2D(),
#   Conv2D(64, 5, activation='relu'),
#   MaxPool2D(),
#   Conv2D(64, 5, activation='relu'),
#   MaxPool2D(),
#   Conv2D(128, 5, activation='relu'),
#   MaxPool2D(),
#   Flatten(),
#   Dense(512, activation='relu'),
#   Dropout(0.5),
#   Dense(128, activation='relu'),
#   Dense(64, activation='relu'),
#   Dense(28, activation='softmax') 
# ])
model_1.load_weights("save_new_weights_2.h5")





app = FastAPI(title="monument detection", description="BNMIT")

# Create a function to import an image and resize it to be able to be used with our model
def load_and_prep_image(img, img_shape=300):
  """
  Reads an image from filename, turns it into a tensor
  and reshapes it to (img_shape, img_shape, colour_channel).
  """
  # Read in target file (an image)


  # Decode the read file into a tensor & ensure 3 colour channels 
  # (our model is trained on images with 3 colour channels and sometimes images have 4 colour channels)
  img = tf.image.decode_image(img, channels=3)

  # Resize the image (to the same size our model was trained on)
  img = tf.image.resize(img, size = [img_shape, img_shape])

  # Rescale the image (get all values between 0 and 1)
  img = img/255.
    
  return img

# Adjust function to work with multi-class
def pred_and_plot(model, img, class_names):
  """
  Imports an image located at filename, makes a prediction on it with
  a trained model and plots the image with the predicted class as the title.
  """
  # Import the target image and preprocess it
  img = load_and_prep_image(img)

  # Make a prediction
  pred = model.predict(tf.expand_dims(img, axis=0))

  # Get the predicted class
  if len(pred[0]) > 1: # check for multi-class
    pred_class = class_names[pred.argmax()] # if more than one output, take the max
  else:
    pred_class = class_names[int(tf.round(pred)[0][0])] # if only one output, round

  return pred_class



@app.post("/monument")
async def predictCNN(file: UploadFile = File(...)):
    img=await file.read()
    print(file.content_type)
    l=['Amr ibn al-Aas Mosque', 'Burj Khalifa', 'Charar-e-Sharief',
       'Charminar', 'Christ the Redeemer', 'Eiffel Tower',
       'Gateway of India', 'Golden Temple', 'Great Wall of China',
       'India Gate', 'Machu Pichu', 'Pyramid of Giza', 'Qutub Minar',
       'Roman Colosseum', 'Sun Temple Konark', 'Taj Mahal',
       'Victoria Memorial']
    class_names=np.array(l)
    response=pred_and_plot(model_1,img,class_names)

    

    return {"monument_type": response}      




####################-----------------------------------------------------------         
