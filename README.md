# HANGMAN GAME

Hangman Game is a Python terminal game, which runs in a mock terminal on Heroku.

Users can test their knowledge of english vacabulary. The game will allow the user to choose the word length they would like to play. They have a choice from four to nine letters. The user gets six lives to try to guess the secret word. A scoreboard will be visible with the user's high score and current max score. The game will give the user the option to get a hint, the word synonyms, when only one life remains. If the user loses, the secret word will be revealed and the player can opt to get the word's definition. These extra features added to the classic game, gives the user an educative experience while playing this Hangman Game. The game also allows the user to replay the game to increase their high score, which adds a fun and competitive element as well.

![Responsive Mockup](assets/images/mockup.png)

[View the live version of the Hangman Game project here](https://hangman-game-ci.herokuapp.com/)

---

## How To Play

Hangman Game is based on the classic paper-and-pencil game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)). In this version: 

- At the start of every game the player gets to choose the word length: from 4 to 9 letters.
- A hi-score will be displayed, reflecting the highest score attained by the player. A current max score will be calculated, which is the highest  attainable score for the game with the chosen word length.
- The game starts with 6 lives and with every wrong letter guess the player will lose a life. Every new game will start with the current max score displayed which will decrease when the player loses a life.
- When there is only one life left, the player will have the option to get a hint.
- The player will win when having guessed all the word letters before losing all lives.
- The current max score remaining at the end of the game will be the final score for the game. If the game end score is higher than the displayed hi-score, the hi-score will be updated.
- If the player loses the game, the secret word will be revealed and the player will get the option to see the word's definition.
- At the end of every game the player will be given the option to replay the game to increase their hi-score or to exit the game. After the player exits the game, the game can be run again with the hi-score reset to zero.


## Project Goals

- To develop a fun educative python terminal game.
- To develop a terminal game with great user experience.
- To develop a game where the user can test their knowledge of english vocabulary.
- To develop a game where the user can broaden their english vocabulary knowledge.
- To develop a game where the user is challenged to keep improving while playing.


## UX - User Experience

### User Stories

- As a first-time user:
    - I want to be able to know which game I will be playing from the title logo.
    - I want to be able to have access to the instructions before starting the game.
- As a user:
    - I want to be able to choose from different word lengths before starting the game.
    - I want to visually be able to keep track of the game's score.
    - I want to have the opportunity to improve my score, by being able to replay the game.
    - I want to be able to choose different word lengths when replaying the game.
    - I want to have access to my hi-score. 
    - I want to be provided with a hint when I have have a hard time guessing the secret word.
    - I want to be able to improve my vocabulary knowledge, by having access to the word synonyms and definitions that I don't know.
    - I want to be able to exit the game to have a fresh start with the hi-score reset to zero. 


## Design

### Features

![Design Features](assets/images/design-features.png)

### Flowchart

![Design Features](assets/images/design-flowchart.png)


## Features

### Existing Features

- **Landing Page**

![Landing Page](assets/images/landing-page.png)

- **Landing Page Options**

![Landing Page Options](assets/images/landing-page-options.png)

- **Instructions**

![Instructions](assets/images/instructions.png)

- **Game Page**

![Game Page](assets/images/game-page.png)

- **Game Page Guess**

![Game Page Guess Feedback](assets/images/game-page-guess.png)

- **Game Page Life Feedback**

![Game Page Life Feedback](assets/images/game-page-life.png)

- **Game Page Hint Option**

![Game Page Hint Option](assets/images/game-page-hint.png)

- **Game Page Won Feedback**

![Game Page Won Feedback](assets/images/game-page-won.png)

- **Game Page Lost Feedback**

![Game Page Lost Feedback](assets/images/game-page-lost.png)

- **Game Page Definition Option**

![Game Page Definition Option](assets/images/game-page-definition.png)

- **Game Page Replay Option**

![Game Page Replay Option](assets/images/game-page-replay.png)

- **Game Replay Page**

![Game Replay Page](assets/images/game-replay-page.png)

- **Game Replay High Score**

![Game Replay High Score](assets/images/game-replay-hi-score.png)

- **Input validation and Error-checking**

![Game Validation and Error-checking](assets/images/game-error.png)

![Game Validation and Error-checking Code](assets/images/game-error-code.png)

### Future Features

- Allow the player to input their name to provide a more personalised gaming experience.
- Have a High Score for multiple players that is accessible even after resetting the game.
- Allow the player the option to write the word in one go, when the player guesses the word.


## Technology Used

### Languages

- [Python](https://www.python.org/)

### Frameworks, Libraries & Programs

- [Git](https://git-scm.com/):
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to Github.
- [Github](https://github.com/):
    - Github is used to store the project's code.
- [Diagrams.net](https://app.diagrams.net/):
    - Diagrams.net was used to create and store the features diagram and hangman flowchart.
- [Heroku](https://www.heroku.com/):
    - Heroku was used to deploy the live version of the terminal.


## Testing

I have manually tested this project by doing the following:

- I have passed the code through a Python autopep8 linter and confirmed there are no problems. 

![Testing Linter Install](assets/images/testing-linter-install.png)

![Testing Linter Command](assets/images/testing-linter-command.png)

- Given invalid inputs with all the game's input questions: strings when numbers are expected, numbers when strings are expected, out of bounds inputs, no input (enter key), empty space input, wrong number or letter inputs.

![Testing Input](assets/images/testing-input.png)

- Used a print statement in my local terminal to test if a different secret word is generated on every replay and if the secret word display functions correctly.

![Testing Print Statement](assets/images/testing-print-statement.png)

- Tested the word list in hangman_words.py: tested to make sure all words that I added to the word list got a synonym and definition returned when web scraped. Also implemented a feedback message in the case there is a change with the api and an empty list (synonym) or dictionary (definition) for a word gets returned in the future.

![Testing Empty List](assets/images/testing-empty-list.png)

![Testing Empty Dictionary](assets/images/testing-empty-dictionary.png)

- Tested in my local terminal and the Code Institute Heroku terminal.

### Bugs

#### Solved Bugs

- 

### Remaining Bugs

- No bugs remaining.

### Validator Testing

- PEP8
    - No errors were returned from passing my code through the Python autopep8 linter.


## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment:
    - Fork or clone this repository.
    - Log in Heroku.
    - Click 'New' and select 'Create new app'.
    - Choose a name for the app, region and click on 'Create app'.
    - In 'Settings' buildpacks need to be added. Set the buildpacks to Python and NodeJS in that order. They install future dependencies that are needed outside the requirements file.
    - In 'Deploy' section link the Heroku app to the repository by connecting it to github.
    - Enter the name of the repository you want to connect it with and click 'Connect'.
    - There is a option to either deploy using automatic deploys or manual deployment, which deploys the current state of the branch.
    - Click deploy branch.


## Credits

- Code Institute for the deployment terminal.
- [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)) for the details of the Hangman game. 
- [StackOverflow](https://stackoverflow.com/questions/52910297/pydictionary-word-has-no-synonyms-in-the-api) provided me a solution when the api requests send by PyDictionary didn't return any synonyms.


## Acknowledgements

- Thank you to my mentor Naoise Gaffney for giving me positive encouragement, guidance and support throughout the development process.
- Thank you to [Code Institute](https://codeinstitute.net/) for their information, guidance and support.
- Thank you to the Slack community for their support and information.