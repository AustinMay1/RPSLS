from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.user = Human()
        self.opponent = Human()

    def run_game(self):
        self.display_rules()
        self.is_opponent_human_or_ai()
        self.get_names()
        self.start_round()
        self.display_game_winner()

    def display_rules(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
        print('')

    def is_opponent_human_or_ai(self):
        opp_type = input('Do you want to play multiplayer? y/n: ')
        if opp_type == 'y':
            self.opponent = Human()
        else:
            self.opponent = Ai()

    def get_names(self):
        user_name = self.user.get_name()
        print(user_name)
        opp_name = self.opponent.get_name()
        print(opp_name)

    def start_round(self):
        while (self.user.score < 2 and self.opponent.score < 2):
            user_select = self.user_select()
            opp_select = self.opponent_select()
            print(user_select, opp_select)
            self.play_round(user_select, opp_select)
        self.display_game_winner()
        play_again = input('Do you want to play again? y/n: ')
        if play_again == 'y':
            self.user.score = 0
            self.opponent.score = 0
            self.start_round()
        else:
            return

    def play_round(self, user_select, opponent_select):
        user_score = self.user.score
        opp_score = self.opponent.score
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
            pass


    def user_select(self):
        turn = self.user.get_gesture()
        return turn

    def opponent_select(self):
        turn = self.opponent.get_gesture()
        return turn

    def display_round_winner(self, user_score, opp_score):

        if self.user.score == user_score and self.opponent.score == opp_score:
            print('Tie')
        elif user_score < self.user.score:
            print(self.user.name, " Wins!")
        else:
            print(self.opponent.name, " Wins!")

    def print_score(self):
        print(f'{self.user.name} has :{self.user.score} points.')
        print(f'{self.opponent.name} has :{self.opponent.score} points.')

    def display_game_winner(self):
        if self.user.score > self.opponent.score:
            print(self.user.name, " wins the game")
        else:
            print(self.opponent.name, " wins the game")

    


