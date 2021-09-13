from player import Player


class Human(Player):
    def __init__(self):
        super().__init__(self)

    def get_name(self):
        self.name = str(input("Please enter a name for the player: "))
        print("Player: ", self.name)

    def get_gesture(self):
        selection = str(
            input("What is your choice (rock, paper, scissors, lizard, spock): "))
        return selection
