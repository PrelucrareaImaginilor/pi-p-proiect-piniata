import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import background_fct as bg
import PIL as pil

directory = '..\\ds\\'
df = pd.read_csv(directory + 'shapes1.csv')
file_paths = df['file_name'].values #din excel luam nume imagine
labels = df['label'].values #si ce forma are

top = int((120-96)/2)
fv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 5 6 7 8 13 14
for i in range(len(file_paths)):
    img = np.asarray(pil.Image.open(directory + file_paths[i]))
    #img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    tmp = cv.copyMakeBorder(img, top, top, 0, 0, cv.BORDER_REPLICATE)#marim imaginea sa fie 120 pe 120
    # classes = [
    #     "CAPSULE",  # 0
    #     "OVAL",  # 1
    #     "TEAR",  # 2
    #     "ROUND",  # 3
    #     "HEXAGON",  # 4
    #     "SQUARE",  # 5
    #     "TRIANGLE",  # 6
    #     "PENTAGON",  # 7
    #     "DIAMOND",  # 8
    #     "RECTANGLE",  # 9
    #     "SEMI-CIRCLE",  # 10
    #     "DOUBLE CIRCLE",  # 11
    #     "TRAPEZOID",  # 12
    #     "FREEFORM",  # 13
    #     "OCTAGON",  # 14
    #     "BULLET"  # 15
    # ]
    if labels[i] in [3, 4, 5, 6, 7, 8, 13, 14]: # formele care au orientarea diferita
        tmp=cv.rotate(tmp, cv.ROTATE_90_CLOCKWISE)
    cv.imwrite(directory + file_paths[i], tmp)
    print(file_paths[i], "done")
            # plt.figure(figsize=[2,2])
            # plt.xlabel(f'{file_paths[i]}')
            # plt.title(f'{labels[i]}')
            # plt.imshow(tmp[0:60, 0:120], cmap='gray')

plt.show()

