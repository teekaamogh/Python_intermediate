'''
Walrus operator(:=): The walrus operator is like the assignment operator, but it can be used inside 
expressions (such as conditionals, loops, and function calls).
Note: assignment operator can't be used in conditions like if(x=10), it gives error
hence we use walrus operator if(x:=10)
'''

'''
if (n := len([1, 2, 3, 4])) > 2:
  print(f"List has {n} elements")
'''

def hello():
  print("Hello")
  print("Hello")
  print("Hello")
  print("Hello")
  print("Hello")
  return 1

if((a:=hello())>10):
  print(a)

else:
  print("Its not greater than 10")