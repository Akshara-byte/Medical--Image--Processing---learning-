import cv2

img = cv2.imread("sample.jpg")

cv2.imshow("Medical Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()