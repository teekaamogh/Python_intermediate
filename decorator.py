'''
Decorators and wrappers:
wrappers is a fucntion which is used to add additional line of codes to a function 
decorators is a function which runs the wrapper function
in this example we are adding additional lines of code to the say_hello() function
'''

def say_hello():
  print("Hello") #this is the basic function


def decorator():   
  def wrapper():   
    print("Before hello")
    say_hello()            #here we are calling the function say_hello()
    print("After hello")
  return wrapper

x=decorator()   
x()

'''
x=decorator()   
x()
In this code when we call decorator function using decorator()
It just returns the wrapper function
In x=decorator() the returned wrapper function is stored in x
When we use x(), we are calling the x variable which means we are calling the wrapper function

We can also use decorator()()
Here 1st () returns the wrapper function and 2nd () calls the function
'''