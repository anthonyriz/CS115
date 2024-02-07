############################################################
# Name:Anthony Rizzuto
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. Anthony Rizzuto
# CS115 Lab 1
#  
############################################################

def same(word):
  lowerWord = word.casefold()
  length = len(lowerWord)
  if (lowerWord[0] == lowerWord[length-1]):
    return True
  else:
    return False

def consecutiveSum(x, y):
  sum = ((x+y)/2)*(y-x-1)
  return sum



