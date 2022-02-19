# Ai NxN Tic tac toe
## Description
Tic tac toe game with changeable board size. It has both multiplayer and single player mode (in this last one it is possible to play against different opponents).


<p align="center">
  <img src="https://github.com/Pauloguilhermepp/AI_NxN_tic_tac_toe/blob/main/Imgs/tictactoe_img.png?">
</p>

## Running a game
Inside the `src` folder there is an example of how to run a game in the `main.py` file. Details about how to create a multiplayer game or choose some specific bot to play against are explained below.

## Game parameters
Some important parameters of the game class:

* **side**: Size of the board of the game (number of squares on the side). 

* **window_size**: Size in pixels of the game screen.

* **mode**: Sets if the game will be with two human players (in this case its value is **palyer_vs_player**), with a human and a bot (**player_vs_bot**) or with two bots (**bot_vs_bot**).

* **opponent**: Defines which bot will be the opponent. Possible values are: **random_op**, **dumb_minimax_op**, **alpha_beta_minimax_op** or **heuristic_alpha_beta_minimax_op**.

* **bots**: Defines which bots will play against themselves.