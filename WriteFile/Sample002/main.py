# coding: utf-8

import json
from collections import OrderedDict
import pprint

FILE_NAME = "test.txt"

text = "Hello, how are you?"
file = open(FILE_NAME, "w")
file.write(text)
file.close();

# 動画の読み込み
video = cv2.VideoCapture("./movies/apple.mp4")
# 幅
W = video.get(cv2.CAP_PROP_FRAME_WIDTH)
# 高さ
H = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
# 総フレーム数
count = video.get(cv2.CAP_PROP_FRAME_COUNT)
# fps
fps = video.get(cv2.CAP_PROP_FPS)


