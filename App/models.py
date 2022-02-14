# -*- coding: utf-8 -*-
from keras.preprocessing import image
from tensorflow import keras
import tensorflow as tf
import pathlib
import keras
import numpy as np

# data_dir = tf.keras.utils.get_file(origin="http://mireu-server.iptime.org:8000/list/HDD2/hana/Garbage_images.tar.gz", fname="Garbage_images", untar=True)
data_dir = pathlib.Path("/home/mireu/.keras/datasets/Garbage_images")

image_count = len(list(data_dir.glob('*/*.jpg')))
images_categories = ['metal', 'glass', 'paper', 'trash', 'cardboard', 'plastic']

IMAGE_SIZE = (100, 100)
BATCH_SIZE = 16

train_dataset = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    subset= "training",
    validation_split = 0.2,
    seed=1,
    image_size = IMAGE_SIZE,
    batch_size = BATCH_SIZE,
    label_mode = "categorical",
    class_names = images_categories
)

test_dataset = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    subset= "validation",
    validation_split = 0.2,
    seed=1,
    image_size = IMAGE_SIZE,
    batch_size = BATCH_SIZE,
    label_mode = "categorical",
    class_names = images_categories
)

INPUT_SHAPE = IMAGE_SIZE + (3,)

model = keras.Sequential([
    keras.Input(shape=INPUT_SHAPE),

    keras.layers.Rescaling(1.0/255),
    keras.layers.Flatten(),
    
    keras.layers.Dense(512, activation="relu"),
    keras.layers.Dropout(0.2, noise_shape=None, seed=1),
    
    keras.layers.Dense(256, activation="relu"),
    keras.layers.Dropout(0.1, noise_shape=None, seed=1),
    
    keras.layers.Dense(512, activation="relu"),
    keras.layers.Dense(len(images_categories), activation = "softmax")
])

model.build(IMAGE_SIZE)
model.summary()

optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001)
model.compile(loss = "categorical_crossentropy", optimizer=optimizer, metrics=["accuracy"])

history = model.fit(
    train_dataset,
    epochs=25,
    shuffle=True,
    verbose=1,
    validation_data=test_dataset
)

def model_run_main(file_path):
    img=image.load_img(file_path, target_size=(100, 100))

    x=image.img_to_array(img)
    x=np.expand_dims(x, axis=0)
    images = np.vstack([x])

    classes = model.predict(images, batch_size=10)

    print(classes[0])

    a = 0
    for images_categorie in images_categories:
        # print(classes[0][a], images_categorie)

        if classes[0][a] > 0:
            print(classes[0][a], images_categorie)
        else:
            pass
        
        a = a + 1
