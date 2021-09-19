# Hangman Game
The goal of this challenge is create the game Hangman where the user have to guess the hidden word before his run out of the life


# Breakdown project

1) Generate a random word taken from a list of words.

2)Generate as many blanks as letter in the word to show the user how many letters they need to guess.
  >ex. for the word "dog" generate "---". 
  
3)Ask user to guess a letter.

4)Check if the guessed letter is in the word.
  
5)if the guessed letter in the word replace the blank with the letter.
  > Check if all the blanks are filled. ex word "dog" guess letter "o" replace "_o_"
  >> if yes end the game 
  >> if no go back at point 1.
  
6)If the guessed letter is not in the word lose a life.
  > check if the user run out of lifes.
  >> If yes end the game 
  >> If no go back at point 1.
  
 

