from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def get_name(self):
        self.name = str(input("Please enter a name for the player: "))

    def get_gesture(self):
        selection = str(
            input(f"What is your choice {self.name}? (rock, paper, scissors, lizard, spock): "))
        return selection
