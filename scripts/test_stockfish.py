import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import chess
from chess_engine import choose_move
from utils import load_config

def main():
    config = load_config("configs/chess.yaml")
    engine_cfg = config.get("engine", {})

    board = chess.Board()

    move = choose_move(
        board,
        stockfish_path=engine_cfg.get("stockfish_path"),
        time_limit=engine_cfg.get("time_limit_s", 0.1),
    )

    print("Test Stockfish / fallback move")
    print(f"Move: {move.uci()}")

if __name__ == "__main__":
    main()
