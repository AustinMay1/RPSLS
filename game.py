from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.user = Human()
        self.opponent = Human()

    def run_game(self):
        self.display_rules()
        self.is_opponent_human_or_ai()
        self.start_round()
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

    def start_round(self):
        user_name = self.user.get_name()
        print(user_name)
        opp_name = self.opponent.get_name()
        print(opp_name)
        while (self.user.score < 2 and self.opponent.score < 2):
            user_select = self.user_select()
            opp_select = self.opponent_select()
            print(user_select, opp_select)
            self.play_round(user_select, opp_select)

    def play_round(self, user_select, opponent_select):
        if user_select == 'rock' and opponent_select == 'scissors':
            self.user.score += 1
        elif user_select == 'scissors' and opponent_select == 'rock':
            self.opponent.score += 1
        elif user_select == 'scissors' and opponent_select == 'paper':
            self.user.score += 1
        elif user_select == 'paper' and opponent_select == 'scissors':
            self.opponent.score += 1
        elif user_select == 'paper' and opponent_select == 'rock':
            self.user.score += 1
        elif user_select == 'rock' and opponent_select == 'paper':
            self.opponent.score += 1
        elif user_select == 'rock' and opponent_select == 'lizard':
            self.user.score += 1
        elif user_select == 'lizard' and opponent_select == 'rock':
            self.opponent.score += 1
        elif user_select == 'lizard' and opponent_select == 'spock':
            self.user.score += 1
        elif user_select == 'spock' and opponent_select == 'lizard':
            self.opponent.score += 1
        elif user_select == 'spock' and opponent_select == 'scissors':
            self.user.score += 1
        elif user_select == 'scissors' and opponent_select == 'spock':
            self.opponent.score += 1
        elif user_select == 'scissors' and opponent_select == 'lizard':
            self.user.score += 1
        elif user_select == 'lizard' and opponent_select == 'scissors':
            self.opponent.score += 1
        elif user_select == 'lizard' and opponent_select == 'paper':
            self.user.score += 1
        elif user_select == 'paper' and opponent_select == 'lizard':
            self.opponent.score += 1
        elif user_select == 'paper' and opponent_select == 'spock':
            self.user.score += 1
        elif user_select == 'spock' and opponent_select == 'paper':
            self.opponent.score += 1
        elif user_select == 'spock' and opponent_select == 'rock':
            self.user.score += 1
        elif user_select == 'rock' and opponent_select == 'spock':
            self.opponent.score += 1
        else:
            print('You tied!')
        self.print_score()

    def user_select(self):
        turn = self.user.get_gesture()
        return turn

    def opponent_select(self):
        turn = self.opponent.get_gesture()
        return turn

    def display_round_winner(self):
        pass

    def print_score(self):
        print(f'{self.user.name} has :{self.user.score} points.')
        print(f'{self.opponent.name} has :{self.opponent.score} points.')

    def display_game_winner(self):
        pass
