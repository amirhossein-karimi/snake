import random

class Food:
    def __init__(self) -> None:
        self.x = random.randint(1, 18)
        self.y = random.randint(1, 18)
