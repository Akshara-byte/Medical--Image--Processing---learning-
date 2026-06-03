import cv2

# Read image
img = cv2.imread("sample.jpg", 0)

# Resize
img = cv2.resize(img, (224, 224))

# Noise removal
blur = cv2.GaussianBlur(img, (5,5), 0)

# CLAHE enhancement
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
enhanced = clahe.apply(blur)

# Edge detection
edges = cv2.Canny(enhanced, 100, 200)

# Save outputs
cv2.imwrite("lung_enhanced.jpg", enhanced)
cv2.imwrite("lung_edges.jpg", edges)

print("Pipeline completed successfully")