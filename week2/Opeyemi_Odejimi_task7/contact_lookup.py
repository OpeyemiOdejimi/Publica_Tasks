# Task 5: Contact Quick Lookup
# * Store three names and their phone numbers in two separate tuples
# * Create a dictionary from them using dict(zip(...))
# * Ask the user for a name and display the corresponding number (or an error message.)
# * Requirements:
# * Use zinc() and dict() to combine tuples
# * Use .get() for safe retrieval
# No loops

#Create tuples for names and phone numbers
names = ("Serif", "Tade", "Femi")
phone_num = ("01-744664", "01-75837", "01-464647")

#Create a dictionary
information = {name: num for name, num in zip(names, phone_num)}

#Ask the users for a new name plus get number
username = input("Enter a name: ")
print(information.get(username))


