#!/usr/local/bin/python3
#_*_ coding: utf-8 _*__

import sys
import io
import os
import requests
from bs4 import BeautifulSoup
import random

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, "UTF-8")

args = sys.argv

#引数チェック ファイル名を指定する
if 2 > len(args):
	print("引数が少なすぎます")
	exit(1)

search_word = args[1]

Res = requests.get("https://www.google.com/search?hl=jp&q=" + search_word + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
Html = Res.text
Soup = BeautifulSoup(Html,'lxml')
links = Soup.find_all("img")
i = 2
flg = 0
length = len(links)
str = ""
while(flg < 3):
	str = links[i].get("src")
	if str is not None:
		print(str+"<br>")
		flg = flg + 1
	i = i + 1
	if i >= length:
		exit()
