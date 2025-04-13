import cv2

img = cv2.imread("original.jpg", 0)
bordas = cv2.Canny(img, 100, 200)
cv2.imwrite("filtrada.jpg", bordas)
