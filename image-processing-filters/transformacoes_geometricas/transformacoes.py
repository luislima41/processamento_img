import cv2

img = cv2.imread("original.jpg")
resized = cv2.resize(img, (300, 300))
(h, w) = resized.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(resized, matrix, (w, h))
cv2.imwrite("transformada.jpg", rotated)
