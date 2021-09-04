#!/usr/local/bin/python3
#_*_ coding: utf-8 _*__

#from janome.tokenizer import Tokenizer		#品詞分解用モジュール
import janome
import markovify					#マルコフ連鎖で文章を生成するライブラリ
import sys
import io
import os

tokenizer = janome.Tokenizer()
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, "UTF-8")
#train_file = "./sonshi_jpn_pick.txt"

#model = sentence_module.generate_model(train_file)
#print(model.make_sentence().replace(" ", ""))

print("::done")
