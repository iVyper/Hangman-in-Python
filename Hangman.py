import random

game_status = True
user_guesses = 7
unsolved_word = ""
chosen_word = ""

def welcome():
    print("Welcome to Hangman!\n\n"
          "In this game, the computer will choose a word and you will try to guess it by suggesting letters,\n"
          "with each incorrect guess resulting in part of a stick figure being drawn until it's complete,\n"
          "or you guess the word correctly.\n")

def word_selection():
    global unsolved_word
    global chosen_word
    word_pool = ["green", "amazing", "camp"]
    chosen_word = random.choice(word_pool)
    unsolved_word = "_" * len(chosen_word)

def char_at_index(word, char):
    indexes = []
    for i, letter in enumerate(word):
        if letter == char:
            indexes.append(i)
    return indexes

def user_guess():
    global user_guesses
    global unsolved_word
    global chosen_word
    users_char_guess = input("Guess a letter: ")
    if users_char_guess in chosen_word:
        char_in_word = char_at_index(chosen_word, users_char_guess)
        if len(char_in_word) > 1:
            print(f"There are {len(char_in_word)} {users_char_guess}'s in the word.\n")
            for i in range(len(char_in_word)):
                unsolved_word = unsolved_word[:char_in_word[i]] + users_char_guess + unsolved_word[char_in_word[i]+1:]
        else:
            print(f"There is {len(char_in_word)} {users_char_guess} in the word.\n")
            unsolved_word = unsolved_word[:chosen_word.index(users_char_guess)] + users_char_guess + unsolved_word[chosen_word.index(users_char_guess) + 1:]
    else:
        print(f"Sorry, there is not a/an {users_char_guess} in the word.\n")
        user_guesses -= 1


def main():
    global game_status
    global chosen_word
    welcome()
    word_selection()

    while game_status:
        if user_guesses > 0:
            print(f"The word to solve is: {unsolved_word}")
            print(f"You have {user_guesses} guesses left.\n")
            if chosen_word != unsolved_word:
                user_guess()
            else:
                print("The word was correct. You win!\n")
                game_status = False
        else:
            print("Sorry, you have no more guesses left. You lose.\n")
            game_status = False

    print("Thank you for playing!")
main()