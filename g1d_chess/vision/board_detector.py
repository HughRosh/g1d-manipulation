import cv2
import numpy as np


class BoardDetector:
    """
    Chessboard-specific detector.

    Uses OpenCV's chessboard corner detector first.
    For an empty board, it detects the internal 7x7 grid corners,
    then expands them to estimate the full board outline and all 64 centers.
    """

    def detect_board_corners(self, image_bgr):
        gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

        pattern_size = (7, 7)
        ok, corners = cv2.findChessboardCornersSB(gray, pattern_size)

        if not ok:
            raise RuntimeError(
                "Could not detect chessboard grid. Try a clearer image, less glare, or crop closer to the board."
            )

        pts = corners.reshape(-1, 2)

        grid = pts.reshape(7, 7, 2)

        # Internal chessboard corners
        inner_tl = grid[0, 0]
        inner_tr = grid[0, 6]
        inner_br = grid[6, 6]
        inner_bl = grid[6, 0]

        # Each internal corner is one square in from the outer board edge.
        # Expand outward by one square width.
        right_vec = (inner_tr - inner_tl) / 6.0
        down_vec = (inner_bl - inner_tl) / 6.0

        outer_tl = inner_tl - right_vec - down_vec
        outer_tr = inner_tr + right_vec - down_vec
        outer_br = inner_br + right_vec + down_vec
        outer_bl = inner_bl - right_vec + down_vec

        return np.array([outer_tl, outer_tr, outer_br, outer_bl], dtype=np.float32)

    def square_centers_image(self, image_bgr):
        corners = self.detect_board_corners(image_bgr)
        tl, tr, br, bl = corners

        centers = {}

        for rank_from_top in range(8):
            for file_idx in range(8):
                u = (file_idx + 0.5) / 8.0
                v = (rank_from_top + 0.5) / 8.0

                top = tl * (1.0 - u) + tr * u
                bottom = bl * (1.0 - u) + br * u
                point = top * (1.0 - v) + bottom * v

                square = f"{chr(ord('a') + file_idx)}{8 - rank_from_top}"
                centers[square] = point.tolist()

        return centers

    def debug_draw(self, image_bgr):
        image = image_bgr.copy()
        corners = self.detect_board_corners(image)
        centers = self.square_centers_image(image)

        poly = corners.astype(int)
        cv2.polylines(image, [poly], True, (0, 255, 255), 3)

        for square, point in centers.items():
            x, y = map(int, point)
            cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
            cv2.putText(
                image,
                square,
                (x + 4, y - 4),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.35,
                (0, 255, 0),
                1,
            )

        return image
