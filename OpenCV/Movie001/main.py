# coding: utf-8

"""
1, numpy, opencvインストール
	pip install numpy
	pip install opencv-python
	pip install pillow
	pip install matplotlib
"""

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Movie
cap   = cv2.VideoCapture("../movies/sample01.mp4")# Movie
W     = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))# Width
H     = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height
COUNT = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))# Count
FPS   = int(cap.get(cv2.CAP_PROP_FPS))# Fps
print("Video W:%d H:%d COUNT:%d FPS:%d" % (W, H, COUNT, FPS))

def captureFrame(dir, name, ext=".png", off=16):

	if not cap.isOpened(): return
	os.makedirs(dir, exist_ok=True)# Directory
	path = os.path.join(dir, name)
	digit = len(str(int(COUNT)))
	print("saveFrame %s" % path)

	for f in range(COUNT):
		ret, frame = cap.read()# Read
		if ret==False: return
		if f%off!=0: continue
		writeFrame("{}_{}.{}".format(path, str(f).zfill(digit), ext), frame)

def writeFrame(path, frame):

	bgr_lower  = np.array([0, 0, 180])# 抽出する色の下限(BGR)
	bgr_upper  = np.array([50, 50, 255])# 抽出する色の上限(BGR)
	img_mask   = cv2.inRange(frame, bgr_lower, bgr_upper)# BGRからマスクを作成
	img_target = cv2.bitwise_and(frame, frame, mask=img_mask)
	img_gray   = cv2.cvtColor(img_target, cv2.COLOR_BGR2GRAY)# グレイカラー

	_, threshold = cv2.threshold(img_gray, 20, 255, cv2.THRESH_BINARY)# 閾値を設定
	contours, _  = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)# 輪郭を抽出

	l_color = (255, 255, 255)
	l_width = 1
	f_style = cv2.FONT_HERSHEY_DUPLEX
	f_scale = 1
	f_color = (255, 255, 255)

	for cnt in contours:
		(x, y), radius = cv2.minEnclosingCircle(cnt)
		center = (int(x),int(y))
		if radius > 20:
			approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
			cv2.drawContours(img_gray, [approx], 0, l_color, l_width)
			cv2.putText(img_gray, "circle", center, f_style, f_scale, f_color)

	cv2.imwrite(path, img_gray)


captureFrame("out", "sample")# Test
cap.release()# Release

"""
img_orig   = cv2.imread("./images/apple_2.png")# 画像の読み込み
bgr_lower  = np.array([0, 0, 100])# 抽出する色の下限(BGR)
bgr_upper  = np.array([100, 100, 255])# 抽出する色の上限(BGR)
img_mask   = cv2.inRange(img_orig, bgr_lower, bgr_upper)# BGRからマスクを作成
img_target = cv2.bitwise_and(img_orig, img_orig, mask=img_mask)
img_gray   = cv2.cvtColor(img_target, cv2.COLOR_BGR2GRAY)# グレイカラー

_, threshold = cv2.threshold(img_gray, 20, 255, cv2.THRESH_BINARY)# 閾値を設定
contours, _  = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)# 輪郭を抽出

l_color = (255, 255, 255)
l_width = 1
f_style = cv2.FONT_HERSHEY_DUPLEX
f_scale = 1
f_color = (255, 255, 255)

for cnt in contours:
	(x, y), radius = cv2.minEnclosingCircle(cnt)
	center = (int(x),int(y))
	if radius > 20:
		approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
		cv2.drawContours(img_gray, [approx], 0, l_color, l_width)
		cv2.putText(img_gray, "circle", center, f_style, f_scale, f_color)

cv2.imwrite("./images/result.png", img_gray)# 画像の出力
"""

"""
img_orig = cv2.imread("./images/sample_4.png") # 画像の読み出し
hsv_1 = cv2.cvtColor(img_orig, cv2.COLOR_BGR2HSV) # BGR->HSV変換
hsv_2 = np.copy(hsv_1)
hsv_3 = np.copy(hsv_1)

# h>173の画素のhを-60
hsv_2[:, :, 0] = np.where(hsv_1[:, :, 0]>173, hsv_1[:, :, 0]-60, hsv_1[:, :, 0])
# h<5の画素のhを+120
hsv_3[:, :, 0] = np.where(hsv_2[:, :, 0]<5, hsv_2[:, :, 0]+120, hsv_2[:, :, 0])

rbg = cv2.cvtColor(hsv_3, cv2.COLOR_HSV2BGR) # HSV->BGR変換

cv2.imwrite("./images/result.png", rbg) # 画像の保存
"""

"""
# ファイルを読み込み グレースケール化
img_orig = cv2.imread("./images/sample_1.png", cv2.IMREAD_GRAYSCALE)

# 閾値を設定
_, threshold = cv2.threshold(img_orig, 240, 255, cv2.THRESH_BINARY)

# 輪郭を抽出
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_DUPLEX

for cnt in contours:
	approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
	cv2.drawContours(img_orig, [approx], 0, (0), 2)
	x = approx.ravel()[0]
	y = approx.ravel()[1]

	if len(approx) > 10:
		cv2.putText(img_orig, "circle", (x, y), font, 1, (0))   

# 結果の画像作成
cv2.imwrite("./images/output_circle.png", img_orig)
"""

"""
# 色基準で2値化する。
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 色の範囲を指定する
lower_color = np.array([20, 80, 10])
upper_color = np.array([50, 255, 255])

# 指定した色に基づいたマスク画像の生成
mask = cv2.inRange(hsv, lower_color, upper_color)
output = cv2.bitwise_and(hsv, hsv, mask = mask)

cv2.imwrite("./images/result.jpg", output)
Image(filename='./images/result.jpg')
"""