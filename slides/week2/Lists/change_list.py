thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Add Item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert to specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
