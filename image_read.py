import cv2

img = cv2.imread("sample.jpg")

if img is None:
    print("Image not found")
else:
    print("Image Loaded Successfully")
    print("Shape:", img.shape)