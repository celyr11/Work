#Hangman game
#Used a little help with this video: https://www.youtube.com/watch?v=kbTBgpOtlG0

import random
print("Welcome to Hangman!")
word_bank = ["cely", "laura", "colores", "volleyball", "harleyquinn", "michael", "jailen", "checo", "celular", "Electroencefalografista"]

random_word = random.choice(word_bank)
word_length = len(random_word)
lives = 6
guessed_letters = []

while lives > 0:
    display_word = ""
    for letter in random_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)

    if display_word.replace(" ", "") == random_word:
        print("Congratulations! You guessed the word:", random_word)
        break

    chosen_action = input("Type 'exit' if you want to leave the game, if not write ok: ").lower()
    if chosen_action == 'exit':
        print("Play again later if you want :)")
        exit()

    chosen_letter = input("Choose a letter: ").lower()

    if chosen_letter in guessed_letters:
        print("You've already guessed that letter!")
        continue

    guessed_letters.append(chosen_letter)

    if chosen_letter not in random_word:
        lives -= 1
        print("Incorrect! You have", lives, "lives left.")
    else:
        print("Correct!")

    try:
        if chosen_letter not in word_bank:
            raise ValueError("That letter is not in the word bank")
    except ValueError as a:
        print("Error:", a)
        print("Try again!")

if lives == 0:
    print("You have no more lives. The word was:", random_word)

