from flask import Flask, render_template
from flask import request
from module.markov import sentence_module
from module.ocr import ocr_module
from module.util import util_module
from module.deeplearning import deeplearning_module

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/markovify")
def markovify():
    return render_template("markovify.html")

@app.route("/markovify/generate_sentence_api", methods=["POST"])
def generate_api():
    model = sentence_module.generate_model(request.values.get("lang"))
    return model.make_sentence().replace(" ", "")

@app.route("/ocr")
def ocr_top():
    return render_template("ocr.html")

@app.route("/ocr/get_title_api", methods=["POST"])
def ocr_detect():
    json_data = request.values.get("upload_img")
    request_img = util_module.image_decode_base64(json_data)
    if not request_img:
        result = "invalid img"
    else:
        result = ocr_module.detect_title(request_img)

    return result

@app.route("/ocr/get_image_api", methods=["POST"])
def search_google_image():
    search_word = request.values.get("search_word")
    return ocr_module.search_word_image(search_word)

@app.route("/chainer")
def chainer():
    return render_template("chainer.html")

@app.route("/chainer/identify_api", methods=["POST"])
def identify_img():
    json_data = request.values.get("upload_img")
    request_img = util_module.image_decode_base64(json_data)
    if not request_img:
        result = "invalid img"
    else:
        result = deeplearning_module.img_identify(request_img)
    
    return result


@app.route("/requirement")
def check_requirement():
    import pkgutil
    str = ""
    for m in pkgutil.iter_modules():
        str += m.name
        str += "<br>"
    return str

if __name__ == "__main__":
    app.run()
