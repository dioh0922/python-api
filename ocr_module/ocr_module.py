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


# base64で送られた画像をデコードする
def decode_base64_to_image(base64_data):
    if "base64," in base64_data:
        base64_data = base64_data.split(",")[1]

    img = Image.open(BytesIO(base64.b64decode(base64_data)))
    gray_img = img.convert("L")
    bin_img = gray_img.point(lambda x: IMAGE_BLACK if x < threshold else IMAGE_WHITE)

    target = bin_img.filter(ImageFilter.MedianFilter())

    tool = pyocr.get_available_tools()
    str = ""
    if len(tool) == 0:
        str = "No OCR"
    else:
        try:
            image = target
            result = tool[0].image_to_string(image,
                lang="jpn",
                builder=pyocr.builders.TextBuilder(tesseract_layout=6)
                )

            #指定した文字列を辞書に登録してあるパターンに補正する
            proc_txt = jaconv.z2h(result, digit=True)
            proc_txt = jaconv.h2z(proc_txt, kana=True)
            revision = proc_txt.replace(" ", "")

            for i in DICTIONARY:
                revision = revision.replace(i, DICTIONARY[i])

            str += revision

        except Exception as e:
            str += e

    return str

