from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.user = Human()
        self.opponent

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
        pass

    def display_gestures(self):
        pass

    def user_select(self):
        pass

    def opponent_select(self):
        pass

    def display_round_winner(self):
        pass

    def track_score(self):
        pass

    def display_game_winner(self):
        pass
