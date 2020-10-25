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