import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adagrad

imgfile_dir = "../archive/garbage classification/Garbage classification/"

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

classes = os.listdir(imgfile_dir)

SIZE = 128

# configuracion de entrenamiento
entrenamiento_datagen = ImageDataGenerator(rescale = 1./255)

# generador
generador_entrenamiento = entrenamiento_datagen.flow_from_directory(
    imgfile_dir,
    target_size=(SIZE,SIZE),
    batch_size=128,
    class_mode='binary'
)

data_augmentation = keras.Sequential(
    [
        layers.experimental.preprocessing.RandomFlip("horizontal"),
        layers.experimental.preprocessing.RandomRotation(0.5),
    ]
)

model = tf.keras.models.Sequential([
    # Note the input shape is the desired size of the image SIZExSIZE with 3 bytes color
    tf.keras.layers.Dense(50, activation='relu', input_shape=(128, 128, 3)),
    # This is the first convolution
    tf.keras.layers.Conv2D(50, (3,3), activation='relu'),
    tf.keras.layers.SpatialDropout2D(0.5),
    tf.keras.layers.MaxPooling2D(2, 2),
     # This is the first convolution
    tf.keras.layers.Conv2D(50, (3,3), activation='relu'),
    tf.keras.layers.SpatialDropout2D(0.5),
    tf.keras.layers.MaxPooling2D(2, 2),
    # Flatten the results to feed into a DNN
    tf.keras.layers.Flatten(),
    # 512 neuron hidden layer
    tf.keras.layers.Dense(200, activation='relu'),
    tf.keras.layers.Dense(100, activation='relu'),
    # Only 1 output neuron. It will contain a value from 0-1 where 0 for 1 class ('horses') and 1 for the other ('humans')
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy',
              optimizer=Adagrad(learning_rate=0.1),
              metrics=['accuracy'])

history = model.fit(
    generador_entrenamiento,
    steps_per_epoch=20,  
    epochs=30,
    verbose=1
)

score = model.evaluate_generator (generador_entrenamiento,verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

conclusion_model = keras.Sequential([model, keras.layers.Softmax()])
conclusion = conclusion_model.predict(test_images)