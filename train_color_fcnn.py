import tensorflow as tf
from keras.layers import concatenate
from tensorflow.keras import models, layers
import numpy as np
from tensorflow.python.keras.utils.np_utils import to_categorical
from color_prel import my_pill_color
color_map = {
    'BLACK': 0, 'WHITE': 1, 'GRAY': 2, 'RED': 3, 'ORANGE': 4,
    'BROWN': 5, 'YELLOW': 6, 'GREEN': 7, 'TURQUOISE': 8,
    'BLUE': 9, 'PURPLE': 10, 'PINK': 11
}
classes =[
    'BLACK', #0
    'WHITE', #1
    'GRAY',  #2
    'RED',   #3
    'ORANGE',#4
    'BROWN', #5
    'YELLOW',#6,
    'GREEN', #7
    'TURQUOISE', #8
    'BLUE', #9
    'PURPLE', #10
    'PINK' #11
]

def train_fcnn(train_split=0.5):
    ds_all = tf.data.Dataset.load("./dataset_pastile_culoare")
    train_size = int(train_split * 4392)
    ds_train = ds_all.take(train_size)
    ds_test = ds_all.skip(train_size)

    x1_train,x2_train, y1_train,y2_train = [], [], [], []
    x1_test, x2_test, y1_test, y2_test  = [], [], [], []

    for x1,x2, y1,y2 in ds_train:
        #string-urile rgb sunt transformate in liste, iar fiecare element este normalizat la 255
        x1_list = [float(val)/255 for val in x1.numpy().decode('utf-8').split(',')]
        x2_list = [float(val)/255 for val in x2.numpy().decode('utf-8').split(',')]
        y1_train.append(y1.numpy())
        y2_train.append(y2.numpy())
        x1_train.append(x1_list)
        x2_train.append(x2_list)


    for x1, x2, y1, y2 in ds_test:
        x1_list = [float(val)/255 for val in x1.numpy().decode('utf-8').split(',')]
        x2_list = [float(val)/255 for val in x2.numpy().decode('utf-8').split(',')]
        y1_test.append(y1.numpy())
        y2_test.append(y2.numpy())
        x1_test.append(x1_list)
        x2_test.append(x2_list)

#VAR2
    input_train = np.concatenate([x1_train, x2_train], axis=1)
    input_test = np.concatenate([x1_test, x2_test], axis=1)
    output1_train = np.array(y1_train)  # Primele 3 clase
    output2_train = np.array(y2_train)  # Ultimele 3 clase
    output1_test = np.array(y1_test)
    output2_test = np.array(y2_test)

    inputs = layers.Input(shape=(6,))
    x = layers.Dense(128, activation='relu')(inputs)
    x = layers.Dense(64, activation='relu')(x)

    output1 = layers.Dense(12, activation='softmax', name="output1")(x)  # 3 clase
    output2 = layers.Dense(12, activation='softmax', name="output2")(x)  # 3 clase

    model = models.Model(inputs=inputs, outputs=[output1, output2])

    model.compile(
        optimizer='adam',
        loss={'output1': 'sparse_categorical_crossentropy', 'output2': 'sparse_categorical_crossentropy'},
        metrics={'output1': 'accuracy', 'output2': 'accuracy'}
    )

    model.fit(input_train,{'output1': output1_train, 'output2': output2_train},
        batch_size=128,
        epochs=50
    )
    print("Evaluare fcnn pe imagini de test")
    model.evaluate(
        input_test,
        {'output1': output1_test, 'output2': output2_test},
        batch_size=128
    )

    print("Salvare fcnn")
    model.save(".\\fcnn_color\\fcnn.h5")


def prepare_input(color1, color2):
    color1_normalized = [float(val)/255 for val in color1]
    color2_normalized = [float(val)/255  for val in color2]
    input_data = np.concatenate([color1_normalized, color2_normalized], axis=0)  # (6,)
    input_data = np.array(input_data).reshape(1, 6)
    return input_data


def get_color_prediction(fcnn, img):
    color1,color2=my_pill_color(img)

    input=prepare_input(color1,color2)
    pred = fcnn.predict(input, verbose=0)

    pred1=np.argmax(pred[0],axis=1)
    pred2=np.argmax(pred[1],axis=1)
    if(classes[pred1[0]]==classes[pred2[0]]):
        return classes[pred1[0]]
    else:
        return classes[pred1[0]]+','+classes[pred2[0]]

def get_fcnn(path=".\\fcnn_color\\fcnn.h5"):
    fcnn = tf.keras.models.load_model(path)
    return fcnn

import PIL as pil
def readImage(path):
    img = np.asarray(pil.Image.open(path))
    return img

def main():
    train_fcnn()

    # print(get_color_prediction(fcnn, color))
if __name__ == '__main__':
    main()