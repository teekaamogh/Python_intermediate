'''
Exception handeling: It is used to handle runtime errors such that the code does not crash
try: The block in which you write the code that might cause an error.
except: The block that runs if an error occurs in try block.
raise: A python keyword used to manually raise an exception.
finally: A block that always executes, no matter hwat happens in try or except blocks.
Note: There are multiple type of exception handeling techniques like ValueError,ZeroDivisionError etc...
'''

while True:
  try:
    x=int(input("Enter 1st number:"))
    y=int(input("Enter 2nd number:"))
    print(f"The division of {x} by {y} is {x/y}")

  except ZeroDivisionError:
    print("Cannot divide by zero.")

  except ValueError:
    print("Wrong datatype entered.")
  
  except Exception as e:
    print("Unknown error.")

  if(y==0):
    raise ZeroDivisionError("Cannot divide by 0")


'''
#Example using try,exception and else  
try:
  a=int(input("Enter 1st number:"))
  b=int(input("Enter 2nd number:"))
  print(a/b)

except Exception as e:
  print(e)

else:
  print("Exectuted the code")
'''

'''
#Example for finally block
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
try:
  c=a/b
  print(c)
except Exception as e:
  print(e)

finally:
  print("This is always executed)       #no matter whether the output is valid or invalid this block will be executed
'''