
import cv2
import matplotlib.pyplot as plt
import numpy as np

screen = np.zeros((512, 512), np.uint8)
screen = cv2.rectangle(screen, (100, 100), (200, 200), (255, 255, 255), 0)
screen = cv2.rectangle(screen, (130, 130), (170, 170), (255, 255, 255), 0)
screen_color = cv2.cvtColor(screen, cv2.COLOR_GRAY2BGR)

ret, thr = cv2.threshold(screen, 200 , 255,cv2.THRESH_BINARY)
copy = thr.copy()
img1, contours, hierarchy = cv2.findContours(copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
EXTERNAL = cv2.drawContours(img1, contours, -1, (253, 125, 0), 5)

EXTERNAL2 = cv2.drawContours(screen_color, contours, -1, (253, 125, 0), 5)

cv2.imshow('binary', EXTERNAL)
cv2.imshow('bgr', EXTERNAL2)
