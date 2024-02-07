'''
Created on December 3rd , 2023
@author:   Anthony Rizzuto
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5 
'''

memo = {}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    result = 0
    if n in memo:
        return memo[n]
    if n == 0:
        return 2
    elif n == 1:
        return 1
    
    else: 
        result = fast_lucas(n-1) + fast_lucas(n-2)

    memo[n] = result
    return result


def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_help(amount, coins, memo):
        result = 0
        if (amount, tuple(coins)) in memo:
            return memo[(amount, tuple(coins))]
        if amount == 0:
            return 0
        elif not coins:
            result = float('inf') 
        else: 
            if amount >= coins[0]: 
                use_it = 1 + fast_change_help(amount - coins[0], coins, memo)
            else: use_it = float('inf')

            lose_it = fast_change_help(amount, coins[1:], memo)
            result = min(use_it, lose_it)

        memo[(amount, tuple(coins))] = result
        return result
    return fast_change_help(amount, coins, {})
    
    

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


