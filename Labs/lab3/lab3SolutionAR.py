############################################################
# Name: Anthony Rizzuto
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. Anthony Rizzuto
# CS115 Lab 3
#
############################################################

def change(amount, coins):
    '''
    This function takes two elements, amount and coins, where amount is an integer that represents
    the amount of change that a customer is to be given.

    Coins is represented as a list, which tells the program the values of the coins available.

    The program then finds the smallest number of coins needed to add up to "amount" only using the values 
    in "coins" list.
    '''
    if amount == 0:
        return 0
    elif coins == [] or amount < 0:
        return float("inf")
    else:
        use_it = change(amount - coins[0], coins[0:]) + 1
        lose_it = change(amount, coins[1:])
    
    return min(use_it, lose_it)

print(change(48, [1, 5, 10, 25, 50]))