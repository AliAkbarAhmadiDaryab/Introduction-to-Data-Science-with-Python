# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# For example, 'hello' is the same as "hello".

print("Hello")
print('Hello')

a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Multiline Strings using single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# String Slicing
b = "Welcome to Python!"
print(b[2:5])

b = "Welcome to Python!"
print(b[:5])

# Python built in Functions for string
# Upper
a = "Hello, World!"
print(a.upper())

# Lower
a = "Hello, World!"
print(a.lower())

# Strip()
a = " Welcome to Python! "
print(a.strip()) # returns "Hello, World!"

# Replace
a = "Welcome to Python!"
print(a.replace("P", "D"))

# Split
a = "Welcome to Python!"
print(a.split(",")) 