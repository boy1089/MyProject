# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 23:33:26 2018

@author: Jiyoung Yun
"""

import cv2
import matplotlib.pyplot as plt
read = cv2.VideoCapture(0)
read.set(3,320)
read.set(4,240)

while(1):
    _, frame = read.read()
    cv2.imshow('frame', frame)
    th2 = cv2.adaptiveThreshold(frame[:,:,0], 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 501, -10)
    cv2.imshow('th2', th2)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()