import cv2
import numpy as np


class BoardROIDetector:
    def __init__(self, x_min=0.12, x_max=0.78, y_min=0.61, y_max=0.95):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def detect_board_corners(self, image_bgr):
        # Fixed corners from your current camera image.
        return np.array([
            [430, 640],    # top left
            [1365, 640],   # top right
            [1535, 985],   # bottom right
            [250, 985],    # bottom left
        ], dtype=np.float32)

    def square_centers_image(self, image_bgr):
        tl, tr, br, bl = self.detect_board_corners(image_bgr)
        centers = {}

        for r in range(8):
            for f in range(8):
                u = (f + 0.5) / 8.0
                v = (r + 0.5) / 8.0

                top = tl * (1 - u) + tr * u
                bottom = bl * (1 - u) + br * u
                p = top * (1 - v) + bottom * v

                square = f"{chr(ord('a') + f)}{8 - r}"
                centers[square] = p.tolist()

        return centers

    def debug_draw(self, image_bgr):
        image = image_bgr.copy()
        corners = self.detect_board_corners(image_bgr)
        centers = self.square_centers_image(image_bgr)

        cv2.polylines(image, [corners.astype(int)], True, (0, 255, 255), 4)

        for square, point in centers.items():
            x, y = map(int, point)
            cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
            cv2.putText(image, square, (x + 4, y - 4),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 0), 1)

        return image
