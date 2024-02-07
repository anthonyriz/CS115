for i in range (10, 0, -3): #10, 7, 4, 1
    j = 4
    total = 0
    while j < i: # 4 < 4
        j += 1 # 7
        total += j # 5 + 6 + 7
    print (i, j, total) #Assume we print i, j and total here

'''
i j total
---------------
NA NA NA
10 10 45
7  7  18
4  4  0
1  4  0
'''