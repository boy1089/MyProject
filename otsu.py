import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dog.jpg')
img1 = img[:, :, 0]
img = cv2.copyMakeBorder(img1, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
#img = cv2.GaussianBlur(img, (5, 5), 0)
blockSize = 201

C = 1
img_ret = img.copy()
img_th = img.copy()
for ix, iy in np.ndindex(img.shape):
    img_seg = img[ix - int(blockSize/2):ix+int(blockSize/2), iy - int(blockSize/2):iy+int(blockSize/2)]
    ret, th = cv2.threshold(img_seg, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    img_ret[ix, iy] = ret
    if img_th[ix, iy] >= ret:
        img_th[ix, iy] = 1
    else : 
        img_th[ix, iy] = 0

imgList = [img_ret, img_th, img1, img]
imgTitle = ['threshold', 'result', 'original', 'padding']
for j in range(4):
    plt.subplot('22%s'%j)
    plt.imshow(imgList[j], cmap = 'gray')
    plt.title(imgTitle[j])
