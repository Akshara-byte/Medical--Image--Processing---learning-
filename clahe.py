import cv2

img = cv2.imread("sample.jpg", 0)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

enhanced = clahe.apply(img)

cv2.imshow("Original", img)
cv2.imshow("CLAHE Enhanced", enhanced)

cv2.waitKey(0)
cv2.destroyAllWindows()