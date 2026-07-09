import argparse
import cv2

from g1d_chess.vision.board_detector import BoardDetector


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--out", default="board_detect_debug.jpg")
    args = parser.parse_args()

    image = cv2.imread(args.image)
    if image is None:
        raise FileNotFoundError(args.image)

    detector = BoardDetector()
    debug = detector.debug_draw(image)

    cv2.imwrite(args.out, debug)
    print(f"Saved {args.out}")


if __name__ == "__main__":
    main()
