import cv2

img = cv2.imread("sample.jpg")

resized = cv2.resize(img, (224, 224))

print("Original Shape :", img.shape)
print("Resized Shape :", resized.shape)

cv2.imshow("Original", img)
cv2.imshow("Resized", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()