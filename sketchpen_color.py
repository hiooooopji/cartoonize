import cv2
import numpy as np

# Define the 24 sketchpen colors (in BGR format)
PALETTE_24 = np.array([
    [0, 0, 0], [255, 255, 255], [255, 0, 0], [0, 255, 0], [0, 0, 255],  # Black, White, Red, Green, Blue
    [255, 255, 0], [255, 165, 0], [255, 20, 147], [128, 0, 128], [0, 255, 255],  # Yellow, Orange, Pink, Purple, Cyan
    [165, 42, 42], [210, 180, 140], [173, 216, 230], [0, 128, 128], [0, 100, 0],  # Brown, Tan, Light Blue, Teal, Dark Green
    [192, 192, 192], [128, 128, 128], [250, 128, 114], [139, 69, 19], [75, 0, 130],  # Silver, Grey, Salmon, Saddle Brown, Indigo
    [46, 139, 87], [255, 192, 203], [240, 230, 140]  # Sea Green, Light Pink, Khaki
], dtype=np.uint8)

def quantize_color(image):
    """Reduce colors in the image to the 24-color sketchpen palette"""
    reshaped = image.reshape((-1, 3))  # Flatten image
    distances = np.linalg.norm(reshaped[:, None] - PALETTE_24[None, :], axis=2)  # Compute distance to all palette colors
    nearest_color = PALETTE_24[np.argmin(distances, axis=1)]  # Find the closest color for each pixel
    return nearest_color.reshape(image.shape)  # Reshape back to original image shape

def sketchpen_color_effect(image_path):
    """Apply sketchpen effect with only 24 colors"""
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur for smoothing
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges using adaptive threshold
    edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Convert edges to 3-channel
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Reduce colors in the original image
    quantized_color = quantize_color(image)

    # Blend quantized colors with the sketch effect
    sketch_colored = cv2.bitwise_and(quantized_color, edges_colored)

    return sketch_colored

if __name__ == "__main__":
    sketch = sketchpen_color_effect("images/input.jpg")
    cv2.imshow("Sketchpen 24-Color Effect", sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
