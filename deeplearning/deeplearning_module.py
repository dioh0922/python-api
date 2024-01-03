
from deeplearning.MyChain import MyChain
import datetime
import chainer
from chainer.datasets import tuple_dataset
from chainer import cuda, Function, \
	report, training, utils, Variable
from util import util_module
import numpy as np


def img_identify(img):
    dt_st = datetime.datetime.now()

    model = MyChain()
    chainer.serializers.load_npz('./deeplearning/trained_model/check_soy.net', model)

    split_data = util_module.rgb_split(img)

    img_arr = []
    class_id = []

    img_arr.append(split_data)
    class_id.append(0)

    test = tuple_dataset.TupleDataset(img_arr, class_id)

    x = Variable(np.array([test[0][0]], dtype=np.float32))

    result = model.fwd(x)	#画像をモデルに通す

    classifier = np.argmax(result.data)		#一番大きいものをクラスと識別する

    identify_result = ""    
    if classifier == 0:
        identify_result = "醤油(密閉ボトル)に見える"
    elif classifier == 1:
        identify_result = "醤油(昔のボトル)に見える"
    elif classifier == 2:
        identify_result = "めんつゆに見える"
    else :
        identify_result = "識別に失敗しました"

    return identify_result
