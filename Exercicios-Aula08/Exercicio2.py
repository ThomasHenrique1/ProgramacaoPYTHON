import cv2
import numpy as np
img = cv2.imread('R.bmp')
median = cv2.medianBlur(img, 5)
compare = np.concatenate((img, median), axis=1)
cv2.imshow("entrada", img)
cv2.imshow("Final ",median)
cv2.waitKey(0)