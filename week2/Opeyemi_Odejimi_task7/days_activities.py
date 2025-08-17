# Task 3: Days and Activities pairing
# * Store days of the week in a tuple and ask the user to input an activity for three specific days.
# * Use dictionary comprehension to pair days and activities
# * Print the dictionary
# * Requiremnets:
# * Use a tuple for days

days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 'Saturday')
day_one = input("Enter first day of the week where you partook in an activity: ")
day_two = input("Enter second day of the week where you partook in an activity: ")
day_three = input("Enter third day of the week where you partook in an activity: ")

#Ask user for 3 activities
first_activity = input("What is the first activity?: ")
second_activity = input("What is the second activity?: ")
third_activity = input("What is third activity?: ")
#Display dictionary
days_active= (day_one, day_two, day_three)
activities = (first_activity, second_activity, third_activity)
print({day: activity for day, activity in zip(days_active, activities)})