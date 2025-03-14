#from pickletools import uint8

import PIL as pil
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def masca_pastila(img):
    median = cv.medianBlur(img, 5)

    # threshold pe imaginea originala cu prag 156
    ret, thresh1 = cv.threshold(median, 156, 255, cv.THRESH_BINARY)

    # blur la threshold
    thresh3 = cv.medianBlur(thresh1, 11)
    # adunarea celor doua masti
    thresh1 = cv.bitwise_or(thresh1, thresh3)
    # threshhold la imaginea initiala cu prag de 110
    ret, thresh2 = cv.threshold(median, 110, 255, cv.THRESH_BINARY_INV)
    # blur la thresh2
    thresh4 = blur = cv.medianBlur(thresh2, 9)
    thresh2 = cv.bitwise_or(thresh2, thresh4)

    # adunarea
    thresh1 = cv.bitwise_or(thresh2, thresh1)
    thresh1 = cv.bitwise_or(thresh3, thresh1)
    return thresh1

def eliminare_fundal(img,masca):
    img = cv.bitwise_and(img, masca)
    return img


def contur_pastila(img,masca):
    img = cv.Canny(masca, 110, 200)
    return img