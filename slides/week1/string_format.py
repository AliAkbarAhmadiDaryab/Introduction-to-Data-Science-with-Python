age = 36
# txt = "My name is John, I am " + age # this line will have error.
# print(txt) 

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


quantity = 3
item_no = 567
price = 49.95
myorder = "I want {quantity} pieces of item {item} for {price} dollars."
print(myorder.format(quantity=quantity, item=item_no, price=price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))