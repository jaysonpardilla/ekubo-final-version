"""capture_image.py

Safely import OpenCV at runtime. In headless server environments the
full `opencv-python` wheel can fail due to missing system GL libs.
We prefer `opencv-python-headless` in `requirements.txt`. If `cv2` is
not available the function returns None and does not prevent Django
from starting.
"""

import os

def capture_image(filename='intruder.jpg'):
    try:
        import cv2
    except Exception:
        # OpenCV not available in this environment (headless/server)
        return None

    # Open the webcam
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()

    image_path = None
    if ret:
        # Save the captured image
        if not os.path.exists('captured_images'):
            os.makedirs('captured_images')
        image_path = os.path.join('captured_images', filename)
        cv2.imwrite(image_path, frame)

    cam.release()
    return image_path
