import numpy as np


def minimax(game_state, maximazing):
    if game_state.checking_winer():
        if not maximazing:
            return 1
        else:
            return -1

    elif game_state.checking_draw():
        return 0

    scores = []
    N = game_state.side

    for i in np.arange(N * N):
        x, y = i % N, i // N

        if game_state.is_empty(x, y):
            game_state.board[x][y] = game_state.current_player_symb

            game_state.change_player()

            scores.append(minimax(game_state, not maximazing))

            game_state.current_player_symb = game_state.board[x][y]

            game_state.board[x][y] = 0

    if maximazing:
        return max(scores)

    return min(scores)


def move(game_state):
    best_score = -10
    best_move = None

    N = game_state.side
    for i in np.arange(N * N):
        x, y = i % N, i // N

        current_player_symb = game_state.current_player_symb

        if game_state.is_empty(x, y):
            game_state.board[x][y] = game_state.current_player_symb

            game_state.change_player()

            new_score = minimax(game_state, False)

            game_state.board[x][y] = 0

            if new_score > best_score:
                best_score = new_score
                best_move = [x, y]

        game_state.current_player_symb = current_player_symb

    return best_move
