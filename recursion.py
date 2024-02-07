#exercise 1

def mySum (L):
    if not L:
        return 0
    else:
        return L[0] + mySum(L[1:])

#exercise 2

def reverseString(s):
    if not s:       #if the string is empty, returns a blank list
        return ""

    else:
        return s[-1] + reverseString(s[:-1]) 

print(reverseString("friends"))