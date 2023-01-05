import os

from src.food import Food
from src.colors import BColors
import keyboard


class GameBoard:

    def __init__(self) -> None:
        self.x = 20
        self.y = 20
        self.game_board_char = '*'
        self.food = None
        self.snake = None
        self.game_board = [[' '] * self.y for i in range(self.x)]
        self.arrow = 'left'

    def add_food(self, food) -> None:
        self.food = food
        self.game_board[self.food.x][self.food.y] = f"{BColors.OKGREEN}#"

    def add_snake(self, snake) -> None:
        self.snake = snake

    def fill_game_board(self) -> None:
        for x in range(self.x):
            for y in range(self.y):
                if x == 0 or x == self.x - 1:
                    self.game_board[x][y] = f"{BColors.WARNING}{self.game_board_char}"
                if y == 0 or y == self.y - 1:
                    self.game_board[x][y] = f"{BColors.WARNING}{self.game_board_char}"

    def print_game_board(self) -> None:
        os.system('cls')
        for x in range(self.x):
            for y in range(self.y):
                print(self.game_board[x][y], end='   ')
            print("\n")
        print(f'{BColors.OKGREEN}SCORE:', len(self.snake.tails ))
  

    def print_snake(self) -> None:

        self.game_board[self.snake.tails[0]
                        .cx][self.snake.tails[0].cy] = f"{BColors.WARNING}@"

        for x in range(1, len(self.snake.tails)):

            self.game_board[self.snake.tails[x]
                            .cx][self.snake.tails[x].cy] = f"{BColors.OKCYAN}O"

    def eat_food(self) -> None:
        if self.snake.tails[0].cx == self.food.x and self.snake.tails[0].cy == self.food.y:
            self.add_food(Food())
            self.snake.add_tails()   
        

    def run(self):

        self.game_board[self.snake.tails[-1].cx][self.snake.tails[-1].cy] = ' '
        self.snake.tails[0].px = self.snake.tails[0].cx
        self.snake.tails[0].py = self.snake.tails[0].cy

        if keyboard.is_pressed('up') and self.arrow != 'down':
            self.arrow = 'up'
        if keyboard.is_pressed('right') and self.arrow != 'left':
            self.arrow = 'right'
        if keyboard.is_pressed('left') and self.arrow != 'right':
            self.arrow = 'left'
        if keyboard.is_pressed('down') and self.arrow != 'up':
            self.arrow = 'down'

        if self.snake.tails[0].cx == 0 or self.snake.tails[0].cx == 19 or self.snake.tails[0].cy == 0 or self.snake.tails[0].cy == 19:
            os.system('cls')
            print('YOU LOSE , YOUR SCORE IS ' , len(self.snake.tails));
            exit()
        
        i = 0;
        for x in self.snake.tails:
            if(len(self.snake.tails) > 1):
                    if (i != 0):
                        if self.snake.tails[0].cx == x.cx and self.snake.tails[0].cy == x.cy:
                            os.system('cls')
                            print('YOU LOSE , YOUR SCORE IS ' , len(self.snake.tails));
                            exit();
                    i +=1       
        self.snake.move(self.arrow)

        self.print_snake()

        self.eat_food()

        self.print_game_board()

