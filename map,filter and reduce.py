'''
map(): A built-in python function which is used to apply a method to each element in iterables like list,tuple etc..
filter(): A function in Python which is used to apply a method/function on data structures like list, tuple
etc.,and it keeps only those elements for which the function returns True.
reduce(): A function in Python (from the functools module) that applies a given function 
cumulatively to the elements of an iterable, reducing the iterable to a single value
'''

'''
#example for map()
l1=[1,2,3,4,5]

def square(x):
  return x*x

new=list(map(square,l1))
print(new)
'''

'''
#example for filter()
l1=[1,2,3,4,5,6,7,8,9,10]

def condition(x):
  if x>4:
    return x
  
new=list(filter(condition,l1))
print(new)
'''

'''
#example for reduce
from functools import reduce
l1=[1,2,3,4,5,6]

def sum(a,b):
  return a+b

new=reduce(sum,l1)
print(new)
'''

'''
working of the above example
[1,2,3,4,5,6]
[3,3,4,5,6]
[6,4,5,6]
[10,5,6]
[15,6]
[21]
'''