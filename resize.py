import cv2
path='assignment1.jpg'
image=cv2.imread(path)
window_name='image'
width=500
height=500
image=cv2.resize(image,(int(width),int(height)))
cv2.imshow(window_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows()