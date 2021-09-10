from player import Player

class Human(Player):
    def __init__ (self):
        super().__init__(self)
        self.choice = str(input("What is your choice (rock, paper, scissors, lizard, spock): "))


    def get_name (self):
        self.name = input("Please enter a name for the player: ")
        print("Player: ",self.name)

    def get_gesture (self):
        while self.choice in self.gestures:
            pass
        else :
            return self.choice

            
        
            

        
            
        



