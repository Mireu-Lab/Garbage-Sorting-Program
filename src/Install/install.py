import tensorflow as tf

print(tf.keras.utils.get_file(origin="http://mireu-server.iptime.org:8000/list/HDD1/hana/Garbage_Images.tar.gz", fname="Garbage_Images", untar=True))
