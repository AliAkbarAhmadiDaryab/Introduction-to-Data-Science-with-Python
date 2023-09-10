myset = {"apple", "banana", "cherry"}
print(myset)

# Set items are unordered, unchangeable, and do not allow duplicate values.
# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Duplicates not allowed, check the result
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# True and 1
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

# Get the len of the list
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# Check the output
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# Set with various data types
set1 = {"abc", 34, True, 40, "male"}

# Create a list using the set constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
