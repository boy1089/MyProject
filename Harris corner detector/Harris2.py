
import cv2
import matplotlib.pyplot as plt
from PIL import ImageGrab
import numpy as np
def nothing(x):
    pass
cv2.namedWindow('image')
cv2.createTrackbar('th1', 'image', 2, 255, nothing)
cv2.createTrackbar('th2', 'image', 1, 100, nothing)

n = 0
while(1):
    

    th1 = cv2.getTrackbarPos('th1', 'image')
    th2 = cv2.getTrackbarPos('th2', 'image') / 100.
    
    screen = np.array(ImageGrab.grab(bbox = (100,100, 500, 500)))
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    screen_copy = screen.copy()
    dst = cv2.cornerHarris(gray, th1, 3, th2)
    screen_copy[dst>0.01*dst.max()] = [0, 0, 255]
    cv2.imshow('screen', screen_copy)
#    cv2.imshow('bilateral', canny_bilateral)
    