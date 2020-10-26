# coding: utf-8

"""
1, pyenvインストール
	brew install pyenv
2, .bash_profileに追記
	# Python
	export PYENV_ROOT="$HOME/.pyenv"
	export PATH="$PYENV_ROOT/bin:$PATH"
	eval "$(pyenv init -)"
3, インストールできるバージョン
	pyenv install --list
4, インストール
	pyenv install 3.8.0
5, インストール済のバージョン
	pyenv versions
6, バージョンを有効にする
	pyenv global 3.8.0
7, バージョン確認
	python -V
8, ファイル実行
	python xxx.py
"""

# Comment
print("Hello World!!")

# 定数
MY_MSG = "Hoge"
print(MY_MSG)

# 変数
my_msg = "Fuga"
print(my_msg) 

# 複数行
my_html = """
<html>
	<head>
		<title>Welcome</title>
	</head>
	<body>
		<p1>Welcome</p>
	</body>
</html>
"""
print(my_html)

# 数値, 小数, 論理
i = 12
f = 34.5
b = True # False