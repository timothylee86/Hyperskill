import random
import string

def getOption():
    option = ""
    while (option not in ['play', 'exit']):
        option = input('Type "play" to play the game, "exit" to quit: ')
    return option




print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']

while (getOption() == "play"):
    print("")
    answer = random.choice(word_list)
    word = '-' * len(answer)
    letters = set(answer)
    guessed_letters = set()
    attempts_remaining = 8

    while attempts_remaining > 0:

        print("\n" + word)

        if word == answer:
            print("You guessed the word!\nYou survived!")
            break

        guess = input("Input a letter: ")

        # Error checking
        if len(guess) != 1:
            print("You should input a single letter")
            continue
        elif (not set(guess).issubset(string.ascii_lowercase)):
            print("It is not an ASCII lowercase letter")
            continue

        # Process the user input
        if guess in guessed_letters:  # Already guessed the letter
            print("You already typed this letter")
        elif guess not in answer:  # Guessed wrong letter
            print("No such letter in the word")
            attempts_remaining -= 1
            guessed_letters.add(guess)
        elif guess in letters and guess not in guessed_letters:  # Correct letter (not already guessed)
            guessed_letters.add(guess)
        else:  # Correct letter (already guessed)
            print("No improvements")
            attempts_remaining -= 1

        word = "".join(x if x in guessed_letters else '-' for x in answer)

    else:
        print("You are hanged!")


