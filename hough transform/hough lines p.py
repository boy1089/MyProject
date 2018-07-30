import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(gray, 100, 150, apertureSize = 3)

#lines = cv2.HoughLines(edges, 1, np.pi/180,50)
minLineLength = 100
maxLineGap = 1
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 20, minLineLength, maxLineGap)

for j in range(len(lines)):
    for x1, y1, x2, y2 in lines[j]:
        a = np.cos(theta)
      
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)


plt.figure()
plt.subplot(221)
plt.imshow(gray, cmap = 'Greys_r')
plt.subplot(222)
plt.imshow(edges)
plt.subplot(223)
plt.imshow(img)
plt.subplot(224)
plt.scatter([x[0][0] for x in lines],[ x[0][1] for x in lines])
