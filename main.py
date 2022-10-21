from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position 
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]
    secret = actual
    

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if(letter in secret):

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == secret[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:

        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True)

    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      printColorfulLetter(letter, False)
      

    print(Style.RESET_ALL + " ", end="")


def getSixLetterInput():
  #Word variable set as empty
  word = ""

  #Check if the word is six letters, re-prompt for word until length is 6
  while(not len(word) == 6):
    word = input("Enter a six letter word: ")

  #Return the user's input
  return word.lower()

### Main Program ###
  
#Main variables:
#Set the secret word
secretWord = "trains"
#Set the guess counter
guessCount = 0
#Set the current guess
userGuess = ""

#Welcome Text
print(r"""
          _______  _______  ______     _______  _        _______          
|\     /|(  ___  )(  ____ )(  __  \   (  ____ )( \      (  ___  )|\     /|
| )   ( || (   ) || (    )|| (  \  )  | (    )|| (      | (   ) |( \   / )
| | _ | || |   | || (____)|| |   ) |  | (____)|| |      | (___) | \ (_) / 
| |( )| || |   | ||     __)| |   | |  |  _____)| |      |  ___  |  \   /  
| || || || |   | || (\ (   | |   ) |  | (      | |      | (   ) |   ) (   
| () () || (___) || ) \ \__| (__/  )  | )      | (____/\| )   ( |   | |   
(_______)(_______)|/   \__/(______/   |/       (_______/|/     \|   \_/   
                                                                         
""")

#Instructions
print("Welocme to Word Play")
print("================")
print("You have five tries to get the word correct")
print("The word is SIX CHARACTERS long, and you must enter a guess of this length")
print("If a letter is in the correct place, it will be GREEN")
print("If a letter is in the word, but not in the correct place, it will be YELLOW")
print("If the letter is NOT in the word, it will be RED")
print()

#Guess loop
while(guessCount <5 and userGuess !=secretWord):
  #Prompt user for their guess
  userGuess = getSixLetterInput()
  #Check guess accuracy and display for user color-coated, then add a line
  print(f"Attempt {guessCount +1}:")
  printGuessAccuracy(userGuess, secretWord)
  print()
  #Increase count by 1
  guessCount += 1

#Check if user won
if(userGuess == secretWord and guessCount < 5):
  print("You win!")
  
else:
  print("Better luck next time!")