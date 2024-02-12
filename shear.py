import cv2
import numpy as np
img= cv2.imread('assignment1.jpg')
M= np.array([[1,0.2,0], [0,1,0]])
rows, cols, ch=img.shape
dst=cv2.warpAffine(img, M, (cols,rows))
cv2.imshow('dst',dst)
cv2.waitKey(0)