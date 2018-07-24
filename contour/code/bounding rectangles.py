
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('rec.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)
img, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
#EXTERNAL = cv2.drawContours(screen_color, contours, 0, (253, 125, 0), 0)
#EXTERNAL = cv2.resize(EXTERNAL, (1000, 1000), 2, 2, interpolation=cv2.INTER_AREA)


copy = img.copy()
copy = cv2.cvtColor(copy, cv2.COLOR_GRAY2BGR)
for j in range(len(contours)):
        
    
    idx = j

    x, y, w, h = cv2.boundingRect(contours[idx])
   
    copy = cv2.rectangle(copy, (x, y), (x+w, y+h), (0, 255, 0), 1)
EXTERNAL = cv2.resize(copy, (1000, 1000), 2, 2, interpolation=cv2.INTER_AREA)

cv2.imshow('bgr',  EXTERNAL)
