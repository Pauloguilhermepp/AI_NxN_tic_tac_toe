import random

list_of_movements = []

def move(game_state):
    global list_of_movements
    N = game_state.side

    if(len(list_of_movements) == 0):
        list_of_movements = list(range(0, N * N))
        random.shuffle(list_of_movements)

    for i in list_of_movements:
        x, y = i % N, i // N
        if(game_state.board[x][y] == 0):
            return [x, y]
