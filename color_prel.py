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

def pill_color(color1,color2,color3,color4):
    if color1==color2==color3==color4:
        return color1
    elif color1==color3 and color2==color4:
        return color1+", "+color2
    elif color1==color3==color2 or color1==color3==color4:
        return color1
    elif color1==color4==color2 or color2==color3==color4:
        return color2
    elif color1==color3:
        return color1+", "+color2
    elif color2==color4:
        return color1+", "+color2
    else:
        return color1

def my_pill_color(color):
    #transf imaginii in imagine hsv
    color = cv.cvtColor(color, cv.COLOR_RGB2HSV_FULL)

    color = cv.medianBlur(color, 3)
    color = cv.convertScaleAbs(color, color, 1.1, -20)


    #regiuni de interes
    roi1 = [30, 20, 45, 35]
    roi2 = [80, 20, 95, 35]
    roi3 = [30, 50, 45, 65]
    roi4 = [80, 50, 95, 65]

    #sectiuni de imagine care reprezinta zonele de interes
    section1 = color[roi1[1]:roi1[3], roi1[0]:roi1[2]]
    section2 = color[roi2[1]:roi2[3], roi2[0]:roi2[2]]
    section3 = color[roi3[1]:roi3[3], roi3[0]:roi3[2]]
    section4 = color[roi4[1]:roi4[3], roi4[0]:roi4[2]]

    # gasim culoarea medie din fiecare zona
    avg1_row = np.average(section1, axis = 0)
    avg1 = np.round(np.average(avg1_row, axis = 0))
    avg2_row = np.average(section2, axis = 0)
    avg2 = np.round(np.average(avg2_row, axis = 0))
    avg3_row = np.average(section3, axis = 0)
    avg3 = np.round(np.average(avg3_row, axis = 0))
    avg4_row = np.average(section4, axis = 0)
    avg4 = np.round(np.average(avg4_row, axis = 0))


    #doar pt vizualizare
    # print(avg1)
    # print(avg2)
    # print(avg3)
    # print(avg4)
    #pentru a gasi culoare exacta pentru fiecare zona -> blue/white/etc.
    color1=switch(avg1)
    color2=switch(avg2)
    color3=switch(avg3)
    color4=switch(avg4)
    # print(color1)
    # print(color2)
    # print(color3)
    # print(color4)

    # a = avg1.astype(tuple)
    # b = avg2.astype(tuple)
    # c = avg3.astype(tuple)
    # d = avg4.astype(tuple)
    # print(d)
    # color = cv.rectangle(color, (roi1[0], roi1[1]), (roi1[2], roi1[3]), a, 4)
    # color = cv.rectangle(color, (roi2[0], roi2[1]), (roi2[2], roi2[3]), b, 4)
    # color = cv.rectangle(color, (roi3[0], roi3[1]), (roi3[2], roi3[3]), c, 4)
    # color = cv.rectangle(color, (roi4[0], roi4[1]), (roi4[2], roi4[3]), d, 4)

    my_pill_colors=pill_color(color1, color2, color3, color4)
    return my_pill_colors