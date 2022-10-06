import pyfiglet
import random
import re
from hangman_colors import COLORS
from hangman_words import WORD_LIST


secret_word = None
secret_word_display = []
guess = None
game_over = False


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


def get_player_guess():
    '''
    Get the player's guess (letter) by creating an input 'Guess a letter: '
    Set the player's (answer) input letter to lower case.
    Store the answer in the guess variable.
    Runs a while (loop) guess_error to give player input error feedback and
    give the player a new chance to guess a letter (input).
    '''
    global guess
    guess = input('Guess a letter: ').lower()
    guess_error = True
    while guess_error:
        if not re.match('^[a-z]*$', guess):
            print('\nError! Please enter one letter from the alphabet a-z.\n')
            guess = input('Guess a letter: ').lower()
        elif len(guess) > 1:
            print('\nError! Please enter one letter from the alphabet a-z.\n')
            guess = input('Guess a letter: ').lower()
        elif re.match('^\s*$', guess):
            print('\nError! Please enter one letter from the alphabet a-z.\n')
            guess = input('Guess a letter: ').lower()
        else:
            break


def add_correct_guess_to_display(guess):
    '''
    Checks if player guessed letter is in secret word.
    If so, adds the guess to display_secret_word (replaces underscore (blank) with guessed letter).
    '''
    for ind in range(len(secret_word)):
        letter = secret_word[ind]
        if letter == guess:
            secret_word_display[ind] = letter
    
    print(f"\n{' '.join(secret_word_display)}\n")


def check_won_game():
    '''
    Checks if there are no underscores (blanks) left in secret_word_display.
    If so, sets variable game_over to True.
    '''
    global game_over
    if '_' not in secret_word_display:
        game_over = True


def play_hangman():
    '''
    Creates a while loop for when variable game_over equals false.
    In the loop while not game_over:
    Calls functions get_player_guess(), display_hangman_logo('red', 'reset'), add_correct_guess_to_display(guess),
    check_won_game()
    '''
    global game_over
    
    while not game_over:
        get_player_guess()
        
        display_hangman_logo('red', 'reset')

        add_correct_guess_to_display(guess)
        
        check_won_game()

        
play_hangman()