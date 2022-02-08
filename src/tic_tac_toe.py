# Class that represents the tic-tac-toe game.
import pygame
import numpy as np

# Class to represent tic tac toe game:
class Tic_tac_toe:
    # Constructor:
    def __init__(self, side=3, window_size=500):
        self.board = [
            [0 for i in np.arange(side)] for j in np.arange(side)
        ]  # Creating board
        self.side = side  # Saving variable with board length

        self.window_size = window_size  # Saving screen size
        self.square_size = round(window_size / self.side)

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

    # Checking if it is a valid movement:
    def valid_movement(self, x, y):

        # Checking if "x" is in the correct range:
        if x < 0 or x >= self.side:
            return False

        # CHecking if "y" is in the correct range:
        if y < 0 or y >= self.side:
            return False

        # Checking if the position is empty:
        if self.board[x][y] != 0:
            return False

        return True

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
                print("Player {player} won this game!".format(player=player))
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
        """bg_color = (0, 0, 0)
        radius -= thic
        pygame.draw.circle(self.screen, bg_color, (x, y), radius, width = 0)"""

    # Draw player movement:
    def draw_move(self, player, x, y):
        xpos = x * self.square_size + self.square_size // 2
        ypos = y * self.square_size + self.square_size // 2

        if player == "x":
            self.draw_x(xpos, ypos, 3)
        else:
            self.draw_o(xpos, ypos, 3)

    # Change player turn:
    def change_player(self, player):
        if player == "x":
            return "o"
        else:
            return "x"

    # Function to run the game:
    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            [self.window_size, self.window_size]
        )  # Creating screen

        self.game_on = True
        current_player = "x"

        print("Starting tic-tac-toe game!")
        print("It is {player} time: ".format(player=current_player))

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
                            self.player_turn(current_player, xpos, ypos)
                            and self.game_on
                        ):
                            current_player = self.change_player(current_player)
                            print("It is {player} time: ".format(player=current_player))

            pygame.display.update()

        pygame.quit()
