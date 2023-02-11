from flask import Flask
from flask import request
from markovify_module import sentence_module

app = Flask(__name__)

@app.route("/generate_sentence_api", methods=["POST"])
def generate_api():
	model = sentence_module.generate_model(request.values.get("lang"))
	return model.make_sentence().replace(" ", "")

if __name__ == "__main__":
	app.run()
