# The simplest way of looping through the list elements
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
  
# Loop the list using it's index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])  
  

# Using the while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
# Looping using the loop Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]  