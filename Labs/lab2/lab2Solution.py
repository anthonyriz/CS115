############################################################
# Name: Anthony Rizzuto
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. Anthony Rizzuto
# CS115 Lab 2
#
###########################################################

def dot(L,K):   #function returns the dot product of 2 lists
    if not L or not K:  #if one or both of the lists are empty, 0 is returned
        return 0
    x = L[0] * K[0]         #the first elements in each lists are multiplied together, then recursion
                            #is used for every next element in each list and is added to the previous sums 
    return x + dot(L[1:],K[1:])

def explode(s):     #function explodes a string (s) into a list of characters
    if not s:       #if the string is empty, returns a blank list
        return []
    else:       
        return [s[0]] + explode(s[1:])      #returns a list (given by []) and recursion is used for every next character

def ind(e, L):      #function indexes the first occurance of element e in provided list L
    if not L:           #if e is not found in list L, the length of L is returned
        return len(L)       
    elif e == L[0]:     #if e is the first element in the list, 0 is returned (as 0 represents first element in a list)
        return 0
    else:
        index = ind(e, L[1:])   #if e is not the first element in the list, then recursion is used to go through the list until e is found

        return index + 1    #every time the function is called again, the integer index adds 1 to keep track of the index of e in list L 

def removeAll(e, L):        #function removes element e out of list L
    if not L: 
        return []         #if element e is not in L, returns empty 
    elif e == L[0]: 
        return removeAll(e, L[1:])  #if element e is the 'first' element in list L, 
                                    #it will skip over it and call the function again starting with the second element
    else: 
        return [L[0]] + removeAll(e, L[1:])    #once the first element is not e, the new list will be returned, starting with the new first
                                                # and this function will run over and over 

def myFilter(f, L):     #function that filters out a list based on predicate function provided (f)
    if not L:          
        return []
    elif f(L[0]):       #says if the predicate function is True
        return [L[0]] + myFilter(f, L[1:])      
    else:                  #if the predicate function is False
        return myFilter(f, L[1:])

def deepReverse(L):     #function reverses a list L
    if not L:
        return []

    elif isinstance(L[0], list):        #If true
        reversedList = deepReverse(L[0])
    else:       #If false
        reversedList = L[0]     #new list named reversedList is created starting at beginning of List
    
    return deepReverse(L[1:]) + [reversedList]  #the function is called again for every index and is added to the reversedList, in the reversed order


        



    







