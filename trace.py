def subset(capacity, items):
    if capacity <= 0 or items == []:
        return 0
    elif items[0] > capacity:
        return subset(capacity, items[1:])
    else:
        use_it = items[0] + subset(capacity - items[0], items [1:])
        lose_it = subset(capacity, items[1:])
        return max(use_it, lose_it)

print (subset(7, [2,3,4]))

'''
2 + subset(5, [3,4])
    3 + subset(2, [4])
            subset(2, [])
            0
    subset(5,[4])
2 + (7-3)= 6
2 + (7-4) = 5


'''