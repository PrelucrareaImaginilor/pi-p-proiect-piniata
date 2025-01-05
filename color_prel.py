import numpy as np
import PIL as pil
import cv2 as cv
import matplotlib.pyplot as plt



def switch(avg):
    h,s,v=avg
    #print(h,s,v)
    if(v==0 and s==0 and h==0) :
        return "BLACK"
    elif(s==0 and v>=70 or (s<=30 and v>80)):
        return "WHITE"
    elif(s==0 and v!=0):
        return "GRAY"
    if h<5 or h<14:
        if v<=40:
            return "BROWN"
        else:
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



def my_pill_color(color):
    #transf imaginii in imagine hsv
    color = cv.cvtColor(color, cv.COLOR_RGB2HSV_FULL)
    color = cv.medianBlur(color, 3)
    color = cv.convertScaleAbs(color, color, 1.1, -20)

    #regiuni de interes
    roi1 = [30, 20, 45, 35]
    roi2 = [80, 20, 95, 35]


    #sectiuni de imagine care reprezinta zonele de interes
    section1 = color[roi1[1]:roi1[3], roi1[0]:roi1[2]]
    section2 = color[roi2[1]:roi2[3], roi2[0]:roi2[2]]

    avg1_row = np.average(section1, axis = 0)
    avg1 = np.round(np.average(avg1_row, axis = 0))
    avg2_row = np.average(section2, axis = 0)
    avg2 = np.round(np.average(avg2_row, axis = 0))




    return avg1,avg2