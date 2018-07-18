# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 23:33:26 2018

@author: Jiyoung Yun
"""

import cv2
import matplotlib.pyplot as plt
from PIL import ImageGrab
import numpy as np


def nothing(x):
    pass
cv2.namedWindow('image')
cv2.createTrackbar('th1', 'image', 0, 255, nothing)
cv2.createTrackbar('th2', 'image', 0, 255, nothing)

n = 0
while(1):
    
    th1 = cv2.getTrackbarPos('th1', 'image')
    th2 = cv2.getTrackbarPos('th2', 'image')
    
    screen = np.array(ImageGrab.grab(bbox = (100,100, 500, 500)))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
 
    edge = cv2.bilateralFilter(screen,9, 75, 75 )
    canny_bilateral = cv2.Canny(edge, th1, th2, 3 )
    canny_screen = cv2.Canny(screen, th1, th2, 3)
    cv2.imshow('screen', canny_screen)
    cv2.imshow('bilateral', canny_bilateral)
    
    if cv2.waitKey(25) & 0xFF == ord('s'):
        cv2.imwrite('screen%s.jpg'%n, canny_screen )
        cv2.imwrite('bilateral%s.jpg'%n, canny_bilateral)
        n+=1
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    