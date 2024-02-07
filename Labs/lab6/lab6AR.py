'''
Created on 10-18-23
@author:   Anthony Rizzuto
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 != 0:
        return True
    else:
        return False
    
    #The largest power of 2 that occurs in 42 is 2^5 = 32. Then 42-32 = 10. The largest power of 2 that 
    # occrus in 10 is 2^3 = 8. 10-8 = 2. The largest power of 2 that occurs in 2 is 2^1 = 2. 2-2 = 0. 
    # Answer: 
    #_1_ _0_ _1_ _0_ _1_ _0_
    #2^5 2^4 2^3 2^2 2^1 2^0

'''

In base-2 representation, if you are given an odd base-10 number, the least-significant bit will be 1
as by definition, an odd number is a number that equals twice some number plus 1. Anything to the zero power equals 1, and 
there will always be a remainder of one after 2^1 = 2.

If you are given an even base-10 number, the least-significant bit - the rightmost bit - in its base-2 representation will be
0; by definition an even number is twice some number

'''

'''

If we have a base-2 number and we eliminate the least-significant bit, this takes the value of the original number and halves it.
base-2 1010 = 10... base-2 101 = 5. Same with base-2 1011 = 11... base-2 101 = 5 and 11/2 = 5 (in Python's oridinary
integer division)

We have a number N written in base 10 (decimal) and we let Y denote N/2, where we
round down if N is odd (this is Python's ordinary integer division). If we already had the base-2
representation of Y, perhaps from recursion, this would allow us to easily find the base-2
representation of N by adding a 0 as the least-signifcant bit of Y, assuming N is even. If N is odd, then we
add a 1 as the least-significant bit of Y, as this adds 1 to N. As stated above, if you remove the least-significant bit of a base-2 number, it halves
the base-10 of that number. So if you add a least-significant bit, it doubles the base-10 of that number. 

'''
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n <= 0:
        return '' #changed from 0 in case error persists
    else:
        return numToBinary(n//2) + str(n % 2) 
            
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[-1] == 0:
        return binaryToNum(s[:-1])
    else:
        return binaryToNum(s[:-1]) * 2 + int(s[-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    
    if len(s)!= 8:
        return ''
    else:
        answer = str((len(s) - len(numToBinary(binaryToNum(s) + 1))) * '0') + numToBinary(binaryToNum(s) + 1)
        if len(answer) >8:
            return answer[1:]
        else:
            return answer

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    
    if len(s) != 8:
        return ''
    elif n >= 0:
        print(s)
        return count(increment(s), n - 1)
    else:
        return     

'''
The ternary representation for the value 59 is below:

_2_ _0_ _1_ _2_
3^3 3^2 3^1 3^0

3^2 = 27 --> 27*2 = 54 --> 59-54 = 5 --> 3^2 = 9 --> 9>5 --> 3^2 = 0 --> 3^1 = 3 --> 5-3 = 2 --> 3^0 = 1 --> 1*2 = 2 --> 2-2 = 0
'''
def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
   
    if n <= 0:
        return '' #changed from 0 in case error persists
    else:
        return numToTernary(n//3) + str(n % 3) 

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
         return ternaryToNum(s[:-1]) * 3 + int(s[-1])
        
