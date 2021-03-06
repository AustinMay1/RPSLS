from player import Player
import random


class Ai(Player):
    def __init__(self):
        super().__init__()
        self.name = 'AI'
        self.type = 'ai'

    def get_gesture(self):
        selection = random.choice(self.gestures)
        return selection

    def get_name(self):
        return self.name
