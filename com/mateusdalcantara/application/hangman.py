from com.mateusdalcantara.application.resources.hangman_stages_and_logo import stages, logo
from com.mateusdalcantara.application.resources.hangman_words import word_list
import random

"""
Hangman Game: A Python-based version of the classic Hangman game.

This script allows the user to play a simple version of Hangman. The program randomly selects a word from a predefined 
list, and the user must guess letters in order to reveal the word. 
The game continues until the user either guesses the word correctly or loses all their lives.

Modules:
- `stages` and `logo` from `hangman_stages_and_logo`: Provides ASCII art for the stages of the hangman drawing and the game logo.
- `word_list` from `hangman_words`: A predefined list of words that the game can choose from.
- `random`: Used to randomly select a word from the word list.

Global variables:
- `lives`: The number of lives the player has (default: 6).
- `chosen_word`: The word randomly selected from the word list.
- `placeholder`: A string of underscores representing the word to guess.
- `correct_letters`: A list of letters that the player has correctly guessed.

Game Flow:
1. The game starts by displaying the game logo and randomly selecting a word.
2. A placeholder string of underscores representing the word is shown.
3. The player is asked to guess a letter.
4. The game checks if the letter has been guessed before and ensures the guessed letter is part of the word.
5. If the guessed letter is correct, it is revealed in the word; if it's wrong, the player loses one life.
6. The game continues until the player either guesses the word or loses all lives.
7. At the end of the game, the hangman stage is displayed based on the number of remaining lives.

Example usage:
- The player is prompted to guess letters.
- When the incorrect guess are typed the image of hangman change to worse.
- When all the letters are guessed correctly or the player loses all lives, the game ends.
- The game updates the word with correct guesses and reduces lives on incorrect guesses.



"""

lives = 6

# Display the game logo
print(logo)

# Randomly choose a word from the word list
chosen_word = random.choice(word_list)
print(chosen_word)

# Create a placeholder string with underscores representing the word to guess
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: "+placeholder)

game_over = False
correct_letters = []

while not game_over:

    # Display remaining lives
    print(f" *******<{lives}>/6 LIVES LEFT*******")

    # Prompt the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in correct_letters:
        print("You've already guessed {}".format(guess))

    display = ""

    # Update the display based on the guessed letter
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess:" + display)

    # Handle incorrect guesses
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. you lose a life.")
        if lives == 0:
            game_over = True
            print("You lose.")

    # Check if the player has guessed all the letters
    if "_" not in display:
        game_over = True
        print("You win.")

    # Display the hangman stage based on the remaining lives
    print(stages[lives])