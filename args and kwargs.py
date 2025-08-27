'''
args: *args allows a function to accept any number of positional arguments (like a tuple).
kwargs: **kwargs allows a function to accept any number of keyword arguments (like a dictionary).
'''

#example for args
def sum(*args):
  total=0
  for i in args:
    total+=i
  return total

print(sum(2,3,4,4,5,5))


#example for kwargs
def marks(**kwargs):
  for item in kwargs.keys():
    print(f"The marks of {item} is {kwargs[item]}")

marks(edward=99,jessy=100,john=100)
      

#example for args and kwargs
def func(*args,**kwargs):
  print(args)
  print(kwargs)

func(1,2,3,4,jack=34,jill=45,marie=32)