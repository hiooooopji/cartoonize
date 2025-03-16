import cv2
import numpy as np

def vectorize_edges(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Detect edges
    edges = cv2.Canny(image, 100, 200)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on a blank canvas
    canvas = np.ones_like(image) * 255
    cv2.drawContours(canvas, contours, -1, (0, 0, 0), 1)

    cv2.imshow("Vectorized Image", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return canvas

if __name__ == "__main__":
    vectorize_edges("images/input.jpg")
