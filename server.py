from flask import Flask, render_template
from flask import request
from markovify_module import sentence_module
from ocr_module import ocr_module

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
	return ocr_module.detect_title(json_data)

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
