from chess_engine import get_test_move
from board_geometry import move_to_pick_place

def main():
    fen, move = get_test_move()
    plan = move_to_pick_place(move)

    print("G1-D Chess")
    print(f"Test move: {move}")
    print(f"Board FEN: {fen}")
    print("Pick/place plan:")
    print(plan)

if __name__ == "__main__":
    main()
