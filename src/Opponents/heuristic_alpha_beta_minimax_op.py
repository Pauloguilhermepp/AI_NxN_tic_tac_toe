import math
import numpy as np


def heuristic_function(game_state, maximazing):
    pontuation = 0
    symb = game_state.current_player_symb

    # Checking rows:
    for row in np.arange(game_state.side):
        plus = 0
        minus = 0

        for symbol in np.arange(game_state.side):
            if symb == game_state.board[row][symbol]:
                plus += 1
            elif(game_state.board[row][symbol] != 0):
                minus += 1
            
            if(plus > 0 and minus > 0):
                plus = 0
                minus = 0
                break
        
        pontuation += plus - minus

    # Checking columns:
    for col in np.arange(game_state.side):
        plus = 0
        minus = 0

        for symbol in np.arange(game_state.side):
            if symb == game_state.board[symbol][col]:
                plus += 1
            elif(game_state.board[symbol][col] != 0):
                minus += 1

            if(plus > 0 and minus > 0):
                plus = 0
                minus = 0
                break
        
        pontuation += plus - minus

    # Checking main diagonal:
    plus = 0
    minus = 0
    
    for id in np.arange(game_state.side):

        if symb == game_state.board[id][id]:
            plus += 1
        elif(game_state.board[id][id] != 0):
            minus += 1 

        if(plus > 0 and minus > 0):
            plus = 0
            minus = 0
            break
    
    pontuation += plus - minus

    # Checking other diagonal:
    plus = 0
    minus = 0

    for id in np.arange(game_state.side):

        if symb == game_state.board[game_state.side - id - 1][id]:
            plus += 1
        elif(game_state.board[game_state.side - id - 1][id] != 0):
            minus += 1

        if(plus > 0 and minus > 0):
            plus = 0
            minus = 0
            break
    
    pontuation += plus - minus

    if(maximazing):
        return pontuation

    return -pontuation

def minimax(game_state, maximazing, alpha, beta, depth):
    
    if game_state.checking_winer():
        if not maximazing:
            return math.inf
        else:
            return -math.inf

    elif game_state.checking_draw():
        return 0

    elif(depth == 0):
        return heuristic_function(game_state, maximazing)
    
    max_score = -math.inf
    min_score =  math.inf
    
    N = game_state.side

    
    for i in np.arange(N * N):
        x, y = i % N, i // N

        if game_state.is_empty(x, y):
            game_state.board[x][y] = game_state.current_player_symb

            game_state.change_player()

            score = minimax(game_state, not maximazing, alpha, beta, depth - 1)

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
    best_score = -math.inf
    best_move = None
    depth = 2

    N = game_state.side
    for i in np.arange(N * N):
        x, y = i % N, i // N

        current_player_symb = game_state.current_player_symb

        if game_state.is_empty(x, y):
            game_state.board[x][y] = game_state.current_player_symb

            game_state.change_player()

            new_score = minimax(game_state, False, -math.inf, math.inf, depth)

            game_state.board[x][y] = 0

            if new_score > best_score:
                best_score = new_score
                best_move = [x, y]

        game_state.current_player_symb = current_player_symb

    return best_move
