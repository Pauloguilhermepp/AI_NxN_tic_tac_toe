import numpy as np


def minimax(game_state, maximazing, alpha, beta):
    if game_state.checking_winer():
        if not maximazing:
            return 1
        else:
            return -1

    elif game_state.checking_draw():
        return 0

    max_score = -10
    min_score =  10
    
    N = game_state.side

    
    for i in np.arange(N * N):
        x, y = i % N, i // N

        if game_state.is_empty(x, y):
            game_state.board[x][y] = game_state.current_player_symb

            game_state.change_player()

            score = minimax(game_state, not maximazing, alpha, beta)

            game_state.current_player_symb = game_state.board[x][y]

            game_state.board[x][y] = 0
            
            if(maximazing):
                max_score = max(max_score, score)
                alpha = max(alpha, score)

                if(beta <= alpha):
                    break
            
            else:
                min_score = min(min_score, score)
                beta = min(beta, score)

                if(beta <= alpha):
                    break


    
    if(maximazing):
        return max_score
    
    return min_score
    


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

            new_score = minimax(game_state, False, -10, 10)

            game_state.board[x][y] = 0

            if new_score > best_score:
                best_score = new_score
                best_move = [x, y]

        game_state.current_player_symb = current_player_symb

    return best_move
