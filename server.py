from flask import Flask, render_template
from flask import request
from markovify_module import sentence_module

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

if __name__ == "__main__":
	app.run()
