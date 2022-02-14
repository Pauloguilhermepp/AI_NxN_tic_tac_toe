# Class that represents the tic-tac-toe game.
import pygame
import random
from Opponents import *
import numpy as np

# Class to represent tic tac toe game:
class Tic_tac_toe:
    # Constructor:
    def __init__(self, side = 3, window_size = 500, mode = "player_vs_player", opponent = "random_op"):
        self.board = [
            [0 for i in np.arange(side)] for j in np.arange(side)
        ]  # Creating board
        self.side = side  # Saving variable with board length

        self.window_size = window_size  # Saving screen size
        self.square_size = round(
            window_size / self.side
        )  # Size of the squares in the board
        self.mode = mode  # Game mode
        self.opponent = opponent # Choosing opponent

    # Function to test if someone won:
    def checking_winer(self):

        # Checking rows:
        for row in np.arange(self.side):
            symb = self.board[row][0]

            if symb == 0:
                continue

            for symbol in np.arange(1, self.side):
                if symb == self.board[row][symbol]:
                    if symbol == self.side - 1:
                        return True
                    continue
                else:
                    break

        # Checking columns:
        for col in np.arange(self.side):
            symb = self.board[0][col]

            if symb == 0:
                continue

            for symbol in np.arange(1, self.side):
                if symb == self.board[symbol][col]:
                    if symbol == self.side - 1:
                        return True
                    continue
                else:
                    break

        # Checking main diagonal:
        for id in np.arange(self.side):
            symb = self.board[0][0]

            if symb == 0:
                break

            if symb == self.board[id][id]:
                if id == self.side - 1:
                    return True
                continue
            else:
                break

        # Checking other diagonal:
        for id in np.arange(self.side):
            symb = self.board[self.side - 1][0]

            if symb == 0:
                break

            if symb == self.board[self.side - id - 1][id]:
                if id == self.side - 1:
                    return True
                continue
            else:
                break

        return False

    # Checking draw:
    def checking_draw(self):
        for i in np.arange(self.side):
            for j in np.arange(self.side):
                if self.board[i][j] == 0:
                    return False

        return True

    # Checking if the move is inside the game board:
    def is_inside(self, x, y):
        # Checking if "x" is in the correct range:
        if x < 0 or x >= self.side:
            return False

        # Checking if "y" is in the correct range:
        if y < 0 or y >= self.side:
            return False

        return True

    # Checking if the position is empty:
    def is_empty(self, x, y):
        if self.board[x][y] != 0:
            return False

        return True

    # Checking if it is a valid movement:
    def valid_movement(self, x, y):
        if(self.is_inside(x, y) and self.is_empty(x, y)):
            return True

        return False

    # Function to make some movement:
    def movement(self, player, x, y):
        if self.valid_movement(x, y):
            self.board[x][y] = player
            self.draw_move(player, x, y)
            return True

        print("Invalid movement, please try again.")
        return False

    # Function to run for each player turn:
    def player_turn(self, player, x, y):

        if self.movement(player, x, y):

            if self.checking_winer():
                print("Player {player} won this game!".format(player = player))
                self.game_on = False

            elif self.checking_draw():
                print("The game tied!")
                self.game_on = False

            return True

        return False

    # Draw perimeter of the board:
    def draw_edge(self):
        rect = pygame.Rect(0, 0, self.window_size, self.window_size)
        pygame.draw.rect(self.screen, (200, 200, 200), rect, 3)

    # Drawing a grid in the screen:
    def draw_grid(self):

        self.draw_edge()

        for x in np.arange(0, self.window_size, self.square_size):
            for y in np.arange(0, self.window_size, self.square_size):
                rect = pygame.Rect(x, y, self.square_size, self.square_size)
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)

    # Draw circle with adjustable thickness:
    def draw_o(self, x, y, thic):
        circle_color = (200, 200, 200)
        radius = self.square_size // 2 - 5
        pygame.draw.circle(self.screen, circle_color, (x, y), radius, width=0)

        bg_color = (0, 0, 0)
        radius -= thic
        pygame.draw.circle(self.screen, bg_color, (x, y), radius, width=0)

    # Draw X function:
    def draw_x(self, x, y, thic):
        rect_color = (200, 200, 200)
        adust = self.square_size // 2 - 10

        x0, y0, x2, y2 = x - adust, y + adust, x + adust, y - adust
        x1, y1, x3, y3 = x + adust, y + adust, x - adust, y - adust
        pygame.draw.line(self.screen, rect_color, (x0, y0), (x2, y2), width=thic)
        pygame.draw.line(self.screen, rect_color, (x1, y1), (x3, y3), width=thic)

    # Draw player movement:
    def draw_move(self, player, x, y):
        xpos = x * self.square_size + self.square_size // 2
        ypos = y * self.square_size + self.square_size // 2

        if player == "x":
            self.draw_x(xpos, ypos, 3)
        else:
            self.draw_o(xpos, ypos, 3)

    # Change player turn:
    def change_player(self):
        if self.current_player_symb == "x":
            self.current_player_symb = "o"
        
        else:
            self.current_player_symb = "x"

    # Function to run the game:
    def run(self):

        if self.mode == "player_vs_player":
            self.run_player_vs_player()

        elif self.mode == "player_vs_bot":
            self.run_player_vs_bot()

        elif self.mode == "bot_vs_bot":
            print("TODO: it mode will be added in the future")

    # Creating mode player vs player:
    def run_player_vs_player(self):

        self.game_on = True
        self.current_player_symb = "x"

        print("Starting tic-tac-toe game!")
        print("It is {player} time: ".format(player = self.current_player_symb))

        pygame.init()
        self.screen = pygame.display.set_mode(
            [self.window_size, self.window_size]
        )  # Creating screen

        while self.game_on:
            self.draw_grid()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_on = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed():
                        xpos, ypos = pygame.mouse.get_pos()
                        xpos, ypos = (xpos // self.square_size), (
                            ypos // self.square_size
                        )
                        if (
                            self.player_turn(self.current_player_symb, xpos, ypos)
                            and self.game_on
                        ):
                            self.change_player()
                            print(
                                "It is {player} time: ".format(
                                    player = self.current_player_symb
                                )
                            )

            pygame.display.update()

        pygame.quit()

    # Deciding who will start:
    def first_to_play(self):
        if random.random() < 0.5:
            return ["Human", "Bot"]

        return ["Bot", "Human"]

    # Defining opponent:
    def choose_opponent(self):
        if(self.opponent == "random_op"):
            self.opponent_move = random_op.move
        
        elif(self.opponent == "dumb_minimax_op"):
            self.opponent_move = dumb_minimax_op.move
            
    # Creating mode player vs bot:
    def run_player_vs_bot(self):

        self.choose_opponent()

        player1, player2 = self.first_to_play()

        self.game_on = True
        self.current_player = player1
        self.current_player_symb = "x"

        print("Starting tic-tac-toe game!")
        print("{Player1} will be the x".format(Player1 = player1))
        print("{Player2} will be the o".format(Player2 = player2))
        print("It is {player} time: ".format(player = self.current_player_symb))

        pygame.init()
        self.screen = pygame.display.set_mode(
            [self.window_size, self.window_size]
        )  # Creating screen

        while self.game_on:
            self.draw_grid()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_on = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() and self.current_player == "Human":
                        xpos, ypos = pygame.mouse.get_pos()
                        xpos, ypos = (xpos // self.square_size), (
                            ypos // self.square_size
                        )
                        if (
                            self.player_turn(self.current_player_symb, xpos, ypos)
                            and self.game_on
                        ):
                            self.change_player()
                            print(
                                "It is {player} time: ".format(
                                    player = self.current_player_symb
                                )
                            )
                            self.current_player = "Bot"

            if self.current_player == "Bot":
                # xpos, ypos = random_op.move(self)
                xpos, ypos = self.opponent_move(self)
                if self.player_turn(self.current_player_symb, xpos, ypos):
                    if self.game_on:
                        self.change_player()
                        print(
                            "It is {player} time: ".format(
                                player = self.current_player_symb
                            )
                        )
                        self.current_player = "Human"
                else:
                    print(
                        "Bot tired to make an invalid movement, program will finish now."
                    )
                    self.game_on = False

            pygame.display.update()

        pygame.quit()
