#!/usr/local/bin/python3
#_*_ coding: utf-8 _*__

from janome.tokenizer import Tokenizer		#品詞分解用モジュール
import markovify					#マルコフ連鎖で文章を生成するライブラリ

#教師データのファイルを指定して文章を生成する処理
def generate_model(f_name):
	#現代語訳の孫子全文を読み出す
	text = read_file_text(f_name)
	tokenizer = Tokenizer()
	str = split_part_of_speach(text)

	model = markovify.NewlineText(str)	#1行ごとに読んでマルコフ連鎖のモデルとする

	return model

#品詞分解してスペースで区切った文字列を返す処理
def split_part_of_speach(text):
	tokenizer = Tokenizer()
	str = ""
	for token in tokenizer.tokenize(text):
		if token.surface == "。":	#。で1行とする
			str += "\n"
		elif token.surface != "\n":
			str += token.surface
			str += " "	#スペースで品詞ごとに区切る

	return str

#ファイルを読み出す処理
def read_file_text(f_name):
	with open(f_name, encoding="utf-8") as fs:
		text = fs.read()

	return text
