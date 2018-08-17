import random

# the game in terminal 

def get_guess():
  secret_word= random.choice(["test","cat"])
  dashes = "-" * len(secret_word)
  guesses_left = 6
  previous_guesses = "Guessed:"
  
  while guesses_left > -1 and not dashes == secret_word:
    print(dashes)
    print (str(previous_guesses))
    hangman_graphic(guesses_left)
    guess = input("Guess:")
    print ("________      ")
    print ("********************************************")

    if len(guess) == 1 :
      previous_guesses= previous_guesses+guess+', '

    if len(guess) != 1:
      print ("Please enter a single letter")

    elif guess in secret_word:
      print ("Correct")
      dashes = update_dashes(secret_word, dashes, guess)

    else:
      print ("Wrong")
      guesses_left -= 1

  if guesses_left < 0:
    print ("You lose... The word was: " + str(secret_word))

  else:
    print ("You win! The word was: " + str(secret_word))


def hangman_graphic(guesses):
  if guesses == 6:
    print ("________      ")
    print ("|      |      ")
    print ("|             ")
    print ("|             ")
    print ("|             ")
    print ("|_________    ")
  elif guesses == 5:
    print ("________      ")
    print ("|      |      ")
    print ("|      0      ")
    print ("|             ")
    print ("|             ")
    print ("|_________    ")
  elif guesses == 4:
    print ("________      ")
    print ("|      |      ")
    print ("|      0      ")
    print ("|     /       ")
    print ("|             ")
    print ("|_________    ")
  elif guesses == 3:
    print ("________      ")
    print ("|      |      ")
    print ("|      0      ")
    print ("|     /|      ")
    print ("|             ")
    print ("|_________    ")
  elif guesses == 2:
    print ("________      ")
    print ("|      |      ")
    print ("|      0      ")
    print ("|     /|\     ")
    print ("|             ")
    print ("|_________    ")
  elif guesses == 1:
    print ("________      ")
    print ("|      |      ")
    print ("|      0      ")
    print ("|     /|\     ")
    print ("|     /       ")
    print ("|_________    ")
  else:
    print ("________      ")
    print ("|      |      ")
    print ("|      0      ")
    print ("|     /|\     ")
    print ("|     / \     ")
    print ("|_________    ")


def update_dashes(secret, cur_dash, rec_guess):
  result = ""

  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess

    else:
      result = result + cur_dash[i]

  return result

  

get_guess()