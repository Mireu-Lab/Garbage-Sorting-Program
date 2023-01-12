# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf

com_models = tf.keras.models.load_model('Data/ai_models')

images_categories = ['metal', 'glass', 'paper', 'trash', 'cardboard', 'plastic']

def model_run_main(file_path):
    img=tf.keras.preprocessing.image.load_img(file_path, target_size=(512, 384))

    x=tf.keras.preprocessing.image.img_to_array(img)
    x=np.expand_dims(x, axis=0)
    images = np.vstack([x])

    classes = com_models.predict(images, batch_size=10)
    
    a = 0
    
    for images_categorie in images_categories:
        # print(classes[0][a], images_categorie)
        a += 1
    
    b = 0
    for images_categorie in images_categories:
        if classes[0][b] == 1:
            return {images_categorie:int(classes[0][b])}
        b += 1