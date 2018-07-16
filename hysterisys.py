import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dog.jpg')
img = img[:, :, 0]



blockSize = 51
C = 10

th3 = cv2.adaptiveThreshold(img,1,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,blockSize,C)


plt.subplot(211)
plt.imshow(img, cmap = 'gray')
plt.subplot(212)
plt.imshow(th3, cmap = 'gray')
