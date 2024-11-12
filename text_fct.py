from pickletools import uint8

import PIL as pil
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def ridicare_contrast(img,masca):
    plt.title("pas0")
    plt.imshow(img, cmap='gray')
    plt.figure()
    cv.convertScaleAbs(img, img, 1.05,-50)
    plt.title("pas1 -> dupa contrast")
    plt.imshow(img, cmap='gray')
    plt.figure()
    ret, img = cv.threshold(img, 80, 220, cv.THRESH_BINARY_INV)
    plt.title("pas1->dupa thresh")
    plt.imshow(img, cmap='gray')
    plt.figure()
    masca=cv.bitwise_not(masca)
    img=cv.bitwise_or(img,img,mask=masca)
    plt.title("mm")
    plt.imshow(masca, cmap='gray')
    plt.figure()
    return img