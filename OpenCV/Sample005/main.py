# coding: utf-8

"""
1, numpy, opencvインストール
	pip install numpy
	pip install opencv-python
	pip install pillow
	pip install matplotlib
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img_orig   = cv2.imread("./images/sample_1.png")# 画像の読み込み
bgr_lower  = np.array([0, 100, 180])# 抽出する色の下限(BGR)
bgr_upper  = np.array([80, 180, 255])# 抽出する色の上限(BGR)
img_mask   = cv2.inRange(img_orig, bgr_lower, bgr_upper)# BGRからマスクを作成
img_target = cv2.bitwise_and(img_orig, img_orig, mask=img_mask)
img_gray   = cv2.cvtColor(img_target, cv2.COLOR_BGR2GRAY)# グレイカラー

_, threshold = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)# 閾値を設定
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