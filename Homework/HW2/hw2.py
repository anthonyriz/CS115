'''
Created on 10/3/23
@author:   Anthony Rizzuto
Pledge:   I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 2
'''
from re import split
import sys
from functools import reduce
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

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
     

def scoreList(Rack):
  '''
  takes a list of lowercase letters (or a Rack) and returns all the possible words that can be made
  with these letters.
  It uses the global dictionary provided (Dictionary)
  '''
  words = filter(lambda x: all(x.count(letter) <= Rack.count(letter) for letter in x), Dictionary) #filters out all words in x and checks if they can be made from Rack
  return [[x, wordScore(x, scrabbleScores)] for x in words]

def bestWord (Rack):
  '''
  uses a Rack of letters and scoring of each letter and returns the highest-scoring word possible 
  using the input letters along with its score
  '''
  if not scoreList(Rack):
    return ['', 0]
  
  return reduce(lambda x, y: x if x[1] >= y[1] else y, scoreList(Rack)) 


print(scoreList(["a", "s", "m", "t", "p"]))


