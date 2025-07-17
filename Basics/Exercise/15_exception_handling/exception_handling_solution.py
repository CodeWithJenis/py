class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID: {self.id} \nName: {self.name}")


# Creating a emp instance of Employee class
emp = Employee(1, "coder")

emp.display()
# Deleting the property of object
del emp.id
try:
    print(emp.id) #this is a attribute error not nameerror as there is no attribute emp.id as we just deleted by del emp.id
except AttributeError:
    print("emp.id is not defined")
  
# Deleting the object itself
del emp
try:
    emp.display()  
except NameError:
    print("emp is not defined")
