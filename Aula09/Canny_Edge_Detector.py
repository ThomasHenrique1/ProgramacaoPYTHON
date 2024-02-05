import cv2
import numpy as np
img = cv2.imread("bola_pink_blue.jpg")

canny = cv2.Canny(img, 10,400)#processamento
#canny3c=cv2.merge((canny,canny,canny))

imgs_concat = np.concatenate((img, canny), axis=0)

cv2.imshow("Original", img)
cv2.imshow("Bordas", canny)
#cv2.imwrite("canny.png", canny)
cv2.waitKey(0)

