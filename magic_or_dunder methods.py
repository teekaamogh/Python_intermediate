class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary

  def __str__(self):
    return f"The name of the employeer is:{self.name} and his salary is:{self.salary}"
  
  def __repr__(self):
    return f"The name of the employeer is:{self.name} and his salary is:{self.salary}"
  
  def __len__(self):
    return len(self.name)
  
e1=Employee("Amogh",19)
print(e1.name)
print(str(e1))
print(repr(e1))
print(len(e1))