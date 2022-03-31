# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf

com_models = tf.keras.models.load_model('Data/ai_models')

def model_run_main(file_path):
    img=tf.keras.preprocessing.image.load_img(file_path, target_size=(100, 100))

    x=tf.keras.preprocessing.image.img_to_array(img)
    x=np.expand_dims(x, axis=0)
    images = np.vstack([x])

    classes = com_models.predict(images, batch_size=10)

    return classes[0]