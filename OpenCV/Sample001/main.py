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

img_orig     = cv2.imread("./images/sample_1.png", cv2.IMREAD_GRAYSCALE)# グレースケール
_, threshold = cv2.threshold(img_orig, 240, 255, cv2.THRESH_BINARY)# 閾値を設定
contours, _  = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)# 輪郭を抽出
font = cv2.FONT_HERSHEY_DUPLEX# フォントを指定

for cnt in contours:
	approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
	cv2.drawContours(img_orig, [approx], 0, (0), 2)
	x = approx.ravel()[0]
	y = approx.ravel()[1]
	if len(approx) > 10:
		cv2.putText(img_orig, "circle", (x, y), font, 1, (0))

cv2.imwrite("./images/result.png", img_orig)# 画像を出力