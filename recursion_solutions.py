def tribonacci(n):
    """Assume n is a positive integer; return the nth tribonacci number"""
    if n == 1 or n == 2: # first element of the series is counted as 1
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci(n - 1)  + tribonacci(n - 2) + tribonacci(n - 3)
def pascal(n,r):
    """assume n and r are two positive integers
       return the rth element of the nth row of Pascal's Triangle"""
    if n == 1:
        return 1
    elif r == 1 or r == n:
        return 1
    else:
        return pascal(n - 1, r-1) + pascal(n - 1, r)

def mySum(l):
    """Assume l is a list of numbers; return the sum of list l"""
    if l == []:
        return 0
    else:
        return l[0]+mySum(l[1:])

def reverseString(string):
    """Takes a string and returns the string in reverse order"""
    if string == "": #or len(string) == 0
        return ""       
    else:
        return reverseString(string[1:]) + string[0]
        #alternate solution string[-1] + reverseString(string[:-1])

# The gcd function returns the greatest common divisor of two numbers.
def gcd(x, y):
    """The gcd function returns the greatest common divisor of two numbers.
        Assume x > y
    """
    if x % y == 0:
        return y
    else:
        return gcd(x, x%y)





