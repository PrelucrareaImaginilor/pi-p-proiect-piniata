<<<<<<< Updated upstream
from pickletools import uint8

=======
import numpy as np
>>>>>>> Stashed changes
import PIL as pil
import cv2 as cv
import matplotlib.pyplot as plt

import background_fct as bk
import text_fct as tf
def main():
    #deschidem imaginea
    temp = np.asarray(pil.Image.open(f'./test/img (11).jpg'))
    color = temp.copy()
    #o facem grayscale
    temp = cv.cvtColor(temp, cv.COLOR_RGB2GRAY)
    img = temp.copy()

    mascaPastila=bk.masca_pastila(img)
    img2=bk.contur_pastila(img,mascaPastila)
    img3=bk.eliminare_fundal(img,mascaPastila)

    plt.title("masca")
    plt.imshow(mascaPastila, cmap='gray')
    plt.figure()
    plt.title("THE contur")
    plt.imshow(img2, cmap='gray')
    plt.figure()
    plt.title("eliminat_fundal")
    plt.imshow(img3, cmap='gray')
    plt.figure()
    #----------de aici in jos pentru culoare-----------------
    color = cv.bitwise_and(color, color, mask = mascaPastila)
    plt.figure()
    plt.title("Colorata")
    plt.imshow(color)

<<<<<<< Updated upstream
    #adunarea
    thresh1=cv.bitwise_or(thresh2,thresh1)
    plt.title("combo thresh-uri")
    plt.imshow(thresh1, cmap='gray')
=======
    #regiuni de interes
    roi1 = [20, 20, 50, 40]
    roi2 = [70, 20, 100, 40]
    roi3 = [20, 60, 50, 80]
    roi4 = [70, 60, 100, 80]

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
    print(avg1)
    print(avg2)
    print(avg3)
    print(avg4)
    a = avg1.astype(tuple)
    b = avg2.astype(tuple)
    c = avg3.astype(tuple)
    d = avg4.astype(tuple)
    print(d)
    color = cv.rectangle(color, (roi1[0], roi1[1]), (roi1[2], roi1[3]), a, 4)
    color = cv.rectangle(color, (roi2[0], roi2[1]), (roi2[2], roi2[3]), b, 4)
    color = cv.rectangle(color, (roi3[0], roi3[1]), (roi3[2], roi3[3]), c, 4)
    color = cv.rectangle(color, (roi4[0], roi4[1]), (roi4[2], roi4[3]), d, 4)
>>>>>>> Stashed changes
    plt.figure()
    plt.title("Colorata cu roi")
    plt.imshow(color)
    #de aici practic doar adaugam niste range-uri pt fiecare culoare si practic stim ce culoari avem
    #-----in sus culoare

    color = cv.bitwise_and(color, color, mask = thresh1)
    plt.figure()
    plt.title("Colorata")
    plt.imshow(color)

<<<<<<< Updated upstream
    #regiuni de interes
    roi1 = [20, 20, 50, 40]
    roi2 = [70, 20, 100, 40]
    roi3 = [20, 60, 50, 80]
    roi4 = [70, 60, 100, 80]

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
    print(avg1)
    print(avg2)
    print(avg3)
    print(avg4)
    a = avg1.astype(tuple)
    b = avg2.astype(tuple)
    c = avg3.astype(tuple)
    d = avg4.astype(tuple)
    print(d)
    color = cv.rectangle(color, (roi1[0], roi1[1]), (roi1[2], roi1[3]), a, 4)
    color = cv.rectangle(color, (roi2[0], roi2[1]), (roi2[2], roi2[3]), b, 4)
    color = cv.rectangle(color, (roi3[0], roi3[1]), (roi3[2], roi3[3]), c, 4)
    color = cv.rectangle(color, (roi4[0], roi4[1]), (roi4[2], roi4[3]), d, 4)
    plt.figure()
    plt.title("Colorata cu roi")
    plt.imshow(color)
    #de aici practic doar adaugam niste range-uri pt fiecare culoare si practic stim ce culoari avem
=======
    #--------------testare pentru scris---------
    #img3 = bk.eliminare_fundal(img, mascaPastila)
    mascaPastila = bk.masca_pastila(img)
    img3=tf.ridicare_contrast(temp,mascaPastila)
    plt.title("ridicare contrast")
    plt.imshow(temp, cmap='gray')
    plt.figure()
    #si cu masca de fundal apoi negat
    #------------------------------------------
>>>>>>> Stashed changes
    plt.show()
    return


if __name__ == '__main__':
    main()