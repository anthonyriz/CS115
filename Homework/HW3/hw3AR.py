'''
Created on October 12, 2023
@author:   Anthony Rizzuto
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount, coins):
    '''
    This function takes two elements, amount and coins, where amount is an integer that represents
    the amount of change that a customer is to be given.

    Coins is represented as a list, which tells the program the values of the coins available.

    The program then finds the smallest number of coins needed to add up to "amount" only using the values 
    in "coins" list.

    Original Code:
    if amount == 0:
        return 0
    elif coins == [] or amount < 0:
        return float("inf")
    else:
        use_it = change(amount - coins[0], coins[0:]) + 1
        lose_it = change(amount, coins[1:])
    
    return min(use_it, lose_it)
    '''
    if amount == 0:
        return [0, []]
    elif coins == [] or amount < 0:
        return [float("inf"), []]
    else:
        use_it = giveChange(amount - coins[0], coins[0:])
        use_it[1].append(coins[0])
        use_it[0] += 1
        lose_it = giveChange(amount, coins[1:])
    return min(use_it, lose_it, key = lambda x: x[0])
    
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Used functions from HW2 below:

def letterScore (letter, scorelist):
  '''
  takes a str letter and returns the value associated with the letter (a number) from a provided
  scorelist (in this case ScrabbleScores)
  '''
  for i in scorelist:
    if i[0] == letter:
      return i[1]


def wordScore (S, scorelist):
  '''
  takes a string as an input and uses a provided scorelist (in this case scrabbleScores) to return the scrabble
  scoring of the string input 
  '''
  if len(S) ==0: 
    return 0

  for i in scorelist:
    if i[0] == S[0]:
     return i[1] + wordScore(S[1:], scorelist)

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    
    if dct == []:
        return []
    elif scores == []:
        return []
    else:
        return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if n == 0:
        return []
    elif L == []:
        return []
    else:
        return [L[0]] + take(n-1, L[1:])



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if n == 0:
        return L
    elif L == []:
        return []
    else:
        return drop(n-1, L[1:])




