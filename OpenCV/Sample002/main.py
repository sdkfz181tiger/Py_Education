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

img_orig = cv2.imread("./images/sample_4.png")# 画像の読み込み
hsv_1    = cv2.cvtColor(img_orig, cv2.COLOR_BGR2HSV)# BGR->HSV変換
hsv_2    = np.copy(hsv_1)# コピー
hsv_3    = np.copy(hsv_1)

# h>173の画素のhを-60
hsv_2[:, :, 0] = np.where(hsv_1[:, :, 0]>173, hsv_1[:, :, 0]-60, hsv_1[:, :, 0])
# h<5の画素のhを+120
hsv_3[:, :, 0] = np.where(hsv_2[:, :, 0]<5, hsv_2[:, :, 0]+120, hsv_2[:, :, 0])
bgr = cv2.cvtColor(hsv_3, cv2.COLOR_HSV2BGR)# HSV->BGR変換

cv2.imwrite("./images/result.png", bgr)# 画像を出力