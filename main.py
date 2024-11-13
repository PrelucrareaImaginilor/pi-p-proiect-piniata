import numpy as np
import PIL as pil
import cv2 as cv
import matplotlib.pyplot as plt

import background_fct as bk
import text_fct as txf
from color_prel import my_pill_color
from text_fct import switch


def main():
    #deschidem imaginea
    temp = np.asarray(pil.Image.open(f'./test/testc (3).jpg'))
    color = temp.copy()
    #o facem grayscale
    temp = cv.cvtColor(temp, cv.COLOR_RGB2GRAY)
    img = temp.copy()

    mascaPastila=bk.masca_pastila(img)
    img2=bk.contur_pastila(img,mascaPastila)
    img3=bk.eliminare_fundal(img,mascaPastila)

    name=my_pill_color(color)

    plt.figure()
    plt.title(name)
    plt.imshow(color)
    #de aici practic doar adaugam niste range-uri pt fiecare culoare si practic stim ce culoari avem
    #-----in sus culoare




    plt.show()
    return


if __name__ == '__main__':
    main()