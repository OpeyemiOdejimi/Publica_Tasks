# Task 2: Super Market Price List
# * Create a program that stores items and their prices in a dictonary
# * Items should come from a list
# * Prices are entered by the user
# * Display all items and prices, then allow the user to update the price of an item.
# * Requirements:
#  * Use dictionary update method .update() or assignment
#  * Use .keys() to display available items.
#  * Use input validation (no advanced functions)

items = ["tyre", "nail", "pencil"]

#Collect prics
price1 = float(input("Enter price for first item: "))
price2 = float(input("Enter price for second item: "))
price3 = float(input("Enter price for third item: "))

#Create dictionary to store items and their prices
dic = {}
dic[items[0]] = price1
dic[items[1]] = price2
dic[items[2]] = price3

#Display items and their output
print(list(dic.keys()))
print(list(dic.values()))

#Update an item price
change_item = input("Enter item which price you want to update: ")
change_price = float(input("Enter updated price here: "))
print(change_item in dic.keys())

dic.update({change_item: change_price})
print(dic)