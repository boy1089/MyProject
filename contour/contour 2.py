# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 23:33:26 2018

@author: Jiyoung Yun
"""

import cv2
import matplotlib.pyplot as plt
from PIL import ImageGrab
import numpy as np


screen = cv2.imread('rec3.png')

#screen = abs(screen - 254)
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

#print(min(screen.flatten()), max(screen.flatten()))

#th1 = 50
#blockSize = 301
#C = 10
ret, canny = cv2.threshold(screen, 200 , 255,cv2.THRESH_BINARY_INV)

#canny = cv2.Canny(cv2.GaussianBlur(screen, (5, 5), 0), 50, 30, 3)
copy = canny.copy()
img, contours, hierarchy = cv2.findContours(copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
EXTERNAL = cv2.drawContours(img, contours, -1, (253, 125, 0), 5)

copy = canny.copy()
img, contours, hierarchy = cv2.findContours(copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
TREE = cv2.drawContours(img, contours, -1, (253, 125, 0), 5)

plt.figure()
plt.subplot(121)
plt.title('original')
plt.imshow(screen, cmap = 'Greys')
plt.colorbar()
plt.subplot(122)
plt.title('canny')
plt.imshow(canny, cmap = 'Greys')
plt.tight_layout()

plt.figure()
plt.subplot(121)
plt.title('EXTERNAL')
plt.imshow(EXTERNAL, cmap = 'Greys')
plt.subplot(122)
plt.title('tree')
plt.imshow(TREE, cmap = 'Greys')

plt.tight_layout()
#plt.savefig('test.png')
