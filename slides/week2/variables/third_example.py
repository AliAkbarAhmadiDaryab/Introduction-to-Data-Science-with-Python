# Global Variable inside the function
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)