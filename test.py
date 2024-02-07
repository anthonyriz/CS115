def addTwoDigits(n):
    """
      Given a two-digit integer n, returns the sum of its digits  
    """
    return addTwoDigits(n // 10 + n % 10)

def largestNumber(n):
    return 10**n -1


def reverse(x):
    return x[::-1]

def mySum(l):
    """Assume l is a list of numbers; return the sum of list l"""
    if l == []:
        return 0
    else:
        return l[0] + mySum(l[1:])

def tribonacci(n):
    if n == 0:
        return 0
    elif n==1:
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

def gcd(x, y):
    """The gcd function returns the greatest common divisor of two numbers."""
    if x % y == 0:
        return y
    else:
        return gcd(x, x%y)

def pascal(n,r):
    if n==1:
        return 1
    elif r == n or r ==1:
        return 1
    else:
        return pascal(n - 1, r - 1) + pascal(n - 1, r)

print (pascal(4, 0))