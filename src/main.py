import cv2

# Load image
image_path = "images/input.jpg"
image = cv2.imread(image_path)

# Show image
cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
