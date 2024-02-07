'''
Created on November 5th, 2023
@author:   Anthony Rizzuto
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.
    
    Pasted from lab 6
    '''
    if n <= 0:
        return '' #changed from 0 in case error persists
    else:
        return numToBinary(n//2) + str(n % 2) 
            
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.

    Pasted from lab 6
    '''
    if s == '':
        return 0
    elif s[-1] == 0:
        return binaryToNum(s[:-1])
    else:
        return binaryToNum(s[:-1]) * 2 + int(s[-1])

def increment(s):
    '''Precondition: s is a string of COMPRESSED_BLOCK_SIZE bits.
    Returns the binary representation of binaryToNum(s) + 1.
    
    Pasted from lab6 and modified to work here
    '''
    
    if len(s)!= COMPRESSED_BLOCK_SIZE:
        return ''
    else:
        answer = str((len(s) - len(numToBinary(binaryToNum(s) + 1))) * '0') + numToBinary(binaryToNum(s) + 1)
        if len(answer) > COMPRESSED_BLOCK_SIZE:
            return answer[1:]
        else:
            return answer

def compress(S):
    '''
    Takes a binary string S of length 64 as input and returns another binary string as output. 
    The output binary string is a run-length encoding of the input string.
    '''

    def helper(S, currentBit, length):
        '''
        helper function that compresses the given string S in compress(S) into the run-length encoding.
        currentBit represents 0 or 1
        '''
       
        if not S: #base case
            return length

        elif length == "1" * COMPRESSED_BLOCK_SIZE: 
            return length + helper(S, 1 - currentBit, "0" * COMPRESSED_BLOCK_SIZE)
            
        elif int(S[0]) != int(currentBit):
            return length + helper(S, 1 - currentBit, "0" * COMPRESSED_BLOCK_SIZE)

        else:
            return helper(S[1:], currentBit, increment(length))

    return helper(S, 0, "0" * COMPRESSED_BLOCK_SIZE)

def uncompress(C):
    '''
    Inverts" or "undoes" the compressing in the compress function. 
    That is, uncompress(compress(S)) should give back S
    '''
    def helper(C, currentBit):
        '''
        helper function that decompresses the compressed string S
        '''
        if C == "": 
            return ""

        else: 
            return binaryToNum(C[:COMPRESSED_BLOCK_SIZE]) * str(int(currentBit)) + helper(C[COMPRESSED_BLOCK_SIZE:], 1 - currentBit)
    
    return helper(C, 0)

#The largest number of bits that the compress algorithm could possibly use to encode a 64-bit string/image
#is 320 bits. If the string provided was to alternate between 0 and 1 every time, the run-length encoding would have to be 
# represented in 5 bits for every 0 and 1, so 32 zeros and 32 ones multiplied by 5 bits each is 320 bits

def compression(S):
    ''' Return the ratio of the compressed size to the original size for image S.'''
    return len(compress(S)) /len(S)

#TESTS:

#Penguin
def test_penguin(penguin):
    '''test case for penguin image'''
    print ('\nPenguin: '+ penguin)
    print('Penguin compressed: ' + compress(penguin))
    print('Penguin Compression: ' + str(compression(penguin)))

#Smile
def test_smile(smile):
    '''test case for smile image'''
    print ('\nSmile: '+ smile)
    print('Smile compressed: ' + compress(smile))
    print('Smile Compression: ' + str(compression(smile)))

#Five
def test_five(five):
    '''test case for five image'''
    print ('\nFive: '+ five)
    print('Five compressed: ' + compress(five))
    print('Five Compression: ' + str(compression(five)))


penguin =  "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
smile = "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
five = "1"* 9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"

test_penguin(penguin)
test_smile(smile)
test_five(five)


#The tests I conducted takes simple images in binary strings of length 64 and runs the compress(s), uncompress(C),
#and compression(S) functions to obtain the run-length encoding, decompressed (or original string), 
#and ratio of compressed size to original size respectfully. 


#This algorithim, Laicompress(S) is impossible because if you take a 64 bit string and compress it into a
#shorter string, some bits will not be accounted for due to not enough size, and this is a major problem
#because first, there could be more than one image with the same short bit string and second, there could be
# different arrangements of these bits inlcluding the bits that could not fit in the string length




