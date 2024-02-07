#memoization

#step 1: memo = {}

memo = {} #step 1
def LCS(s1, s2):
    #step 2: check if it is in dictionary
    #if (s1,s2) in memo:
    #   return memo[(s1,s2)]

    result = 0 #step 3

    if (s1, s2) in memo:    #step 2
        return memo[(s1,s2)]

    #step 3: initialize result = 0
    elif s1 == '' or s2 == '':
        result = 0
    elif s1[0] == s2[0]:
        result = 1 + LCS(s1[1:], s2[1:])
    else:
        chopS1 = LCS(s1[1:], s2)
        chopS2 = LCS(s1, s2[1:])
        result = max (chopS1, chopS2)

    #step 3 cont.
    memo[(s1, s2)] = result 
    return result

#tail recursion

L = [3, 5, 8, 6]
#write a function that will find sum of squares in given list, L
#returns 3^2 + 5^2 + 8^2 + 6^2

def sumSq(L, total = 0 ):     #tail recursion needs an intermediate variable (total) to hold the previous value
    if L == []:
        return total
    else:
        return sumSq(L[1:], total + L[0]**2) #tail recurisve because there are no calculations doen in the traceback
                                            # all calculations are done in function call