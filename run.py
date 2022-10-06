import pyfiglet
import random
from hangman_colors import COLORS
from hangman_words import WORD_LIST


secret_word = None
secret_word_display = []


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


def create_secret_word():
    '''
    Assigns a random selected word from the WORD_LIST list to the secret_word variable.
    '''
    global secret_word
    secret_word = random.choice(WORD_LIST)


create_secret_word()


def display_secret_word():
    '''
    Displays the secret word (hidden) by replacing letters with blanks (underscores).
    '''
    for letter in secret_word:
        secret_word_display.append('_')

    print(f"{' '.join(secret_word_display)}\n")


display_secret_word()