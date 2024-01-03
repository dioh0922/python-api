
import base64
from io import BytesIO
from PIL import Image
import numpy as np

def image_decode_base64(base64_data):

    if not base64_data:
        return None

    # base64で画像データが送られるためデコードする
    if "base64," in base64_data:
        base64_data = base64_data.split(",")[1]

    img = Image.open(BytesIO(base64.b64decode(base64_data)))
    return img

def rgb_split(img):
	img = img.resize((50, 50))
	r,g,b = img.split()
	rImgData = np.asarray(np.float32(r) / 255)
	gImgData = np.asarray(np.float32(g) / 255)
	bImgData = np.asarray(np.float32(b) / 255)

	split_img = np.asarray([rImgData, gImgData, bImgData])
	return split_img
