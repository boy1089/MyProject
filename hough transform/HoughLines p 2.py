import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread('sudoku.png')
img = img[:350, :350]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.GaussianBlur(gray, (5, 5), 0)

canny = cv2.Canny(gray, 30, 200)


lines = cv2.HoughLinesP(canny, 0.1, np.pi/720, 10, minLineLength = 20)

for j in range(len(lines)):
        
    for x1,y1,x2,y2 in lines[j]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


#plt.figure()
#plt.subplot(121)
#plt.imshow(img, cmap = 'Greys_r')
#plt.subplot(122)
plt.imshow(canny)

plt.tight_layout()
