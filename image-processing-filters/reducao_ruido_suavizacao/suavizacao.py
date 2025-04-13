import cv2

img = cv2.imread("original.jpg")
suavizada = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imwrite("filtrada.jpg", suavizada)
