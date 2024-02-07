i = 4
j = 16
p = []

while i < j:    
    i +=1
    total = 0
    for k in range(8, j, 2): 
        total += k 
    p.append(total)
    j -=2
    print (i, j, p) # Assume a print here that prints i j and p

'''
i j p
--------
4 16 []
5 14 [44]
6 12 [44, 30]
7 10 [44, 30, 18]
8 8 [44, 30, 18, 8]

'''