#importing packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from imutils.video import VideoStream
from threading import Thread
import RPi.GPIO as GPIO
from picamera import PiCamera
import numpy as np
import imutils
import time
import cv2
import os


MODEL_PATH = "nazwa_modelu_CNN.model"

#ladowanie modelu
print("LADOWANIE MODELU...")
model = load_model(MODEL_PATH)

#inicjalizacja kamery i wideostreamu
print("LADOWANIE WIDEOSTREAMU....")
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# zapetlenie obrazu z wideostreamu
while True:
	# bierzemy frame z wideostreamu i zmieniamy jego wymiar na max 400px szerokosci
	frame = vs.read()
	frame = imutils.resize(frame, width=400)
