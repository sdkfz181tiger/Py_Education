# coding: utf-8

import cv2
import datetime
import ffmpeg
import json
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# MovieCapture
class MovieCapture:
	mp4_path    = ""
	dir_prefix  = ""
	mov_cap     = None
	mov_w       = 0
	mov_h       = 0
	mov_count   = 0
	mov_fps     = 0
	json_obj    = {}

	def __init__(self):
		print("MovieCapture")

	def capture(self, mp4_path, dir_prefix, off=1):
		print("capture %s -> %s" % (mp4_path, dir_prefix))
		self.mp4_path   = mp4_path
		self.dir_prefix = dir_prefix
		self.mov_cap    = cv2.VideoCapture(mp4_path)# Movie
		self.mov_w      = int(self.mov_cap.get(cv2.CAP_PROP_FRAME_WIDTH))# Width
		self.mov_h      = int(self.mov_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height
		self.mov_count  = int(self.mov_cap.get(cv2.CAP_PROP_FRAME_COUNT))# Count
		self.mov_fps    = int(self.mov_cap.get(cv2.CAP_PROP_FPS))# Fps
		self.json_obj    = json.loads('{"data":[]}');
		print("Video W:%d H:%d COUNT:%d FPS:%d" % (self.mov_w, self.mov_h, self.mov_count, self.mov_fps))
		self.analyze(off)# Analyze
		self.mov_cap.release()# Release

	def analyze(self, off=1, ext_png="png", ext_json="json"):
		print("Analyze...")
		if not self.mov_cap.isOpened(): return
		dir_name = os.path.join("out", self.dir_prefix)
		print("Make directory... %s" % (dir_name))
		os.makedirs(dir_name, exist_ok=True)# Directory
		digit = len(str(int(self.mov_count)))

		# To Frame
		for n in range(self.mov_count):
			ret, frame = self.mov_cap.read()# Read
			if not ret: break
			if n%off!=0: continue# Offset
			file_name_png = "{}.{}".format(str(n).zfill(digit), ext_png)
			path_png = os.path.join(dir_name, file_name_png)
			self.writeFrame(n, path_png, frame)

		# To Json
		file_name_json = "result.{}".format(ext_json)
		path_json = os.path.join(dir_name, file_name_json)
		self.dumpJson(path_json)

	def writeFrame(self, n, path, frame):
		#print("writeFrame %s" % path)

		bgr_lower  = np.array([0, 0, 180])
		bgr_upper  = np.array([50, 50, 255])
		img_mask   = cv2.inRange(frame, bgr_lower, bgr_upper)
		img_target = cv2.bitwise_and(frame, frame, mask=img_mask)
		img_gray   = cv2.cvtColor(img_target, cv2.COLOR_BGR2GRAY)

		_, threshold = cv2.threshold(img_gray, 20, 255, cv2.THRESH_BINARY)
		contours, _  = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		l_color = (255, 255, 255)
		l_width = 1
		f_style = cv2.FONT_HERSHEY_DUPLEX
		f_scale = 1
		f_color = (255, 255, 255)

		found = False
		for cnt in contours:
			(x, y), radius = cv2.minEnclosingCircle(cnt)
			center = (int(x), int(y))
			if radius > 20:
				approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
				cv2.drawContours(img_gray, [approx], 0, l_color, l_width)
				cv2.putText(img_gray, "circle", center, f_style, f_scale, f_color)
				self.json_obj["data"].append({"frame": n, "x": int(x), "y": int(y)})# Found
				found = True
				break
		if not found: self.json_obj["data"].append({"frame": n, "x": 0, "y": 0})# Not found
		#cv2.imwrite(path, img_gray)# Image

	def dumpJson(self, path):
		print("dumpJson %s" % path)
		with open(path, "w") as file:
			json.dump(self.json_obj, file, indent=2)

	def get_dir_name(self):
		d_obj   = datetime.datetime.now()
		s_year  = str(d_obj.year).zfill(4)
		s_month = str(d_obj.month).zfill(2)
		s_day   = str(d_obj.day).zfill(2)
		s_hour  = str(d_obj.hour).zfill(2)
		s_min   = str(d_obj.minute).zfill(2)
		s_sec   = str(d_obj.second).zfill(2)
		return "out_{}{}{}_{}{}{}".format(s_year, s_month, s_day, s_hour, s_min, s_sec)

# MovieExporter
class MovieExporter:

	def __init__(self):
		print("MovieExporter")
		
	def exportMovie(self, mp4_from, mp4_to, json_list, color_list):

		mov_cap   = cv2.VideoCapture(mp4_from)# Movie
		mov_w     = int(mov_cap.get(cv2.CAP_PROP_FRAME_WIDTH))# Width
		mov_h     = int(mov_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height
		mov_count = int(mov_cap.get(cv2.CAP_PROP_FRAME_COUNT))# Count
		mov_fps   = int(mov_cap.get(cv2.CAP_PROP_FPS))# Fps
		print("Video W:%d H:%d COUNT:%d FPS:%d" % (mov_w, mov_h, mov_count, mov_fps))

		# Json
		json_objs = []
		for l in range(len(json_list)):
			print(json_list[l])
			with open(json_list[l]) as j:
				json_objs.append(json.load(j))

		# Line, Font
		l_color = (255, 255, 255)
		l_width = 4
		f_style = cv2.FONT_HERSHEY_DUPLEX
		f_scale = 1
		f_color = (255, 255, 255)

		fourcc  = cv2.VideoWriter_fourcc("m", "p", "4", "v")
		cap_out = cv2.VideoWriter(mp4_to, fourcc, mov_fps, (mov_w, mov_h))

		for n in range(mov_count):
			ret, frame = mov_cap.read()# Read
			if not ret: break
			for o in range(len(json_objs)):
				json_data = json_objs[o]["data"]
				if n < len(json_data):
					c_frame  = str(json_data[n]["frame"])
					c_center = (int(json_data[n]["x"]), int(json_data[n]["y"]))
					cv2.putText(frame, c_frame, c_center, f_style, f_scale, f_color)
					cv2.circle(frame, c_center, 48, color_list[o], l_width)

			cap_out.write(frame)# Write

		mov_cap.release()# Release
		cap_out.release()

	def exportSound(self, mp4_from_a, mp4_from_b, mp4_to):

		input_a = ffmpeg.input(mp4_from_a)
		input_b = ffmpeg.input(mp4_from_b)
		stream = ffmpeg.output(input_a.audio, input_b, mp4_to, vcodec="copy", acodec="aac")
		ffmpeg.run(stream)



