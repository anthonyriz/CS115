#
# life.py - Game of Life lab
#
# Name: Anthony Rizzuto
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [[0]* width] # What do you need to add a whole row here?
    return A

def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    """returns a 2d array of all live cells - with the value of 1 - except for 
    a one-cell-wide border of empty cells (with the value of 0) around the edge of the 2d array.
    """

    A = createBoard(w, h )

    for row in range(h-1):
        for col in range(w-2):
            if row == col+1 or row: #??
                A[row][col+1] = 1
            else:
                A[row][col] = 0
    return A

def randomCells(w,h):
    """returns an array of randomly-assigned 1's and 0's except that the outer edge of 
    the array is still completely empty (all 0's) 
    """
    A = createBoard(w, h )

    for row in range(h-1):
        for col in range(w-2):
            if row == col+1 or row: 
                A[row][col+1] = random.choice([0,1])
            else:
                A[row][col] = 0
    return A

def copy( A ):
    """makes a deep copy of the 2d array A. Takes in a 2d array A and outputs 
    a new 2d array of data that has the same pattern as the input array
    """
    newA = []
    
    for row in A:
        newRow = []
        for i in row:
            newRow.append(i)
        newA.append(newRow)
    return newA

def innerReverse( A ):
    """takes an old 2d array (or "generation") and then
    creates a new generation of the same shape and size 
    """
    for row in range(1, len(A)-1):
        for col in range(1, len(A)-1):
            A[row][col] = 1 - A[row][col]
    return A

def next_life_generation( A ):
    """ makes a copy of A and then advanced one generation of Conway's game of life within
    the *inner cells* of that copy. The outer edge always stays 0.
    """
    def countNeighbors( row, col, A ):
        """helper function that returns the number of
            live neighbors for a cell in the board A at a particular row and col
            """
        count = 0
        count -= A[row][col] 
        for i in range(-1, 2):
            for j in range(-1, 2):
                count += A[row + i][col + j]
        return count

    newA = copy(A)
    for row in range(1, len(A)-1):
        for col in range(1, len(A[row])-1):     #1. All edge cells stay zero (0) 
            neighbors = countNeighbors(row, col, A)
            if A[row][col] == 1:
                if neighbors < 2 or neighbors > 3:  #2. A cell that has fewer than two live neighbors dies (because of loneliness)
                                                    #3. A cell that has more than 3 live neighbors dies (because of over-crowding)
                    newA[row][col] = 0  
            else:
                if neighbors == 3:  #4. A cell that is dead and has exactly 3 live neighbors comes to life
                    newA[row][col] = 1  

    return newA

'''A = [ [0,0,0,0,0],
[0,0,1,0,0],
[0,0,1,0,0],
[0,0,1,0,0],
[0,0,0,0,0]]

printBoard(A)

print("________")

A2 = next_life_generation( A )
printBoard(A2)

print("________")

A3 = next_life_generation( A2 )
printBoard(A3)'''