import sys
import io
import os

from PIL import Image
from PIL import ImageFilter
import pyocr
import pyocr.builders
import json
import base64
from io import ByteIO
import jaconv

# base64で送られた画像をデコードする
def decode_base64_to_image():
    json_data = request.get_json()
    dict_data = json.loads(json_data)
    img = dict_data["upload_img"]
    return img


