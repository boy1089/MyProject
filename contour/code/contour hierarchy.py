
import cv2
import matplotlib.pyplot as plt
import numpy as np

screen = np.zeros((512, 512), np.uint8)
screen = cv2.rectangle(screen, (100, 100), (200, 200), (255, 255, 255), -1)
screen = cv2.rectangle(screen, (130, 130), (170, 170), (0, 0, 0), -1)
screen = cv2.rectangle(screen, (10, 10), (50, 50), (255, 255, 255), -1)
screen = cv2.rectangle(screen, (110, 110), (120, 120), (0, 0, 0), -1)

screen_color = cv2.cvtColor(screen, cv2.COLOR_GRAY2BGR)

ret, thr = cv2.threshold(screen, 200 , 255,cv2.THRESH_BINARY)
copy = thr.copy()
img1, contours, hierarchy = cv2.findContours(copy, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
#EXTERNAL = cv2.drawContours(img1, contours, -1, (253, 125, 0), 2)

EXTERNAL = cv2.drawContours(screen_color, contours, 0, (253, 125, 0), 0)

EXTERNAL = cv2.resize(EXTERNAL, (1000, 1000), 2, 2, interpolation=cv2.INTER_AREA)

cv2.imshow('bgr', EXTERNAL)

print(hierarchy)

