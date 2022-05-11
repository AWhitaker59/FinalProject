from PyQt5.QtWidgets import *
from RockPaperScissorsUI import Ui_RockPaperScissors
import random


class Controller(QMainWindow, Ui_RockPaperScissors):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.game_over = 0
        self.player_wins = 0
        self.ai_wins = 0
        self.round = 1
        self.Submit.clicked.connect(lambda: self.game_start())

    def computer_choice(self):
        """
        The computer_choice function uses the random module to randomly select the
        AI's choice of 'rock', 'paper', or 'scissors'

        :return: AI's choice of 'rock', 'paper', or 'scissors'
        """
        ai_hand = random.randint(1, 3)
        if ai_hand == 1:
            ai_hand = 'rock'
            self.AI_rock_image.show()
            self.AI_scissors_image.hide()
            self.AI_paper_image_.hide()
        elif ai_hand == 2:
            ai_hand = 'paper'
            self.AI_paper_image_.show()
            self.AI_scissors_image.hide()
            self.AI_rock_image.hide()
        elif ai_hand == 3:
            ai_hand = 'scissors'
            self.AI_scissors_image.show()
            self.AI_paper_image_.hide()
            self.AI_rock_image.hide()
        return ai_hand

    def player_choice(self):
        """
        The player_choice function returns a string input from the human player, after
        ensuring that the input is a valid one.

        :return: The player's choice of 'rock', 'paper', or 'scissors'
        """
        choice = ''
        if self.radioButton_Rock.isChecked():
            choice = 'rock'
            self.Player_rock_image.show()
            self.Player_paper_image.hide()
            self.player_scissors_image.hide()
        elif self.radioButton_Paper.isChecked():
            choice = 'paper'
            self.Player_rock_image.hide()
            self.Player_paper_image.show()
            self.player_scissors_image.hide()
        elif self.radioButton_Scissors.isChecked():
            choice = 'scissors'
            self.Player_rock_image.hide()
            self.Player_paper_image.hide()
            self.player_scissors_image.show()
        else:
            self.win_state_label.setText("Choose a hand")
            choice = ''
        return choice

    def run_game(self, player, ai):
        """
        The function compares the choices of both the AI and the player to see who won the round

        :param player: return value of the player_choice function; string
        :param ai: return value of computer_choice function; string
        :return: returns who won the round; string
        """
        victor = ''
        if player == '':
            victor = ''
        if player == ai:
            pass
        elif player == 'rock':
            if ai == 'paper':
                victor = 'AI'
            elif ai == 'scissors':
                victor = 'Player'
        elif player == 'paper':
            if ai == 'rock':
                victor = 'Player'
            elif ai == 'scissors':
                victor = 'AI'
        elif player == 'scissors':
            if ai == 'rock':
                victor = 'AI'
            elif ai == 'paper':
                victor = 'Player'
        else:
            pass
        return victor

    def win_state(self):
        """
        Determine who won the best of 3 rounds based on the scores

        :return: The string of if the player won,lost, or tied, and states the scores PLAYER TO AI
        """
        if self.ai_wins == self.player_wins:
            return f'Tie! {self.player_wins} to {self.ai_wins}'
        elif self.ai_wins < self.player_wins:
            return f'You Win! {self.player_wins} to {self.ai_wins}'
        elif self.ai_wins > self.player_wins:
            return f'You Lose. {self.player_wins} to {self.ai_wins}'

    def reset(self):
        """
        This function is called at the end of a best of 3 game, and resets the all the variables for a new game
        """
        self.game_over = 0
        self.player_wins = 0
        self.ai_wins = 0
        self.round = 1
        self.player_score_label.hide()
        self.ai_score_label.hide()
        self.ai_score_label.setText(str(self.ai_wins))
        self.player_score_label.setText(str(self.player_wins))
        self.round_label.setText(f'Round:{self.round}')

    def game_start(self):
        """
        This is the primary function, called when "Submit" button is clicked.
        This function keeps track of rounds, counts the scores of each player, and calls
            the "choice" functions as well as the win_state function when a win state is reached
        """
        self.player_score_label.show()
        self.ai_score_label.show()
        self.round_label.setText(f'Round:{self.round}')
        self.round += 1
        self.win_state_label.setText('')
        self.game_over += 1
        victor = self.run_game(self.player_choice(), self.computer_choice())
        if victor == 'AI':
            self.ai_wins += 1
            self.ai_score_label.setText(str(self.ai_wins))
            self.player_score_label.setText(str(self.player_wins))
        elif victor == 'Player':
            self.player_wins += 1
            self.ai_score_label.setText(str(self.ai_wins))
            self.player_score_label.setText(str(self.player_wins))

        if self.ai_wins == 2:
            self.win_state_label.setText(self.win_state())
            self.reset()
        elif self.player_wins == 2:
            self.win_state_label.setText(self.win_state())
            self.reset()
        elif self.game_over == 3:
            self.win_state_label.setText(self.win_state())
            self.reset()