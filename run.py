import pyfiglet
import random
from hangman_words import WORD_LIST


def display_hangman_logo(colorStart, colorEnd):
    """
    Prints hangman_logo with pyfiglet module which takes ASCII text and renders it in ASCII art font 'letter'.
    Applies an Ansi color code to hangman_logo and an Ansi color code to apply after hangman_logo display.
    """
    print("\n")
    hangman_logo = apply_color(colorStart) + pyfiglet.figlet_format('_   hangman',font='letters') + apply_color(colorEnd)
    print(hangman_logo)


def apply_color(color):
    """
    Returns an Ansi color code
    """
    if color == 'red':
        return '\033[1;31m'
    if color == 'purple':
        return '\033[0;35m'
    if color == 'yellow':
        return '\033[1;33m'
    if color == 'blue':
        return '\033[0;34m'
    if color == 'reset':
        return '\033[0m'


display_hangman_logo('red', 'reset')


secret_word = random.choice(WORD_LIST)