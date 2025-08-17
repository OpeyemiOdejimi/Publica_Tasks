# Task 4: Unique Members Registration
# * Ask the user to enter three names separated by commas
# * Convert them to a set to ensure uniqueness.
# * Requirements:
# * Use.split(",") and set() to remove duplicates
# * Use dictionary comprehension {name: len(name) for name in set_of_names}


names = input("Enter three names separated by comma: ")

#Create and display dictionary
name_one= set(names.split(','))
name_one = set(name.strip() for name in name_one)
names_saved_in_dic = {name: len(name) for name in name_one}
print(names_saved_in_dic)