# Access items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# Add item to set
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Add item from another set

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# remove from set
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
# Remove random items
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
# How to empty the set
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)