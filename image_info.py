import cv2

img = cv2.imread("sample.jpg")

print("Height :", img.shape[0])
print("Width  :", img.shape[1])
print("Channels :", img.shape[2])