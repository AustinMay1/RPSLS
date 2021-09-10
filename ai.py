from player import Player
import random


class Ai(Player):
    def __init__(self):
        self.name = 'AI'
        super().__init__()

    def get_gesture(self):
        selection = random.choice(self.gestures)
        return selection
