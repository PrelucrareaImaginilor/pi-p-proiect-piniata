from operator import concat

import numpy as np
import PIL as pil
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.pyplot import title
import re
import color_prel
from color_prel import my_pill_color
import traincnn
import train_color_fcnn
import makeDataset
import pandas as pd
import name_clas as nc

def readImage(path):
    img = np.asarray(pil.Image.open(path))
    return img

def fc_afisare(img, title, yaxis='', xaxis=''):
    plt.figure()
    plt.title(title)
    plt.imshow(img, cmap='gray')
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

def main():
    print("Alegere operatiune:")
    print("1. Generare dataset din folderul ds")
    print("2. Antrenare CNN")
    print("3. Predictie")
    print("4. Statistici")
    print("5. Demo")
    choice = input()
    if choice == '1':
        print('Generare dataset din folderul ds...')
        makeDataset.generare_dataset()
        makeDataset.generate_ds_color()

    elif choice == '2':
        print('Antrenare CNN si FCNN...')
        traincnn.train_cnn()
        train_color_fcnn.train_fcnn()
    elif choice == '3':
        print('Predictie...')
        #deschidem imaginea
        temp = readImage("./ds/40.jpg")
        color = temp.copy()

        #incarcam cnn
        cnn = traincnn.get_cnn()
        fcnn=train_color_fcnn.get_fcnn()

        #facem imaginea grayscale
        temp = cv.cvtColor(temp, cv.COLOR_RGB2GRAY)
        img = temp.copy()

        #mascaPastila = bk.masca_pastila(img)
        #contur = bk.contur_pastila(img,mascaPastila) # preluam forma pastilei
        #nobg = bk.eliminare_fundal(img,mascaPastila) #eliminam fundalul

        predicted_color=train_color_fcnn.get_color_prediction(fcnn,color)


        shape = traincnn.prepare_image(color) #pregatim imaginea pt cnn

        predicted_shape = traincnn.get_shape_prediction(cnn, shape)

        nc.find_name(predicted_color,predicted_shape)
        fc_afisare(color, title=f"{predicted_shape} {predicted_color}")

        plt.show()
    elif choice == '4':
        cnn = traincnn.get_cnn()
        df = pd.read_csv('./shapescolors.csv')
        shapes = df['shape'].values
        colors = df['color'].values
        s=0
        c=0
        t = 0
        fcnn=train_color_fcnn.get_fcnn()
        for i in range(1, 4192):#4192):#(2396, 2436):#4192): #imagini pe care nu a invatat
            print(i)
            img = readImage(f"./ds/{i}.jpg")
            #pcolor = my_pill_color(img)
            shimg = traincnn.prepare_image(img)
            pshape = traincnn.get_shape_prediction(cnn, shimg)
            if pshape in shapes[i-1]:
                s = s+1

            pcolor=train_color_fcnn.get_color_prediction(fcnn, img)
            #print(pcolor)
            correct = 0
            # for color in pcolor.split(", "):
            #     if color in colors[i-1]:
            #         correct = correct+1
            clr = [s for s in re.split(r'[ ,]+', colors[i-1]) if s]
            for x in pcolor.replace(",", " ").split(" "):
                print(x)
                if x in clr:
                    correct = correct + 1
            if correct == len(clr):
                c = c + 1

            # fc_afisare(img, pcolor, "", f"{colors[i-1]} {shapes[i-1]}")
            # plt.show()

            t = t+1
        c = c/t
        s = s/t
        print("Testare facuta pe: ", t, " imagini\nAcuratete forma: ", s*100, "%\nAcuratete culoare: ", c*100, "%\n")
    elif choice == '5':
        temp = readImage("./ds/1.jpg")
        cnn = traincnn.get_cnn()
        fcnn = train_color_fcnn.get_fcnn()
        shimg = traincnn.prepare_image_demo(temp)
        pshape = traincnn.get_shape_prediction(cnn, shimg)
        color_prel.my_pill_color_demo(temp)
        pcolor = train_color_fcnn.get_color_prediction(fcnn, temp)
        fc_afisare(temp, title=f"{pshape} {pcolor}")
        plt.show()
    return

if __name__ == '__main__':
    main()
