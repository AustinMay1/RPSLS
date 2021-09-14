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
        play_status = True
        while(play_status == True):
            self.start_rounds()
            self.display_game_winner()
            play_status = self.play_again()

    def display_rules(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
        print('Play vs AI or a human opponent!')
        print('Pick one of five gestures against your opponent and compare them. Winner gets a point and the first player to 2 points wins the entire match!')
        print('rock crushes scissors')
        print('scissors cuts paper')
        print('paper covers rock')
        print('rock crushes lizard')
        print('lizard poisons spock')
        print('spock smashes scissors')
        print('scissors decapitates lizard')
        print('lizard eats paper')
        print('paper disproves spock')
        print('spock vaporizes rock')

    def is_opponent_human_or_ai(self):
        valid_multi_input = self.validate_yes_no('multiplayer')
        if valid_multi_input == 'y':
            pass
        else:
            self.opponent = Ai()

    def get_names(self):
        self.validate_name(self.user)
        print(f'Player 1\'s name is {self.user.name}')
        if (self.opponent.type != 'ai'):
            self.validate_name(self.opponent)
            print(f'Player 2\'s name is {self.opponent.name}')
        else:
            print(f'Player 2\'s name is {self.opponent.name}')

    def start_rounds(self):
        while (self.user.score < 2 and self.opponent.score < 2):
            user_select = self.user_select().lower()
            opp_select = self.opponent_select().lower()
            print(f'{self.user.name} selected {user_select}.')
            print(f'{self.opponent.name} selected {opp_select}.')
            self.play_round(user_select, opp_select)

    def play_round(self, user_select, opponent_select):
        user_score = self.user.score
        opp_score = self.opponent.score
        self.compare_gestures(user_select, opponent_select)
        self.display_score()
        self.display_round_winner(user_score, opp_score)

    def compare_gestures(self, user_select, opponent_select):
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
        selection = self.select_gesture(self.user)
        return selection

    def opponent_select(self):
        selection = self.select_gesture(self.opponent)
        return selection

    def display_round_winner(self, user_score, opp_score):
        if self.user.score == user_score and self.opponent.score == opp_score:
            print('You tied!')
        elif user_score < self.user.score:
            print(self.user.name, "wins the round!")
        else:
            print(self.opponent.name, "wins the round!")

    def display_score(self):
        print(f'{self.user.name} has: {self.user.score} points.')
        print(f'{self.opponent.name} has: {self.opponent.score} points.')

    def display_game_winner(self):
        if self.user.score > self.opponent.score:
            print(self.user.name, "wins the best of three!")
        else:
            print(self.opponent.name, "wins the best of three!")

    def select_gesture(self, user):
        while(True):
            gesture = user.get_gesture()
            if self.validate_gesture(gesture, user) == True:
                return gesture
            else:
                print('Invalid input, try again.')

    def play_again(self):
        valid_play_again = self.validate_yes_no('play_again')
        if valid_play_again == 'y':
            self.user.score = 0
            self.opponent.score = 0
            return True
        else:
            return False

    def convert_to_y_or_n(self, user_input):
        if user_input.lower() == 'yes' or user_input.lower() == 'y':
            return 'y'
        elif user_input.lower() == 'no' or user_input.lower() == 'n':
            return 'n'
        else:
            return 'invalid'

    def validate_yes_no(self, type):
        valid = False
        while(valid == False):
            if type == 'multiplayer':
                user_input = str(
                    input('Do you want to play multiplayer? y/n: '))
            else:
                user_input = str(input('Do you want to play again? y/n: '))
            user_question = self.convert_to_y_or_n(user_input)
            if user_question == 'invalid':
                valid = False
                print('Invalid input, try again.')
            elif user_question == 'y' or 'n':
                valid = True
                return user_question
            else:
                valid = False

    def validate_gesture(self, user_input, user):
        for gesture in user.gestures:
            if user_input.lower() == gesture:
                return True

    def validate_name(self, user):
        valid = False
        while(valid == False):
            user.get_name()
            if len(user.name) < 25 and user.name.isalpha() == True:
                valid = True
                return user.name
            else:
                print('Invalid input, try again.')
