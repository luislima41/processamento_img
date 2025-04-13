import cv2
import numpy as np

img = cv2.imread("original.jpg", 0)
_, img_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5,5), np.uint8)
closing = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("filtrada.jpg", closing)
