import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class Preprocessing:
    def __init__(self):
        self.data_dir = os.path.join(os.path.dirname(__file__), '../data')

    def image_enhancement(self, file):
        img_array = np.fromstring(file, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (128, 128))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.GaussianBlur(img, (5, 5), 0)

        img = tf.convert_to_tensor(img, dtype=tf.uint8)
        img = tf.expand_dims(img, axis=0)
        
        return img

    def data_generator(self, path):
        test_datagen = ImageDataGenerator()
        batch_size = 32

        test_generator = test_datagen.flow_from_directory(
            path,
            target_size=(128, 128),
            color_mode="rgb",
            shuffle = False,
            class_mode='categorical',
            batch_size=batch_size)

        labels = test_generator.classes
        filenames = test_generator.filenames
        nb_samples = np.ceil(len(filenames)/batch_size)

        return test_generator, nb_samples, labels