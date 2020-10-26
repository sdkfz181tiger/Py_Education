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

img_orig  = cv2.imread("./images/sample_1.png")# 画像の読み込み
bgr_lower = np.array([0, 100, 180])# 抽出する色の下限(BGR)
bgr_upper = np.array([80, 180, 255])# 抽出する色の上限(BGR)
img_mask  = cv2.inRange(img_orig, bgr_lower, bgr_upper)# BGRからマスクを作成
img_red   = cv2.bitwise_and(img_orig, img_orig, mask=img_mask)

cv2.imwrite("./images/result.png", img_red)# 画像の出力