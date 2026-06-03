import cv2

img = cv2.imread("sample.jpg", 0)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

print("Histogram Generated")
print(hist[:10])