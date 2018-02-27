"""
Program to allow users to enter number of items and price of each item.
If total price is over $100 then a 10% discount is to be applied.
"""

number_items = int(input("Enter your number of items: "))
prices = list()
counter = 1
total_price = 0

if number_items <= 0:
    print("Invalid, you can't have zero or less items")

for i in range(number_items):
    item_price = float(input("What is the price of your item {0}?".format(counter)))
    total_price += item_price
    counter = counter + 1

if total_price > 100:
    total_price = total_price * 0.9 #apply 10% discount if total price is over $100


print(total_price)

