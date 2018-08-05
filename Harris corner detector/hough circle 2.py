import cv2
import numpy as np
import matplotlib.pyplot as plt


img = np.zeros((500, 500, 3), np.uint8)
img = cv2.circle(img, (100, 100), 100, (255, 255, 255), 2)
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thr = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)


#plt.imshow(gray)
#canny = cv2.Canny(gray, 50, 30)

#gray = cv2.GaussianBlur(gray, (5, 5), 0)

#canny = cv2.Canny(gray, 30, 150)

#circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, 100, param1 = 200, param2 =30, minRadius = 30, maxRadius = 100)

circles = cv2.HoughCircles(thr, cv2.HOUGH_GRADIENT, 0.1, 100, param1 = 100, param2 =30)

#circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 5,, 150,  minDist = 0, param1 = 1, param2 =1)
circles = np.uint16(np.around(circles))


for i in circles[0, :]:
    
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 3)
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    

#plt.imshow(thr)
plt.figure()
plt.imshow(img, cmap = 'Greys_r')

plt.tight_layout()
