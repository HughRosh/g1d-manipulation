from chess_engine import get_test_move

def main():
    fen, move = get_test_move()
    print("G1-D Chess")
    print(f"Test move: {move}")
    print(f"Board FEN: {fen}")

if __name__ == "__main__":
    main()
