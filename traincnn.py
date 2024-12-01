import cv2 as cv
import os

from matplotlib import pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow.keras import models, layers
import numpy as np
import background_fct as bg

#clasele de pastile
classes = [
 "CAPSULE", #0
 "OVAL", #1
 "TEAR", #2
 "ROUND", #3
 "HEXAGON", #4
 "SQUARE", #5
 "TRIANGLE", #6
 "PENTAGON", #7
 "DIAMOND", #8
 "RECTANGLE", #9
 "SEMI-CIRCLE", #10
 "DOUBLE CIRCLE", #11
 "TRAPEZOID", #12
 "FREEFORM", #13
 "OCTAGON", #14
 "BULLET" #15
]

def get_cnn(path="./CNN/cnn.h5"):
    cnn = tf.keras.models.load_model(path)
    return cnn

def get_shape_prediction(CNN, img):
    y_pred = CNN.predict(img)
    y_classes = np.argmax(y_pred)
    print(classes[y_classes])
    return classes[y_classes]

def prepare_image(img):
    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    mask = bg.masca_pastila(img)
    img = bg.contur_pastila(img, mask)
    plt.figure()
    plt.imshow(img, cmap='gray')
    plt.show()
    # adaugare dimensiune pt canal
    img = np.expand_dims(img, axis=-1)
    # convert la float32
    img = img.astype(np.float32)

    # extindere dimensiuni ca sa se potriveasca cu imputul cnn-ului
    img = np.expand_dims(img, axis=0)
    return img


def train_cnn(train_split=0.5):
    # incarcare dataset din fisier
    ds_all = tf.data.Dataset.load("./dataset_pastile")
    train_size = int(train_split * 4392)
    ds_train = ds_all.take(train_size) #impartire dataset in date de antrenament si date de test
    ds_test = ds_all.skip(train_size)

    # impartire in imagini + label-uri
    x_train, y_train, x_test, y_test = [], [], [], []
    for x, y in ds_train:
        x_train.append(x.numpy())
        y_train.append(y.numpy())
    for x, y in ds_test:
        x_test.append(x.numpy())
        y_test.append(y.numpy())

    # Convert la array numpy
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_test = np.array(x_test)
    y_test = np.array(y_test)

    # arhitectura CNN
    cnn = models.Sequential([
        layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(120, 120, 1)),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(len(classes), activation='softmax'),
    ])

    cnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    cnn.fit(x_train, y_train, epochs=10, batch_size= 128) #antrenare cnn

    print("Evaluare cnn pe imagini de test ")
    cnn.evaluate(x_test, y_test, batch_size=128) #evaluare pe datele de test

    print("Salvare cnn")
    cnn.save(".\\cnn\\cnn.h5") #salvare cnn
    return cnn
