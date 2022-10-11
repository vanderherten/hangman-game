import pyfiglet
import random
import re
import os
from hangman_colors import COLORS
from hangman_words import WORD_LISTS
from hangman_art import STICKMAN_STAGES
# Modules requests & BeautifulSoup are for the synonym hint feature
import requests
from bs4 import BeautifulSoup
# Module PyDictionary for the secret word definition feature
from PyDictionary import PyDictionary

hi_score = 0
current_score = 0
secret_word = None
secret_word_display = []
guess = None
letters_guessed = []
lives = 6
game_over = False
hint = True


def clear_screen():
    '''
    Clears terminal screen.
    First determines whether the os (operating system) is windows or linux or mac.
    Then executes clear screen code accordingly.
    If os.name is 'posix' which is for linux or mac, it executes specific os code.
    else will execute clear screen code for windows.
    '''
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


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


def display_scoreboard(hi_score, current_score):
    '''
    Displays Hangman Game's Scoreboard.
    Prints 'High Score: {hi_score}'
    Prints 'Current Max Score: {current_score}'
    The Current Max Score is the maximum score attainable with player's chosen word length,
    and will decrease when player loses lives.
    '''
    print(f'\nHigh Score: {hi_score}')
    print(f'\nCurrent Max Score: {current_score}\n')


display_scoreboard(hi_score, current_score)


def get_player_word_length():
    '''
    Gets the player's word length choice (number from 4 to 9) for the game.
    Player's input gets stored in the variable word_length_choice.
    Runs a while loop to give the player input error feedback and
    give the player a new chance to choose a word length for the game:
    input("\nPlease choose the game's word length. Pick a number from 4 to 9: ")
    Function returns int(word_length_choice value)
    '''
    while True:
        try:
            word_length_choice = input("\nPlease choose the game's word length. Pick a number from 4 to 9: ")
            while True:
                if not re.match('^[4-9]*$', word_length_choice):
                    print('\nError! Please enter one whole number from 4 to 9.\n')
                    word_length_choice = input("\nPlease choose the game's word length. Pick a number from 4 to 9: ")
                elif re.match('^\s*$', word_length_choice):
                    print('\nError! Please enter one whole number from 4 to 9.\n')
                    word_length_choice = input("\nPlease choose the game's word length. Pick a number from 4 to 9: ")
                elif len(word_length_choice) > 1:
                    print('\nError! Please enter one whole number from 4 to 9.\n')
                    word_length_choice = input("\nPlease choose the game's word length. Pick a number from 4 to 9: ")
                else:
                    break
        except:
            print('\nError! Please enter one whole number from 4 to 9.\n')
        else:
            break
    
    return int(word_length_choice)


word_length = get_player_word_length()
    

clear_screen()


display_hangman_logo('red', 'reset')


def update_current_score(word_length):
    '''
    Calculates current_score according to word_length points per life.
    Returns current_score
    '''
    global lives, current_score
    
    if word_length == 4:
        current_score = 10 * lives
    if word_length == 5:
        current_score = 20 * lives
    if word_length == 6:
        current_score = 30 * lives
    if word_length == 7:
        current_score = 40 * lives
    if word_length == 8:
        current_score = 50 * lives
    if word_length == 9:
        current_score = 60 * lives
    
    return current_score


display_scoreboard(hi_score, update_current_score(word_length))


def update_hi_score():
    '''
    Checks if hi_score is smaller than current_score
    If so, updates hi_score to current_score
    Returns hi_score
    '''
    global hi_score
    if hi_score < current_score:
        hi_score = current_score
    return hi_score


def create_secret_word(word_length):
    '''
    Assigns a random selected word from the WORD_LISTS list to the secret_word variable.
    The player's chosen word length get's used as an index (int(word_length - 4)) to pick a random word
    from the correct word length list.
    '''
    global secret_word
    secret_word = random.choice(WORD_LISTS[word_length - 4])  


create_secret_word(word_length)


def display_secret_word():
    '''
    Displays the secret word (hidden) by replacing letters with blanks (underscores).
    '''
    for letter in secret_word:
        secret_word_display.append('_')

    print(f"\n{' '.join(secret_word_display)}\n")


display_secret_word()


def display_stickman(lives):
    '''
    Prints the variable STICKMAN_STAGES at set index (current live) 
    with its formatted colors (.format(**COLORS)) from the dictionary COLORS.
    '''
    print(STICKMAN_STAGES[lives].format(**COLORS))


display_stickman(lives)


def get_player_guess():
    '''
    Get the player's guess (letter): guess = input('Guess a letter: ').lower()
    Stores the answer in the guess variable.
    Runs a while (loop) to give the player input error feedback and
    give the player a new chance to guess a letter.
    '''
    global guess
    while True:
        try:
            guess = input('Guess a letter: ').lower()
            while True:
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
        except Exception as e:
            print('\nError! {e}! Please enter one letter from the alphabet a-z.\n')
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
        print(f"\nYou've already guessed the letter {guess}. Try again!\n")


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
            print(f"\nYou lost a life! Your guess is not in the secret word.\n")


# Start code used from other source (https://stackoverflow.com/questions/52910297/pydictionary-word-has-no-synonyms-in-the-api)
def synonyms(secret_word):
    '''
    Function looks up synonyms on thesaurus.com (web scrapes) and returns a list of synonym words
    '''
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(secret_word))
    soup = BeautifulSoup(response.text, 'html.parser')
    soup.find('section', {'class': 'css-191l5o0-ClassicContentCard e1qo4u830'})
    return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})] 
# End code used from other source


def give_player_hint(hint):
    '''
    Checks if player only has one life left.
    If so, Asks the player input('Would you like to get a hint? y/n: ').lower()
    Then handles answer error cases with a while loop and gives player feedback.
    If the player answers 'y', synonyms for the secret word will be displayed (web scraped from thesaurus.com).
    The player will be given feedback if no synonym is scraped:
    print('Sorry, there is no hint to display for this secret word.').
    The function returns variable hint = False 
    '''
    global lives
    if lives == 1:
        while hint:
            while True:
                try:
                    player_answer_hint = input('Would you like to get a hint? y/n: ').lower()
                    while True:
                        if player_answer_hint != 'y' and player_answer_hint != 'n':
                            print('\nError! Please answer with either the letter y (for yes) or n (for no).')
                            player_answer_hint = input('Would you like to get a hint? y/n: ').lower()
                        elif re.match('^\s*$', player_answer_hint):
                            print('\nError! Please answer with either the letter y (for yes) or n (for no).')
                            player_answer_hint = input('Would you like to get a hint? y/n: ').lower()
                        elif len(player_answer_hint) > 1:
                            print('\nError! Please answer with either the letter y (for yes) or n (for no).')
                            player_answer_hint = input('Would you like to get a hint? y/n: ').lower()
                        else:
                            break
                except Exception as e:
                    print(f'\nError! {e}! Please answer with either the letter y (for yes) or n (for no).')
                else:
                    break
            if player_answer_hint == 'y':
                synonyms_list = synonyms(secret_word)
                if synonyms_list == []:
                    print('Sorry, there is no hint to display for this secret word.')
                else:
                    print(f'Synonyms for the secret word are: {", ".join(list(set(synonyms_list[:4])))}')    
            hint = False
           
    return hint


hint = give_player_hint(hint)


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


def reveal_secret_word(guess):
    '''
    Checks if player's guess is not in the secret_word.
    If so, checks if game_over variable is equal to True.
    If so, the secret word is revealed to the player:
    print(f'The secret word is {secret_word}.\n')
    '''
    if guess not in secret_word:
        if game_over == True:
            print(f'The secret word is {secret_word}.\n')


def give_player_word_definition(guess):
    '''
    Checks if guess is not in the secret_word:
    If so, checks if game_over == True:
    If so, asks the player input(f'Would you like to see the definition for {secret_word}? y/n: ').lower()
    Then handles answer error cases with a while loop and gives player feedback.
    If the player answers 'y', the definition for the secret word will be displayed 
    (web scraped from thesaurus.com with use of PyDictionary module).
    The player will be given feedback if the scraped definition dictionary is empty:
    print(f'Sorry, there is no definition to display for {secret_word}.').
    '''
    if guess not in secret_word:
        if game_over == True:
            while True:
                try:
                    player_answer_definition = input(f'Would you like to see the definition for {secret_word}? y/n: ').lower()
                    while True:
                        if player_answer_definition != 'y' and player_answer_definition != 'n':
                            print('\nError! Please answer with either the letter y (for yes) or n (for no).')
                            player_answer_definition = input(f'Would you like to see the definition for {secret_word}? y/n: ').lower()
                        elif re.match('^\s*$', player_answer_definition):
                            print('\nError! Please answer with either the letter y (for yes) or n (for no).')
                            player_answer_definition = input(f'Would you like to see the definition for {secret_word}? y/n: ').lower()
                        elif len(player_answer_definition) > 1:
                            print('\nError! Please answer with either the letter y (for yes) or n (for no).')
                            player_answer_definition = input(f'Would you like to see the definition for {secret_word}? y/n: ').lower()
                        else:
                            break
                except Exception as e:
                    print(f'\nError! {e}! Please answer with either the letter y (for yes) or n (for no).')
                else:
                    break
            if player_answer_definition == 'y':
                print(f'Retrieving the definition for {secret_word}...')
                dictionary = PyDictionary()
                definition_dictionary = dictionary.meaning(secret_word)
                definition = '\n'.join(f'{key}: {value}' for key, value in definition_dictionary.items())
                if definition_dictionary == {}:
                    print(f'Sorry, there is no definition to display for {secret_word}.')
                else:
                    print(f'\n{definition}\n')


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
        print('\nCongratulations! You won.\n')


def display_letters_guessed(guess):
    '''
    Checks if guess is not in letters_guessed.
    If so, adds player's guess to letters_guessed list.
    Then Prints display Letters guessed: with guessed letters (all letters from letters_guessed list).
    '''
    if guess not in letters_guessed:
        letters_guessed.append(guess)
    print(f"Letters guessed: {', '.join(map(str, letters_guessed))}\n")


def play_hangman(word_length, hint):
    '''
    Creates a while loop for when variable game_over equals false.
    In the loop while not game_over:
    Calls functions: get_player_guess(), clear_screen(), display_hangman_logo('red', 'reset'),
    lose_life_incorrect_guess(guess), display_scoreboard(hi_score, update_current_score(word_length)),
    add_correct_guess_to_display(guess), display_stickman(lives), give_feedback_repeat_guess(guess)
    give_feedback_incorrect_guess(guess), check_lost_game(guess), check_won_game(),
    display_letters_guessed(guess), hint = give_player_hint(hint), give_feedback_lost_game(guess),
    reveal_secret_word(guess), give_player_word_definition(guess), give_feedback_won_game().
    When game_over is True (after exit while loop):
    Calls function: update_hi_score()
    '''
    global game_over
    hint = True

    while not game_over:
        get_player_guess()
        
        clear_screen()

        display_hangman_logo('red', 'reset')

        lose_life_incorrect_guess(guess)

        display_scoreboard(hi_score, update_current_score(word_length))

        add_correct_guess_to_display(guess)

        display_stickman(lives)

        give_feedback_repeat_guess(guess)

        give_feedback_incorrect_guess(guess)
        
        check_lost_game(guess)

        check_won_game()

        display_letters_guessed(guess)

        hint = give_player_hint(hint)

        give_feedback_lost_game(guess)

        reveal_secret_word(guess)

        give_player_word_definition(guess)

        give_feedback_won_game()
    
    update_hi_score()


play_hangman(word_length, hint)


def replay_hangman(word_length):
    '''
    Ask the player: input('Would you like to play again to increase your score? y/n: ').lower()
    Gives the player feedback if there is a player_answer_error
    While (loop) the player_answer is 'y':
    Resets global variables: current_score = 0, secret_word = None, secret_word_display = [],
    guess = None, letters_guessed = [], lives = 6, game_over = False
    Then the while loop calls the functions: clear_screen(), display_hangman_logo('red', 'reset'),
    display_scoreboard(update_hi_score(), current_score), word_length = get_player_word_length(), clear_screen(),
    display_hangman_logo('red', 'reset'), display_scoreboard(update_hi_score(), update_current_score(word_length)),
    create_secret_word(word_length), display_secret_word(), display_stickman(lives), play_hangman(word_length, hint)
    Then the while loop calls: player_answer = input('Would you like to play again to increase your high score? y/n: ').lower()
    '''
    global hi_score, current_score, secret_word, secret_word_display, guess, letters_guessed, lives, game_over
    
    player_answer = input('Would you like to play again to increase your score? y/n: ').lower()
    player_answer_error = True

    while player_answer_error:
        if player_answer != 'y' and player_answer != 'n':
            print('\nError! Please answer with either the letter y or n.\n')
            player_answer = input('Would you like to play again to increase your high score? y/n: ').lower()
        else:
            break

    while player_answer == 'y':
        current_score = 0
        secret_word = None
        secret_word_display = []
        guess = None
        letters_guessed = []
        lives = 6
        game_over = False
        
        clear_screen()

        display_hangman_logo('red', 'reset')
        
        display_scoreboard(update_hi_score(), current_score)

        word_length = get_player_word_length()
        
        clear_screen()

        display_hangman_logo('red', 'reset')
        
        display_scoreboard(update_hi_score(), update_current_score(word_length))

        create_secret_word(word_length)

        display_secret_word()

        display_stickman(lives)

        play_hangman(word_length, hint)

        player_answer = input('Would you like to play again to increase your high score? y/n: ').lower()


replay_hangman(word_length)