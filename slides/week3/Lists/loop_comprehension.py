# Copy element of one element to another one
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# Using the loop Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# General Syntax

# newlist = [expression for item in iterable if condition == True]
# Using if statement
newlist = [x for x in fruits if x != "apple"]

# without it
newlist = [x for x in fruits]

# The expression can contain the conditions
newlist = [x if x != "banana" else "orange" for x in fruits]