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
    color = cv.medianBlur(color, 3)
    color = cv.convertScaleAbs(color, color, 1.1, -20)

    #regiuni de interes
    roi1 = [30, 70, 45, 85]
    roi2 = [80, 70, 95, 85]


    #sectiuni de imagine care reprezinta zonele de interes
    section1 = color[roi1[1]:roi1[3], roi1[0]:roi1[2]]
    section2 = color[roi2[1]:roi2[3], roi2[0]:roi2[2]]

    avg1_row = np.average(section1, axis = 0)
    avg1 = np.round(np.average(avg1_row, axis = 0))
    avg2_row = np.average(section2, axis = 0)
    avg2 = np.round(np.average(avg2_row, axis = 0))
    return avg1,avg2

def my_pill_color_demo(color):
    color = cv.medianBlur(color, 3)
    color = cv.convertScaleAbs(color, color, 1.1, -20)
    # regiuni de interes
    roi1 = [30, 70, 45, 85]
    roi1_c = [28, 68, 47, 87]
    roi2 = [80, 70, 95, 85]
    roi2_c = [78, 68, 97, 87]
    # sectiuni de imagine care reprezinta zonele de interes
    section1 = color[roi1[1]:roi1[3], roi1[0]:roi1[2]]
    section2 = color[roi2[1]:roi2[3], roi2[0]:roi2[2]]
    avg1_row = np.average(section1, axis=0)
    avg1 = np.round(np.average(avg1_row, axis=0))
    avg2_row = np.average(section2, axis=0)
    avg2 = np.round(np.average(avg2_row, axis=0))

    a = avg1.astype(tuple)
    b = avg2.astype(tuple)
    color = cv.rectangle(color, (roi1_c[0], roi1_c[1]), (roi1_c[2], roi1_c[3]), (255, 255, 255), 4)
    color = cv.rectangle(color, (roi2_c[0], roi2_c[1]), (roi2_c[2], roi2_c[3]), (255, 255, 255), 4)
    color = cv.rectangle(color, (roi1[0], roi1[1]), (roi1[2], roi1[3]), a, 4)
    color = cv.rectangle(color, (roi2[0], roi2[1]), (roi2[2], roi2[3]), b, 4)
    plt.figure()
    plt.title("COLOR AREAS")
    plt.imshow(color)
    return