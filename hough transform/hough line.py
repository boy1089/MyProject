import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(gray, 100, 150, apertureSize = 3)

#lines = cv2.HoughLines(edges, 1, np.pi/180,50)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50)
    
for j in range(len(lines)):
    for rho, theta in lines[j]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
            
        
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)



plt.subplot(221)
plt.imshow(gray, cmap = 'Greys_r')
plt.subplot(222)
plt.imshow(edges)
plt.subplot(223)
plt.imshow(img)
plt.subplot(224)
plt.scatter([x[0][0] for x in lines],[ x[0][1] for x in lines])
