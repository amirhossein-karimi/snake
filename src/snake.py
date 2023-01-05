
from src.tail import Tail
import random

class Snake:

    def __init__(self) -> None:
        self.tails = []
        self.tails.append(Tail(random.randint(1, 18),
                          random.randint(1, 18), None, None))

    def move(self, arrow='left') -> None:
        self.tails[0].px = self.tails[0].cx
        self.tails[0].py = self.tails[0].cy
        if arrow == 'left':
            self.tails[0].cy -= 1
        if arrow == 'right':
            self.tails[0].cy += 1
        if arrow == 'up':
            self.tails[0].cx -= 1
        if arrow == 'down':
            self.tails[0].cx += 1

        for x in range(1, len(self.tails)):
            self.tails[x].py = self.tails[x].cy
            self.tails[x].px = self.tails[x].cx
            self.tails[x].cy = self.tails[x - 1].py
            self.tails[x].cx = self.tails[x - 1].px
        

    def add_tails(self) -> None:
        t = Tail(self.tails[-1].px, self.tails[-1].py, None, None)
        self.tails.append(t)
