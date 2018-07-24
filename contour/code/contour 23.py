
import cv2
import matplotlib.pyplot as plt
import numpy as np

screen = np.zeros((512, 512), np.uint8)
screen = cv2.rectangle(screen, (100, 100), (200, 200), (255, 255, 255), 0)
screen = cv2.rectangle(screen, (130, 130), (170, 170), (255, 255, 255), 0)


ret, thr = cv2.threshold(screen, 200 , 255,cv2.THRESH_BINARY)

copy = thr.copy()
img1, contours, hierarchy = cv2.findContours(copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
EXTERNAL = cv2.drawContours(img1, contours, -1, (253, 125, 0), 5)

copy = thr.copy()
img, contours, hierarchy = cv2.findContours(copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
screen = cv2.cvtColor(screen, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(screen, contours, -1, (253, 125, 0), 5)
#
#img = cv2.circle(img, (contours[0][0][0][0], contours[0][0][0][1]), 10, (255, 255), -1)
#img = cv2.circle(img, (contours[0][1][0][0], contours[0][1][0][1]), 10, (255, 255), -1)
#img = cv2.circle(img, (contours[0][2][0][0], contours[0][2][0][1]), 10, (255, 255), -1)
#img = cv2.circle(img, (contours[0][3][0][0], contours[0][3][0][1]), 10, (255, 255), -1)


plt.figure()
plt.subplot(121)
plt.title('original')
plt.imshow(screen, cmap = 'Greys')
plt.colorbar()
plt.subplot(122)
plt.title('threshold')
plt.imshow(thr, cmap = 'Greys')
plt.tight_layout()

plt.figure()
plt.subplot(121)
plt.title('EXTERNAL')
plt.imshow(img1, cmap = 'Greys')
plt.subplot(122)
plt.title('tree')
plt.imshow(img, cmap = 'Greys')
plt.scatter(contours)
plt.tight_layout()
#plt.savefig('test.png')
