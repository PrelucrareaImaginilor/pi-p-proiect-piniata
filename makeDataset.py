import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import pandas as pd
import background_fct as bg
import numpy as np
import PIL as pil
import cv2 as cv

def generare_dataset():
    directory = '.\\ds\\'
    df = pd.read_csv(directory + 'shapes1.csv')
    file_paths = df['file_name'].values
    labels = df['label'].values

    def read_image(image_file, label):
        def _process_image(image_file_str):
            image_path = directory + image_file_str.numpy().decode('utf-8')
            imagenp = np.asarray(pil.Image.open(image_path))  # .resize((120, 120)))
            imagenp = imagenp[59:119, :]
            imagenp = cv.bilateralFilter(imagenp, 3, 60, 60)
            imagenp = cv.Canny(imagenp, 45, 200)
            imagenp = np.expand_dims(imagenp, axis=-1)
            return imagenp.astype(np.float32)

        image = tf.py_function(_process_image, [image_file], tf.float32)
        return image, label

    ds_all = tf.data.Dataset.from_tensor_slices((file_paths, labels))
    ds_all = ds_all.map(read_image)
    ds_all.save('./dataset_pastile')

def generate_ds_color():
    directory = '.\\ds\\'
    df = pd.read_csv(directory + 'colors.csv')
    color1 = df['color1'].values
    color2 = df['color2'].values
    rgb1= df['rgb1'].values
    rgb2 = df['rgb2'].values

    ds_all = tf.data.Dataset.from_tensor_slices((rgb1, rgb2,color1,color2))
    ds_all.save('./dataset_pastile_culoare')

