# coding: utf-8
from my_modules.movie_analysis import MovieCapture, MovieExporter

# MovieCapture
# 映像から円を判定し、JSONファイルに座標を書き出す
# m_capture = MovieCapture()
# m_capture.capture("../movies/sample_user_01.mp4", "user_01", 1)
# m_capture.capture("../movies/sample_user_02.mp4", "user_02", 1)
# m_capture.capture("../movies/sample_user_03.mp4", "user_03", 1)

# MovieExporter
# JSONから座標を取得して動画へ描画する
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
mp4_input  = "../movies/sample_original.mp4"# 合成元のファイル
mp4_frames = "./result_frames.mp4"# フレームのみのファイル
mp4_output = "./result_output.mp4"# 音声合成後のファイル

m_exporter = MovieExporter()
m_exporter.exportMovie(mp4_input, mp4_frames, json_list, color_list)
m_exporter.exportSound(mp4_input, mp4_frames, mp4_output)