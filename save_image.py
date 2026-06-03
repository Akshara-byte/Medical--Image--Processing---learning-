import cv2

img = cv2.imread("sample.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("lung_gray.jpg", gray)

print("Grayscale image saved successfully")