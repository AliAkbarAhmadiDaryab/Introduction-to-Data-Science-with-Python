# Python Classes/Objects
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

# How to create a class
class MyClass:
  x = 5
  
# Create Object 
p1 = MyClass()
print(p1.x)

# class __init__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Ali", 40)

print(p1.name)
print(p1.age)

# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Ali", 40)

print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("Ali", 40)

print(p1)

# Object Method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Ali", 40)
p1.myfunc()
# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.