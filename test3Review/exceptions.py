'''
Exception Examples
@author: Zumrut Akcam-Kibis
'''
"""
#Example 1
try:
    x = 23
    print(list(map(lambda y : y+1, x)))
except ZeroDivisionError:
    print('This is an IO Error')
except TypeError:
    print('This is a Type Error')
else:
    print('Hello')
finally:
    print('Finally')
print('Done here')"""

'''
#Example 2:
try:
    n = 5
    d = 2 # Try changing this to 2.
    print(n/d)
except ValueError:
    print('This is a Value Error')
except ZeroDivisionError:
    print('This is a Zero Division Error')
else:
    print('We are good to go')
print('Done deal!')'''



#Example 3: Some exception examples
a = int('rest') # ValueError
l = [1,2,3]
print(l[5]) # Index Error
dic = {'5':'here', '6':'there'}
print(dic['8']) #Key Error
