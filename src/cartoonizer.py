import cv2
import numpy as np

def cartoonize(image_path):
    # Load image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply median blur to remove noise
    gray_blur = cv2.medianBlur(gray, 7)

    # Use adaptive threshold to create a sketch-like outline
    edges = cv2.adaptiveThreshold(
        gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
    )

    # Use bilateral filter to smooth colors while preserving edges
    color = cv2.bilateralFilter(image, 10, 250, 250)

    # Convert back to grayscale and blend with edges
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

if __name__ == "__main__":
    cartoon = cartoonize("images/input.jpg")
    cv2.imshow("Hand-Drawn Cartoon", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
