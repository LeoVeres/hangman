def Hangman(guess, word, dashes, guessleft):
    guesses_left = guessleft
    newdashes = dashes
    if guess in word:
      newdashes = update_dashes(word, dashes, guess)
    else:
      guesses_left -= 1
    return newdashes, guesses_left
    


def update_dashes(secret, cur_dash, rec_guess):
  result = ""

  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess

    else:
      result = result + cur_dash[i]

  return result