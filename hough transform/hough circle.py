import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread('circles.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.GaussianBlur(gray, (5, 5), 0)

canny = cv2.Canny(gray, 30, 150)

#circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, 100, param1 = 200, param2 =30, minRadius = 30, maxRadius = 100)

circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, minDist = 0, param1 = 1, param2 =1)
circles = np.uint16(np.around(circles))

canny = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
for i in circles[0, :]:
    
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 1)
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 1)
    
    cv2.circle(canny, (i[0], i[1]), i[2], (0, 255, 0), 1)
    cv2.circle(canny, (i[0], i[1]), 2, (0, 0, 255), 1)
  


plt.figure()
plt.subplot(121)
plt.imshow(gray, cmap = 'Greys_r')
plt.subplot(122)
plt.imshow(canny)

plt.tight_layout()
