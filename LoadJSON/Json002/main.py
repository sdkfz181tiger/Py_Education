# coding: utf-8

import os
import cv2
import json
import datetime
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

RESULT_JSON = "./jsons/sample01.json"
PATH_MOVIE  = "../assets/movies/sample01.mp4"

# JSON
with open(RESULT_JSON) as j:
	jsonObj = json.load(j)

jsonData = jsonObj["data"]
for n in range(len(jsonData)):
	frame = jsonData[n]["frame"]
	x = int(jsonData[n]["x"])
	y = int(jsonData[n]["y"])
	#print("%s, %d, %d" % (frame, x, y))

# Movie
cap_from = cv2.VideoCapture(PATH_MOVIE)# Movie
W     = int(cap_from.get(cv2.CAP_PROP_FRAME_WIDTH))# Width
H     = int(cap_from.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height
COUNT = int(cap_from.get(cv2.CAP_PROP_FRAME_COUNT))# Count
FPS   = int(cap_from.get(cv2.CAP_PROP_FPS))# Fps
print("Video W:%d H:%d COUNT:%d FPS:%d" % (W, H, COUNT, FPS))

# Line, Font
l_color = (255, 255, 255)
l_width = 1
f_style = cv2.FONT_HERSHEY_DUPLEX
f_scale = 1
f_color = (255, 100, 100)

fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
cap_to = cv2.VideoWriter("result.mp4", fourcc, FPS, (W, H))

for n in range(COUNT):
	ret, frame = cap_from.read()# Read
	if not ret: break
	if n < len(jsonData):
		c_frame = str(jsonData[n]["frame"])
		c_center = (int(jsonData[n]["x"]), int(jsonData[n]["y"]))
		cv2.putText(frame, c_frame, c_center, f_style, f_scale, f_color)
		cv2.circle(frame, c_center, 48, l_color, l_width)
	cap_to.write(frame)# Write

cap_from.release()
cap_to.release()