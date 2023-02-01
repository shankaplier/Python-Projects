# imports a module that gives a list of english words
from english_words import get_english_words_set
# importing random module to generate a random
import random
# this statement generates a set of random english words
setOfWords = get_english_words_set(["gcide"], alpha=True, lower=True)
#Global variable blank that shows the player the blanks
global blank
blank = []
#Global variable word that keeps track fo the selected word
global word
word = None
#variable to keep track of how many lives the player has left
global lives
lives = 5

# Generates a word as well as the blanks for the word
def generateword():
    global word
    global blank
    #Generates a random word from the set with all lower case letters if a word isn't generated already
    if blank == []:
      word = random.choice(tuple(setOfWords)).lower()
    #Generates blanks corresponding to every letter in the selected word
    if blank == []:
      for i in range(len(word)):
        blank.append("_")

#Function that check whether a word is in the blank or not and remove a blank if it is
def checkWord(letter):
 global lives
 global word
 global blank
 #Returns a list of positions at which a particular character is in the wordquit
 indexes = [pos for pos, char in enumerate(word) if char == letter]
 #Checks whether the letter guessed is wrong and displays a message
 if indexes == []:
   lives -= 1
   if lives != 0:
    print(f"\nWrong choice please try again, you have {lives} more lives\n")
 #If the player chose the right character it will remove the blanks
 else:
   for pos in indexes:
     blank[pos] = word[pos]

#Function that shows Hangman depending on the amount of lives left
def displayMenu(lives):
  global blank
  if lives == 5:
    print("  +---+")
    print("      |")
    print("      |")
    print("      |")
    print("      |")
    print("      |")
    print("=========")
  elif lives == 4:
    print("  +---+")
    print("  |   |")
    print("  0   |")
    print("      |")
    print("      |")
    print("      |")
    print("=========")
  elif lives == 3:
    print("  +---+")
    print("  |   |")
    print("\ 0   |")
    print("  |   |")
    print("      |")
    print("      |")
    print("=========")
  elif lives == 2:
    print("  +---+")
    print("  |   |")
    print("\ 0 / |")
    print("  |   |")
    print("      |")
    print("      |")
    print("=========")
  elif lives == 1:
    print("  +---+")
    print("  |   |")
    print("\ 0 / |")
    print("  |   |")
    print(" /    |")
    print("      |")
    print("=========")
  elif lives == 0:
    print("  +---+")
    print("  |   |")
    print("\ 0 / |")
    print("  |   |")
    print(" / \  |")
    print("      |")
    print("=========")


#While loop to keep the game running unless the plays inputs quit
while lives > 0:
  generateword()

  #Check to see whether the player has guessed all the blanks
  if "_" in blank:
    displayMenu(lives)
    #Prints the blanks for the player to guess the words
    print(' '.join(blank))
    #Prompts the player to enter a letter he thinks exists in the blank
    guess = input("\nPlease enter a letter of your choice: ")

    #Checks if the player wants to quit the game
    if guess == "quit":
      break
    #Checks if the guessed letter has already been guessed
    elif guess in blank:
      lives -= 1
      print(f"You have already guessed this character. Please try again, you have {lives} more lives")
    #Checks if the player entered only one letter and not any other invalid inputs
    elif len(guess) == 1 and type(guess) == type("s"):
      #Checks whether the letter is in the word 
      checkWord(guess)
  else:
    print("\nCongrats you won!")
    print(f"\nThe word was: {word}")
    break
else:
  displayMenu(lives)
  print("\nYou lost!")
  print(f"\nThe word was: {word}")
  