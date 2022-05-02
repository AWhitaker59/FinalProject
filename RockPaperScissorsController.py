from PyQt5.QtWidgets import *
from RockPaperScissorsUI import Ui_RockPaperScissors
import random


def computer_choice():
    """
    The computer_choice function uses the random module to randomly select the
    AI's choice of 'rock', 'paper', or 'scissors'

    :return: AI's choice of 'rock', 'paper', or 'scissors'
    """
    ai_hand = random.randint(1, 3)
    if ai_hand == 1:
        ai_hand = 'rock'
    elif ai_hand == 2:
        ai_hand = 'paper'
    elif ai_hand == 3:
        ai_hand = 'scissors'
    return ai_hand


class Controller(QMainWindow, Ui_RockPaperScissors):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.game_over = 0
        self.player_wins = 0
        self.ai_wins = 0
        self.Submit.clicked.connect(lambda: self.game_start())

    def player_choice(self):
        """
        The player_choice function returns a string input from the human player, after
        ensuring that the input is a valid one.

        :return: The player's choice of 'rock', 'paper', or 'scissors'
        """
        choice = ''
        if self.radioButton_Rock.isChecked():
            choice = 'rock'
        elif self.radioButton_Paper.isChecked():
            choice = 'paper'
        elif self.radioButton_Scissors.isChecked():
            choice = 'scissors'
        else:
            self.browser_Game.append('Select a Hand!')
        return choice

    def run_game(self, player, ai):
        victor = ''
        if player == ai:
            self.browser_Game.append('Computer is {}. You are {}. You tie.'.format(ai, player))
        elif player == 'rock':
            if ai == 'paper':
                self.browser_Game.append('Computer is paper. You are rock. You lose the round.')
                victor = 'AI'
            elif ai == 'scissors':
                self.browser_Game.append('Computer is scissors. You are rock. You win the round.')
                victor = 'Player'
        elif player == 'paper':
            if ai == 'rock':
                self.browser_Game.append('Computer is rock. You are paper. You win the round.')
                victor = 'Player'
            elif ai == 'scissors':
                self.browser_Game.append('Computer is scissors. You are paper. You lose the round.')
                victor = 'AI'
        elif player == 'scissors':
            if ai == 'rock':
                self.browser_Game.append('Computer is rock. You are scissors. You lose the round.')
                victor = 'AI'
            elif ai == 'paper':
                self.browser_Game.append('Computer is paper. You are scissors. You Win the round.')
                victor = 'Player'
        else:
            pass
        return victor

    def win_state(self):
        if self.ai_wins == self.player_wins:
            return "GAME OVER-IT'S A TIE"
        elif self.ai_wins < self.player_wins:
            return "GAME OVER-YOU WIN"
        elif self.ai_wins > self.player_wins:
            return "GAME OVER-COMPUTER WINS"

    def reset(self):
        self.game_over = 0
        self.player_wins = 0
        self.ai_wins = 0

    def game_start(self):
        self.game_over += 1
        if self.game_over == 3:
            self.browser_Game.append(self.win_state())
            self.browser_Game.append('NEW GAME')
            self.reset()
        elif self.ai_wins == 2 and self.game_over == 2:
            self.browser_Game.append(self.win_state())
            self.browser_Game.append('NEW GAME')
            self.reset()
        elif self.player_wins == 2 and self.game_over == 2:
            self.browser_Game.append(self.win_state())
            self.browser_Game.append('NEW GAME')
            self.reset()

        victor = self.run_game(self.player_choice(), computer_choice())
        if victor == 'AI':
            self.ai_wins += 1
        elif victor == 'Player':
            self.player_wins += 1
        else:
            pass
