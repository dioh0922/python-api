import numpy as np
import chainer
import glob
import random
import matplotlib.pyplot as plt
from PIL import Image
from chainer import cuda, Function, \
	report, training, utils, Variable
from chainer import datasets, iterators, optimizers
from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L
import chainer.serializers as S
from chainer.training import extensions
from chainer.datasets import LabeledImageDataset
from chainer.datasets import TransformDataset
from chainer.training import extensions
from chainer.datasets import tuple_dataset
import datetime

import sys
import io
import os


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, "UTF-8")

print("python start")
