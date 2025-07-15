# Python script for object detection using OpenCV
# Erkennt Objekte mit OpenCV
import cv2
import numpy as np
import os

def detect_object(image_path):
    """
    Detects object color (red or blue) in an image.
    Returns: 1 (Red), 2 (Blue), or 0 (Unknown).
    """
    if not os.path.exists(image_path):
        print(f"Image not found: {image_path}")
        return 0

    # Load image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to load image: {image_path}")
        return 0

    # Convert to HSV for color detection
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define color ranges
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    lower_blue = np.array([100, 120, 70])
    upper_blue = np.array([130, 255, 255])

    # Create masks
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Count non-zero pixels
    red_count = cv2.countNonZero(mask_red)
    blue_count = cv2.countNonZero(mask_blue)

    if red_count > blue_count and red_count > 100:
        return 1  # Red
    elif blue_count > red_count and blue_count > 100:
        return 2  # Blue
    else:
        return 0  # Unknown

if __name__ == "__main__":
    # Test with sample images
    for img in ["src/vision/sample_images/red_block.jpg", "src/vision/sample_images/blue_block.jpg"]:
        result = detect_object(img)
        color = {1: "Red", 2: "Blue", 0: "Unknown"}[result]
        print(f"Image: {img}, Detected: {color}")
