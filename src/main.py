from board_detector import detect_board_state
from chess_engine import choose_move
from board_geometry import move_to_pick_place
from arm_planner import make_pick_place_motion
from robot_controller import execute_motion
from safety_checker import run_safety_checks
from utils import load_config

def main():
    chess_config = load_config("configs/chess.yaml")
    robot_config = load_config("configs/robot.yaml")

    board = detect_board_state()

    engine_cfg = chess_config.get("engine", {})
    move = choose_move(
        board,
        stockfish_path=engine_cfg.get("stockfish_path"),
        time_limit=engine_cfg.get("time_limit_s", 0.1),
    )

    board.push(move)

    plan = move_to_pick_place(move.uci(), chess_config)
    motion = make_pick_place_motion(plan, chess_config)

    print("G1-D Chess")
    print(f"Chosen move: {move.uci()}")
    print(f"Board FEN after move: {board.fen()}")

    safe, message = run_safety_checks(motion, robot_config)
    print(f"Safety check: {message}")

    if not safe:
        print("Motion blocked.")
        return

    execute_motion(motion, dry_run=robot_config["robot"]["dry_run"])

if __name__ == "__main__":
    main()
