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
            use_it = 1 + fast_change_help(amount - coins[0], coins, memo)
            lose_it = fast_change_help(amount, coins[1:], memo)
            result = min(use_it, lose_it)

        memo[(amount, tuple(coins))] = result
        return result
    return fast_change_help(amount, coins, {})
    