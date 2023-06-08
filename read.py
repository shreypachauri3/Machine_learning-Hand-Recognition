import cv2 as cv
import numpy as np

blank =np.zeros((500,500,3),dtype='uint8')


#converting into grayscale image


img =  cv.imread('photo.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=2)
cv.imshow('blank',gray)
cv.waitKey(0)
