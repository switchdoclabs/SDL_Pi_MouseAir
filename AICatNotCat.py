# Artificial Intelligence Cat Not Cat Machine Learning Neural Network
# SDL AUgust 2019
#
#import libraries
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops
from PIL import Image

import state

state.model = tf.keras.models.load_model("CatNotCat.trained",compile=True)

def AnalyzeCatNotCat(pil_img):


    class_names = ["NotCat", "Cat"]


    data = np.asarray( pil_img, dtype="float" )

    data = np.expand_dims(data, axis=0)
    (Cat, NotCat) = state.model.predict(data)[0]

    CatNotCatLevel = Cat*100.0

    

    return CatNotCatLevel


