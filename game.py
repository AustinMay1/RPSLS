from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.user = Human()
        self.opponent = Human()

    def run_game(self):
        self.display_rules()
        self.is_opponent_human_or_ai()
        self.play_round()
        self.display_game_winner()

    def display_rules(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
        print('')

    def is_opponent_human_or_ai(self):
        opp_type = input('Do you want to play multiplayer? y/n: ')
        if opp_type == 'n':
            self.opponent = Ai()
        else:
            self.opponent = Human()

    def play_round(self):
        user_name = self.user.get_name()
        print(user_name)
        opp_name = self.opponent.get_name()
        print(opp_name)
        self.user_select()
        self.opponent_select()
        

    def display_gestures(self):
        turn = self.user.get_gesture()
        print(turn)

    def user_select(self):
        turn = self.user.get_gesture()
        print(turn)
        

    def opponent_select(self):
        if self.opponent.type == 'ai':
            opponent_turn = self.opponent.get_gesture()
            print(opponent_turn)
        else:
            opponent_turn = self.opponent.get_gesture()
            print(opponent_turn)


    def display_round_winner(self):
        pass

    def track_score(self):
        pass

    def display_game_winner(self):
        pass
