import cv2
img = cv2.imread("face_a.jpg")
crop = img[170:100+87, 75:100+27]
cv2.imshow("Original", img)
cv2.imshow("Crop", crop)
cv2.waitKey(0)
