import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dog.jpg')
img = img[:, :, 0]
img = cv2.GaussianBlur(img, (5, 5), 0)


blockSize = 201
C = -100
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,blockSize,C)
#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#            cv2.THRESH_BINARY,blockSize,C)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,blockSize,C)

plt.subplot(211)
plt.imshow(th2, cmap = 'gray')
plt.subplot(212)
plt.imshow(th3, cmap = 'gray')

#plt.imshow(img, cmap = 'gray')
#plt.plot(th2[100])
