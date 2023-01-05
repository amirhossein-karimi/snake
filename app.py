
from src.gameboard import GameBoard
from src.food import Food
from src.snake import Snake
import time


g = GameBoard()
g.add_food(Food())
g.add_snake(Snake())
g.fill_game_board()
g.print_game_board()

while True:
    g.run()
    time.sleep(0.2)
    