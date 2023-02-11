import sentence_module

def generate_markov(lang):
	model = sentence_module.generate_model(lang)
	print(model.make_sentence().replace(" ", ""))
