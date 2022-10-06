import pyfiglet
import random
from hangman_colors import COLORS
from hangman_words import WORD_LIST


def display_hangman_logo(colorStart, colorEnd):
    """
    Prints hangman_logo with pyfiglet module which takes ASCII text and renders it in ASCII art font 'letter'.
    Applies an Ansi color code to hangman_logo and an Ansi color code to apply after hangman_logo display.
    Can choose from the following colors: 'red', 'purple', 'yellow', 'blue', 'reset'
    Color 'reset' used for colorEnd will end the colorStart color, so text after hangman logo will be reset to white. 
    """
    print('\n')
    hangman_logo = COLORS[colorStart] + pyfiglet.figlet_format('_   hangman',font='letters') + COLORS[colorEnd]
    print(hangman_logo)


display_hangman_logo('red', 'reset')


secret_word = random.choice(WORD_LIST)