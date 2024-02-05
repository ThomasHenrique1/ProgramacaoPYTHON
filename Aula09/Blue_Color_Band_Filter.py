import cv2
import numpy as np
frame = cv2.imread("bolas_cores.jpg")
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# Temos que pegar uma cor específica (AZUL)
lower_blue = np.array([110, 127, 127])
upper_blue = np.array([130, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
res = cv2.bitwise_and(frame, frame, mask=mask) 
cv2.imshow("Original", frame)
cv2.imshow("Mascara", mask)
cv2.imshow("final", res)
cv2.waitKey(0)