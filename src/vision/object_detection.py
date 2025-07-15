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

    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to load image: {image_path}")
        return 0

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 100, 50])
    upper_red = np.array([15, 255, 255])
    lower_red2 = np.array([165, 100, 50])
    upper_red2 = np.array([180, 255, 255])
    lower_blue = np.array([90, 100, 50])
    upper_blue = np.array([140, 255, 255])

    mask_red = cv2.inRange(hsv, lower_red, upper_red) + cv2.inRange(hsv, lower_red2, upper_red2)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    red_count = cv2.countNonZero(mask_red)
    blue_count = cv2.countNonZero(mask_blue)
    print(f"Red count: {red_count}, Blue count: {blue_count}")  # Debug

    if red_count > blue_count and red_count > 50:
        return 1  # Red
    elif blue_count > red_count and blue_count > 50:
        return 2  # Blue
    else:
        return 0  # Unknown

if __name__ == "__main__":
    for img in ["src/vision/sample_images/red_block.jpg", "src/vision/sample_images/blue_block.jpg"]:
        result = detect_object(img)
        color = {1: "Red", 2: "Blue", 0: "Unknown"}[result]
        print(f"Image: {img}, Detected: {color}")
