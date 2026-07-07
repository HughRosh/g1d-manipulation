import chess

def get_test_move():
    board = chess.Board()
    move = chess.Move.from_uci("e2e4")

    if move in board.legal_moves:
        board.push(move)

    return board.fen(), move.uci()
