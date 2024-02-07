#Example 1a
L = ["eve", "alice", "bob"]

M = L

L[1] = "mary"

print (M[1])

#Example 1b
L = ["eve", "alice", "bob"]

M = list(L)

L[1] = "mary"

print (M[1])

#Example 1c

L = [[1,2], [3,4]]

M  = list(L)

L[0][1] = 5

M[0] = [6,7]

print(L,M)

#Example 1d
L = [[1,1], [2,2]]

M = list(L)

M.append([5,5])

print (L,M)

#Example 

'''L = [[1,1], [2,2]]

M = [L[1], list(L[0])]

M[0].append([5,5])

print(L, M)'''