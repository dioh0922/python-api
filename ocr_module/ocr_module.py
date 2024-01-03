import sys
import io
import os

from PIL import Image
from PIL import ImageFilter
import pyocr
import pyocr.builders
import json
import base64
from io import BytesIO
import jaconv
import requests
from bs4 import BeautifulSoup
import random

threshold = 100		#2値化するしきい値 経験的に50あたりが文字の印字部分

#2値化の画素値の指定用定数
IMAGE_BLACK = 0
IMAGE_WHITE = 255

#テストケースで誤識別していた文字列の補正用配列
DICTIONARY = {
    "言己": "記",
    "カ\"" : "ガ",
    "宇)" : "字)",
    "宇）": "字)",
    "幼安": "幼女",
    "培場": "劇場",
    "耆己": "記",
    "ハ0": "パ",
    "剖場": "劇場",
    "刀メ": "カメ",
    "亘": "!",	#「亘」はタイトルに常用されないと想定
    "-" : "ー"
}


# 画像から文字列を抽出する
def detect_title(img):

    if not img:
        return "No img"

    # チケットの下地を除去するために2値化画像にする
    gray_img = img.convert("L")
    bin_img = gray_img.point(lambda x: IMAGE_BLACK if x < threshold else IMAGE_WHITE)
    target = bin_img.filter(ImageFilter.MedianFilter())

    tool = pyocr.get_available_tools()
    result = ""
    if len(tool) == 0:
        # OCRがインストールされていなければエラー
        result = "No OCR"
    else:
        try:
            image = target
            detect = tool[0].image_to_string(image,
                lang="jpn",
                builder=pyocr.builders.TextBuilder(tesseract_layout=6)
                )

            #指定した文字列を辞書に登録してあるパターンに補正する
            proc_txt = jaconv.z2h(detect, digit=True)
            proc_txt = jaconv.h2z(proc_txt, kana=True)
            revision = proc_txt.replace(" ", "")

            for i in DICTIONARY:
                revision = revision.replace(i, DICTIONARY[i])

            result += revision

        except Exception as e:
            result += e

    return result

# 検出した文字列で画像検索する
def search_word_image(search_word):
    Res = requests.get("https://www.google.com/search?hl=jp&q=" + search_word + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
    Html = Res.text
    Soup = BeautifulSoup(Html,'lxml')
    links = Soup.find_all("img")
    i = 2
    flg = 0
    length = len(links)
    result = ""

    while(flg < 3):
        search_obj = links[i].get("src")
        if search_obj is not None:
            result += search_obj + "<br>"
            flg = flg + 1
        i += 1
        if i >= length:
            result = "out of range"

    return result
