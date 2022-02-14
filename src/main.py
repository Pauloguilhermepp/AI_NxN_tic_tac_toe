# Main file of the project.
from tic_tac_toe import Tic_tac_toe

# Main function:
def main():
    game = Tic_tac_toe(side = 3, mode = "player_vs_bot", opponent = "dumb_minimax_op")
    game.run()


if __name__ == "__main__":
    main()
