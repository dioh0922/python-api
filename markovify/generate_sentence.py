#!/usr/local/bin/python3
#_*_ coding: utf-8 _*__

import sentence_module
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, "UTF-8")

args = sys.argv
if len(args) < 2:
	print("引数が少なすぎます")
	exit(1)

train_file = args[1]

model = sentence_module.generate_model(train_file)
print(model.make_sentence().replace(" ", ""))
