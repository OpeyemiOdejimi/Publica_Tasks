'''
Task 3: Online Store Cart Calculation
* Create a list of items (e.g., "Book", "Pen, "Bag") and another list of prices (e.g., 500, 100, 2000).
* Start with an empty cart total (cart_total = 0)
* Use assignment operators (+=) to add the price of some items into cart_total.
* Print the list of items and the total price using an f-string like this       
'''
items = ["Book", "Pen", "Bag"]
prices = [500, 100, 2000]
cart_total = 0
cart_total += prices[0]
cart_total += prices[1]
print(f"Items: {items}")
print(f"Total Price: N{cart_total}")
