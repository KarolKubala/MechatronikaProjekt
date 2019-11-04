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
		# prepare the image to be classified by our deep learning network
	image = cv2.resize(frame, (28, 28))
	image = image.astype("float") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	(Zelek, Czekoladka) = model.predict(image)[0]
	label = "Zelek"
	probability = Zelek
	# Sprawdzamy czy zostala wykryta czekoladka czy zelek (porownujemy prawdopodobienstwo)
	if Czekoladka > Zelek:
		#update labelu
		label = "Czekoladka"
		probability = Czekoladka
		
