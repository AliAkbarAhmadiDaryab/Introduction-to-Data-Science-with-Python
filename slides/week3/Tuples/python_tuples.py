# How to define a tuple
mytuple = ("apple", "banana", "cherry")
print(mytuple)

# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# mytuple[0] = 'mango' # This will through and error

# 
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Access Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
# Add item to tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y # thistuple = thistuple + y

print(thistuple)


# Unpack Tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)