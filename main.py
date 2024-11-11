import PIL as pil
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def main():
    #deschidem imaginea
    temp = np.asarray(pil.Image.open(f'./test/img (18).jpg'))
    #o facem grayscale
    temp = cv.cvtColor(temp, cv.COLOR_RGB2GRAY)
    img = temp.copy()

    #fereastra cu imaginea originala
    # plt.title("Imagine Originala")
    # plt.imshow(temp, cmap='gray')
    # plt.figure()

    #aplicare filtru median
    median = cv.medianBlur(img,5)
    # plt.title("blurare")
    # plt.imshow(median, cmap='gray')
    # plt.figure()

    #histograma imaginii
    # plt.title("HISTOGRAMA")
    # plt.hist(img.ravel(), bins=256)
    # plt.figure()

    #threshold pe imaginea originala cu prag 156
    ret, thresh1 = cv.threshold(median, 156, 255, cv.THRESH_BINARY)
    #blur la threshold
    thresh3 = cv.medianBlur(thresh1, 11)
    plt.title("t3")
    plt.imshow(thresh3, cmap='gray')
    plt.figure()
    #adunarea celor doua masti
    thresh1 = cv.bitwise_or(thresh1, thresh3)
    plt.title("THRESHOLD1")
    plt.imshow(thresh1, cmap='gray')
    plt.figure()


    #threshhold la imaginea initiala cu prag de 110
    ret, thresh2 = cv.threshold(median, 110, 255, cv.THRESH_BINARY_INV)
    plt.title("THRESHOLD2")
    plt.imshow(thresh2, cmap='gray')
    plt.figure()
    #blur la thresh2
    thresh4 = blur = cv.medianBlur(thresh2, 9)
    thresh2 = cv.bitwise_or(thresh2, thresh4)
    plt.title("t4")
    plt.imshow(thresh4, cmap='gray')
    plt.figure()

    #adunarea
    thresh1=cv.bitwise_or(thresh2,thresh1)
    plt.title("combo thres-uri")
    plt.imshow(thresh1, cmap='gray')
    plt.figure()
    thresh1=cv.bitwise_or(thresh3,thresh1)
    img=cv.bitwise_and(img, thresh1)


    img= cv.Canny(thresh1,110,200)

    plt.title("THE FINAL")
    plt.imshow(img, cmap='gray')


    plt.show()
    return
#blurez -> binarizare-treshold Xn,cu n oarecare ales ->

if __name__ == '__main__':
    main()