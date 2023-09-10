# You cannot copy a list simply by typing list2 = list1, 
# because: list2 will only be a reference to list1, 
# and changes made in list1 will automatically also be made in list2.


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# use list builtin function, 
# under the hood there are doing the same things
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
