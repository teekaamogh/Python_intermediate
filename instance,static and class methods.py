'''
Instance method:
An instance method is a method in a class that takes the object/instance(referredas self) as its first argument 
By default we use instance method. These methods take 'self' as their default arguement during runtime

Static method:
A static method is a method in a class that does not take self as its first argument,
meaning it can run without being tied to any object or class
Note:when we use static method without @staticmethod it gives us as error
(ex: takes 2 positional arguments but 3 were given)

Note:
Self is not required in sum() method because we are not using the arguments a&b in other methods
Static methods are required because they can be used to run methods without the need of creating object

Class method:
It is a method which is used to take class itself as first argument(cls), it can modify vairables throughout 
all objects
'''

class Employee:

  company="HP"
  def __init__(self,name,age):
    self.name=name 
    self.age=age
  
  def display(self):                              #display() is an example of instance method
    print(f"Name:{self.name}\nAge:{self.age}")

  @staticmethod                                   #by using @staticmethod it becomes a static method 
  def sum(a,b):                                   #sum() is an static method and it doesn't need self argument
    print(a+b)

  @classmethod
  def comp_name(cls):
    print(cls.company)

  @classmethod
  def change_name(cls,new_name):
    cls.company=new_name

e1=Employee("Amogh",19)                           #we created an object e1 to run instance method
e1.display()

Employee.sum(2,3)                                 #no need of creating object to run static method

e1.comp_name()                                    #prints HP 
e1.change_name("Asus")                            
e1.comp_name()                                    #prints Asus as it is changed
e2=Employee("Amogh",19)
e2.comp_name()                                    #prints Asus even though it is not changed to Asus
