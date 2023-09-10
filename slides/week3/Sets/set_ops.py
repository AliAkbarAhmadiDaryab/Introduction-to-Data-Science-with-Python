# Join sets, duplicate are not allowed
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# User keyword update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# intersection, use the common elements
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# Keep in mind, it is on object operation
x.intersection_update(y)

print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# This will return a new set
z = x.intersection(y)

print(z)

# Keep all element expect the duplicate in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# Object level
x.symmetric_difference_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

