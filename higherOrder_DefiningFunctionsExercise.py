from functools import reduce

def addTwoDigits(n):
    """
      Given a two-digit integer n, returns the sum of its digits  
    """
    return n // 10 + n % 10

def largestNumber(n):
    """ Given an integer n, return the largest number that contains exactly n digits. """
    return 10 ** n - 1
    #Alternate solution with string: return int('9' * n)

def reverse(l):
    """ Given a list l return the reverse of the list """
    return l[::-1]
    

def higherOrder(lst):
    """
        An higher order example function that finds
        if the multiplication of squares of a given list
        is divisible by 7.
    """
    newL = list(map(lambda x: x ** 2, lst))
    result = reduce(lambda x, y: x * y, newL)
    return list(filter(lambda x: x % 7 == 0, [result]))

if __name__ == "__main__":
    print("Higher Order Function Result: ", higherOrder([1,3,6]))
    print("The total of digits for 32: ", addTwoDigits(32))
    print("The largest number with 6 digits: ", largestNumber(6))
    print("Reverse of the list [1, 4, 7, 9] is: ", reverse([1, 4, 7, 9]))
    
