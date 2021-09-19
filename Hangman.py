from hangman_art import stages, logo

from hangman_word import word_list
import random

chosen_word = random.choice(word_list)

print(chosen_word)
count_letter = len(chosen_word)
lives = 6
double = ""
# list for check if the user already input the letter
double_word = []
# Create a list and add "_" for the length of the word
display = []
print(logo)
for i in chosen_word:
    display.append("_")

print(display)

game_over = False

while not game_over:
    guess = input("Guess a letter:\n ").lower()
    double = guess
    if double in double_word:
        print("word already chosen\n")
        guess = input("Guess a letter:\n ").lower()
    # loop with the lenght of choose word is the guess is right add the letter to the position on list display

    for count in range(count_letter):
        letter = chosen_word[count]
        if letter == guess:
            display[count] = letter
            double = display[count]
    print(display)
    # if player choose the wrong letter take of 1 life
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not present in the word")

        if lives == 0:
            game_over = True
            print(f"The word was {chosen_word}. You end your lives. Game over!\n")
        # if no more blanck space remains end loop and win the game
    if not "_" in display:
        game_over = True
        print(f"The word was {chosen_word} you win!\n")
    double_word += [guess]

    print(stages[lives])