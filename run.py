import pyfiglet
import random
import re
from hangman_colors import COLORS
from hangman_words import WORD_LIST
from hangman_art import STICKMAN_STAGES


secret_word = None
secret_word_display = []
guess = None
letters_guessed = []
lives = 6
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


def give_feedback_repeat_guess(guess):
    '''
    Checks if player's guess is in the variable letters_guessed.
    If so, prints feedback if the player already guessed the letter.
    '''
    if guess in letters_guessed:
        print(f"You've already guessed the letter {guess}. Try again!\n")


def lose_life_incorrect_guess(guess):
    '''
    Checks if player's guess is not in the secret_word.
    If so, checks if guess is not in letters_guess.
    If so, player loses a life (decrements variable lives by 1).
    '''
    global lives
    if guess not in secret_word:
        if guess not in letters_guessed:
            lives -= 1


def give_feedback_incorrect_guess(guess):
    '''
    Checks if player's guess is not in the secret_word.
    Is so, checks if guess is not in letters_guessed.
    If so, feedback is given to the player that they lost a life and that their guess is not in the secret word.
    '''
    if guess not in secret_word:
        if guess not in letters_guessed:
            print(f"You lost a life! Your guess is not in the secret word.\n")


def check_lost_game(guess):
    '''
    Checks if player's guess is not in the secret_word.
    If so, checks if lives is equal to zero (player has no more lives).
    If so, sets the game_over variable to True.
    '''
    global game_over
    if guess not in secret_word:
        if lives == 0:
            game_over = True


def give_feedback_lost_game(guess):
    '''
    Checks if player's guess is not in the secret_word.
    If so, checks if game_over variable is equal to True.
    If so, feedback is given to the player that they lost.
    '''
    if guess not in secret_word:
        if game_over == True:
            print('Sorry, you lost.\n')


def check_won_game():
    '''
    Checks if there are no underscores (blanks) left in secret_word_display.
    If so, sets variable game_over to True.
    '''
    global game_over
    if '_' not in secret_word_display:
        game_over = True


def give_feedback_won_game():
    '''
    Checks if there are no underscores (blanks) left in secret_word_display.
    If so, feedback is given to the player that they won.
    '''
    if '_' not in secret_word_display:
        print('Congratulations! You won.\n')


def display_stickman(lives):
    '''
    Prints the variable STICKMAN_STAGES at set index (current live) 
    with its formatted colors (.format(**COLORS)) from the dictionary COLORS.
    '''
    print(STICKMAN_STAGES[lives].format(**COLORS))


def display_letters_guessed(guess):
    '''
    Checks if guess is not in letters_guessed.
    If so, adds player's guess to letters_guessed list.
    Then Prints display Letters guessed: with guessed letters (all letters from letters_guessed list).
    '''
    if guess not in letters_guessed:
        letters_guessed.append(guess)
    print(f"Letters guessed: {', '.join(map(str, letters_guessed))}\n")


def play_hangman():
    '''
    Creates a while loop for when variable game_over equals false.
    In the loop while not game_over:
    Calls functions get_player_guess(), display_hangman_logo('red', 'reset'), add_correct_guess_to_display(guess),
    give_feedback_repeat_guess(guess), lose_life_incorrect_guess(guess), give_feedback_incorrect_guess(guess),
    check_lost_game(guess), give_feedback_lost_game(guess), check_won_game(), give_feedback_won_game(),
    display_stickman(lives), display_letters_guessed(guess)
    '''
    global game_over
    
    while not game_over:
        get_player_guess()
        
        display_hangman_logo('red', 'reset')

        add_correct_guess_to_display(guess)

        give_feedback_repeat_guess(guess)

        lose_life_incorrect_guess(guess)

        give_feedback_incorrect_guess(guess)

        check_lost_game(guess)

        give_feedback_lost_game(guess)

        check_won_game()

        give_feedback_won_game()

        display_stickman(lives)

        display_letters_guessed(guess)

 
play_hangman()