import sentence_module
import sys
import io
import os

args = sys.argv
if len(args) < 2:
	print("引数が少なすぎます")
	exit(1)

mode = args[1]

model = sentence_module.generate_model(mode)
print(model.make_sentence().replace(" ", ""))
