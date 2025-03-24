import random

# Global variables to track the game state:
game_status = True  # Flag indicating if the game is still running.
user_guesses = 7  # Number of guesses the player is allowed.
unsolved_word = ""  # The current visible state of the word (with underscores for unguessed letters).
chosen_word = ""  # The secret word chosen by the computer.


def welcome():
    # Displays a welcome message and explains the rules of the game.
    print("Welcome to Hangman!\n\n"
          "In this game, the computer will choose a word and you will try to guess it by suggesting letters,\n"
          "with each incorrect guess resulting in part of a stick figure being drawn until it's complete,\n"
          "or you guess the word correctly.\n")


def word_selection():
    # Chooses a random word from the pool and sets up the unsolved word with underscores.
    global unsolved_word
    global chosen_word
    word_pool = ["green", "amazing", "camp"]  # A list of possible words.
    chosen_word = random.choice(word_pool)  # Randomly select a word from the list.
    unsolved_word = "_" * len(chosen_word)  # Create an unsolved version with underscores.


def char_at_index(word, char):
    # Returns a list of indices where the given character appears in the word.
    indexes = []
    for i, letter in enumerate(word):
        if letter == char:
            indexes.append(i)
    return indexes


def user_guess():
    # Processes the player's guess: checks if the letter is in the word, updates the unsolved word,
    # and decrements the remaining guesses if the guess is wrong.
    global user_guesses
    global unsolved_word
    global chosen_word
    users_char_guess = input("Guess a letter: ")  # Prompt the user to enter a letter.

    if users_char_guess in chosen_word:
        # If the guessed letter is found in the secret word.
        char_in_word = char_at_index(chosen_word, users_char_guess)
        if len(char_in_word) > 1:
            print(f"There are {len(char_in_word)} {users_char_guess}'s in the word.\n")
            # For each occurrence of the letter, replace the corresponding underscore.
            for i in range(len(char_in_word)):
                unsolved_word = unsolved_word[:char_in_word[i]] + users_char_guess + unsolved_word[char_in_word[i] + 1:]
        else:
            print(f"There is {len(char_in_word)} {users_char_guess} in the word.\n")
            # Update the unsolved word at the first occurrence of the guessed letter.
            unsolved_word = unsolved_word[:chosen_word.index(users_char_guess)] + users_char_guess + unsolved_word[
                                                                                                     chosen_word.index(
                                                                                                         users_char_guess) + 1:]
    else:
        # If the guessed letter is not in the word, reduce the number of allowed guesses.
        print(f"Sorry, there is not a/an {users_char_guess} in the word.\n")
        user_guesses -= 1


def main():
    # The main function that controls the flow of the game.
    global game_status
    global chosen_word
    welcome()  # Print the welcome message and game instructions.
    word_selection()  # Select a word and prepare the unsolved word.

    while game_status:
        if user_guesses > 0:
            print(f"The word to solve is: {unsolved_word}")
            print(f"You have {user_guesses} guesses left.\n")
            if chosen_word != unsolved_word:
                # If the word has not been completely guessed, continue to ask for guesses.
                user_guess()
            else:
                # If the word is fully guessed, the player wins.
                print("The word was correct. You win!\n")
                game_status = False
        else:
            # If the player has no more guesses, they lose.
            print("Sorry, you have no more guesses left. You lose.\n")
            game_status = False

    print("Thank you for playing!")


# Start the Hangman game.
main()
