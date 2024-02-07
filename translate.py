import cv2
import numpy as np

img = cv2.imread('Keralalalalala.png')
rows, cols =img.shape[:2]

matrix_trans= np.float32([[1,0,-100], [0,1,-30]])

translated_img = cv2.warpAffine(img, matrix_trans, (cols, rows))
hori = np.concatenate((img, translated_img), axis=1)

cv2.imshow("translate",hori)
cv2.waitKey(0)
cv2.destroyAllWindows()