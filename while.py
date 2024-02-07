def reverseString(string):
    revString = ''
    i = -1
    while i + 1 > (0 - len(string)):
        revString = revString + string[i] 
        i -=1
    return revString

