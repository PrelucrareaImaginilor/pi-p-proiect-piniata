from pickletools import uint8

import PIL as pil
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image
from numpy.ma.core import bitwise_and

import background_fct as bk

def fc_afisare(img,title):
    plt.figure()
    plt.title(title)
    plt.imshow(img, cmap='gray')


def switch(avg):
    h,s,v=avg
    print(h,s,v)
    if(v==0 and s==0 and h==0) :
        return "BLACK"
    elif(s==0 and v>=70 or (s<=30 and v>80)):
        return "WHITE"
    elif(s==0 and v!=0):
        return "GRAY"
    if h<5 or h<14:
        return "RED"
    elif h<20:
        if v<=40:
            return "BROWN"
        else:
            return "ORANGE"
    elif h<40:
        if v<=40:
            return "BROWN"
        else:
            return "YELLOW"
    elif h<120:
        return "GREEN"
    elif h < 130:
        return "TURQUOISE"
    elif h<230:
        return "BLUE"
    elif h<250:
        return "VIOLET"
    elif h<330:
        return "PINK"
    else:
        return "RED"

def pill_color(color1,color2,color3,color4):
    if color1==color2==color3==color4:
        return color1
    elif color1==color3 and color2==color4:
        return color1+";"+color2
    elif color1==color3==color2 or color1==color3==color4:
        return color1
    elif color1==color4==color2 or color2==color3==color4:
        return color2
    elif color1==color3:
        return color1+";"+color2
    elif color2==color4:
        return color1+";"+color2
    else:
        return color1