############################################################
# Name: Anthony Rizzuto
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. Anthony Rizzuto
# CS115 HW 1
#
###########################################################


from functools import reduce

def mult (x,y):     #function multiplies 2 values 
    return x*y

def factorial (n):      #function stores all integers from 1 to n (the number provided by the user), 
                        #then multiplies these numbers together
    numbers = map(int, range (1, n+1))
    fact = reduce (mult, numbers)
    return fact

def add (x,y):      #function adds two values together
    return x+y

def mean(L):        #function uses reduce to reduce all elements in the provided list to one number by adding them together
                    #It then divides this number by the length of the list, or the number of elements added together
    sum = reduce(add, L)
    return sum/(len(L))
