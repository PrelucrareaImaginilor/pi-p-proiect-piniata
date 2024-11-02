import PIL as pil
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

sabelV = np.asarray([
                    [1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]
                ])
sabelH = np.asarray([
                    [1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]
                ])

def main():
    #deschidem imaginea
    temp = np.asarray(pil.Image.open(f'./test/img (1).jpg'))
    #o facem grayscale
    temp = cv.cvtColor(temp, cv.COLOR_RGB2GRAY)

    #fereastra cu imaginea originala
    plt.title("Imagine Originala")
    plt.imshow(temp, cmap='gray')
    plt.figure()

    #histograma imaginii
    plt.title("HISTOGRAMA")
    plt.hist(temp.ravel(), bins=256)
    plt.figure()

    #fereastra cu imaginea dupa ce am egalizat histograma
    temp = cv.equalizeHist(temp)
    plt.title("Imagine Cu Histograma Egalizata")
    plt.imshow(temp, cmap='gray')
    plt.figure()

    #binarizarea imaginii (putem incerca aici sa izolam pastila de fundal)
    ret, mask = cv.threshold(temp, 14, 255, cv.THRESH_BINARY_INV)
    ret, mask2 = cv.threshold(temp, 126, 255, cv.THRESH_BINARY)
    mask3 = cv.bitwise_or(mask, mask2) #masca 1 si 2 "adunate"

    plt.title("MASCA 1")
    plt.imshow(mask, cmap='gray')
    plt.figure()

    plt.title("MASCA 2")
    plt.imshow(mask2, cmap='gray')
    plt.figure()

    plt.title("MASCA 3")
    plt.imshow(mask3, cmap='gray')
    plt.show()
    return

if __name__ == '__main__':
    main()