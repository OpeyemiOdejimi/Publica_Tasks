'''
Task 5: Store Inventory Update
  * Create a dictionary called store with items and their available quantities. Example:
  store = {"Book": 10, "pen": 20, "Bag": 5}
  * Ask the user to input the item they want to buy (e.g., "Pen").
  * Ask the user to input the quantity they want to purchase
  * Use the assignment operator -=to update (reduce) yhe item quantity in the dictionary.
  * Print the updated dictionary in this format:
  
  Before purchase: {'Book': 10, 'Pen': 20, 'Bag': 5}
  After purchase: {'Book': 10, 'Pen': 18, 'Bag': 5}
'''

store = {
    "Book": 10,
    "Pen": 20,
    "Bag": 5
}

print(f"Before purchase: {store}")
buy = input("Input the item you want to buy (Book/Pen/Bag): ")
quantity = int(input("How many?"))

store[buy] *= quantity
print(f"After purchase : {store}")

# store = {
#     "Book": 10,
#     "Pen": 20,
#     "Bag": 5
# }


# item_to_buy = input("Enter the item you want to buy (We have Book, Pen and Bag): ")
# quantity = int(input(f"Enter the quantity of {item_to_buy}s you want to buy: "))

# print(f"Before purchase: {store}")

# store[item_to_buy.title()] -= quantity

# print(f"After purchase: {store}")