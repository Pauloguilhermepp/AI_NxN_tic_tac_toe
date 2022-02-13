import numpy as np

def minimax(game_state, maximazing, current_player_symb):
    if(game_state.checking_winer()):
        if(not maximazing):
            return 1
        else:
            return -1
    
    elif(game_state.checking_draw()):
        return 0
    
    scores = []
    N = game_state.side

    for i in np.arange(N * N):
        x, y = i % N, i // N

        if(game_state.board[x][y] == 0):
            game_state.board[x][y] = current_player_symb
            
            if(current_player_symb == "o"):
                current_player_symb = "x"
            
            else:
                current_player_symb = "o" 
            
            scores.append(minimax(game_state, not maximazing, current_player_symb))

            current_player_symb = game_state.board[x][y]
            game_state.board[x][y] = 0

    if(maximazing):
        return max(scores)

    else:
        return min(scores)

def move(game_state):
    best_score = -10
    best_move = None

    N = game_state.side
    for i in np.arange(N * N):
        x, y = i % N, i // N

        current_player_symb = game_state.current_player_symb

        if(game_state.board[x][y] == 0):
            game_state.board[x][y] = current_player_symb

            if(current_player_symb == "o"):
                current_player_symb = "x"
            
            else:
                current_player_symb = "o" 

            new_score = minimax(game_state, False, current_player_symb)
            
            game_state.board[x][y] = 0

            if(new_score > best_score):
                best_score = new_score
                best_move = [x, y]

    return best_move