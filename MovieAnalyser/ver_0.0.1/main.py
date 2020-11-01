# coding: utf-8

from my_modules.movie_analysis import MovieCapture, MovieExporter

# MovieCapture
# m_capture = MovieCapture()
# m_capture.capture("../movies/sample_user_01.mp4", "user_01", 1)
# m_capture.capture("../movies/sample_user_02.mp4", "user_02", 1)
# m_capture.capture("../movies/sample_user_03.mp4", "user_03", 1)

# MovieExporter
json_list = [
	"./out/user_01/result.json",
	"./out/user_02/result.json",
	"./out/user_03/result.json"
]
color_list = [
	(255, 100, 100),
	(100, 255, 100),
	(100, 100, 255)
	]
m_exporter = MovieExporter()
m_exporter.export("../movies/sample_original.mp4", json_list, color_list)