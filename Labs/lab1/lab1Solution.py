############################################################
# Name: Anthony Rizzuto
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. Anthony Rizzuto
# CS115 Lab 1
#
###########################################################

from math import factorial
from functools import reduce


def inverse(x):
    x = float(x)  # converts int to float
    return 1/x  # function returns 1 divided by the integer (now float) provided by user


def e(n):
    factorials = map(factorial, range(1, n+1))  # variable 'factorials' stores each factorial value from the 
                                                #range 1 to the integer (n+1) because range does not include endpoint
    
    reciprocal = map(inverse, factorials)   #variable 'reciprocal' stores each factorial value and holds the reciprocal of them
    
    return reduce(add, reciprocal) + 1  #adds up each reciprocal || 1/1! + 1/2! ... 1/n! || and adds 1 to this value

def add(a, b):      #simple function to add two elements together
    return a + b
