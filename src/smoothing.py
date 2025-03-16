import cv2

def apply_smoothing(image_path):
    image = cv2.imread(image_path)
    
    # Apply bilateral filter
    smooth = cv2.bilateralFilter(image, 9, 75, 75)

    cv2.imshow("Smoothed Image", smooth)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return smooth

if __name__ == "__main__":
    apply_smoothing("images/input.jpg")
