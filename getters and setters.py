'''
@property:If we use @property, it lets us access the attribute without parentheses (()), as if it were a normal variable
@<method_name>.setter: Used with a getter generally which is used to modify the value of attribute
'''

class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary

  @property
  def first_name(self):
    first=self.name.split()
    return first[0]
  
  @first_name.setter
  def change_name(self,new_name):
    x=self.name.split()[1]
    y=f"{new_name} {x}"
    self.name=y

e=Employee("Daenerys Targaryen",297000)
print(e.first_name)               #we write print(e.first_name()) normally, but with @property we can ignore ()
e.change_name="Aegon"            #we write e.change_name("abc") normally, but with @method_name.setter we can ignore () and use =
print(e.name)             

