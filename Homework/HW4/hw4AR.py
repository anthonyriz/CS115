'''
Created on October 23, 2023
@author:   Anthony Rizzuto
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 4
'''

def pascal_row(n):
    """return the nth row of Pascal's Triangle"""
    
    def prev_row(x):
        '''helper function that calculates previous row terms in Pascal's Triangle '''
        if len(x)==1:
            return [1]
        else: 
            return [x[0] + x[1]] + prev_row(x[1:])
            
    if n == 0:
        return [1]
    if n == 1:
        return [1,1]
    else:
        return [1] + prev_row(pascal_row(n-1))

def pascal_triangle (n):
    '''prints a list of lists containing all the values of Pascal's Triangle up to row n'''
    if n == 0:
        return [[1]]
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]

def test_pascal_row():
    '''tests the function pascal_row(n) using assertion'''

    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]
    assert pascal_row(9) == [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

def test_pascal_triangle():
    '''tests the function pascal_triangle(n) using assertion'''

    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(10) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1], [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]]

test_pascal_row()