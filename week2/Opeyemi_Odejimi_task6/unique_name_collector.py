# Task 2: Unqiue Name Collector
#  * Write a program that collects the names of people attending a seminar(no duplicates allowed) and displays them in alphabetical order.
visitor1 = input("Enter your name: ")
visitor2 = input("Enter your mame: ")
visitor3 = input("Enter your name: ")

seminar_attendees = (visitor1, visitor2, visitor3)
display = sorted(seminar_attendees)
print(display)
