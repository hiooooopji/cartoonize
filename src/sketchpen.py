import cv2
import numpy as np

def sketchpen_effect(image_path):
    # Load image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges using adaptive threshold
    edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Convert edges to 3-channel format for display
    sketch = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return sketch

if __name__ == "__main__":
    sketch = sketchpen_effect("images/input.jpg")
    cv2.imshow("Sketchpen Effect", sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
