# Task 1: Student Bio Data Storage
# Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary.
#  * Courses should be stored as a list
#  * Display the bio-data neatly using escape sequences
#  * Requirements
#     * Use input() to collect details
#     * Use dictionary operations (dict[key] = value) to store data.
#     * Use print() formatting with \n and \t for better output


student_name = input("Enter your name here: ")
student_age = int(input("Enter student\'s age here: "))
student_gender = input('Enter student\'s gender here: ')
student_courses = input('Enter your courses separated by space here: ')

#Create dictionary
student_bio = {}
student_bio['Student Name'] = student_name
student_bio['age'] = student_age
student_bio['gender'] = student_gender
student_bio['courses'] = student_courses.split()

#Print Output
courses_fmt = ' '.join(student_bio['courses'])
print(f'name: {student_bio["Student Name"]:>44} \nage: {student_bio["age"]:>45} \ngender: {student_bio["gender"]:>42} \ncourses: {courses_fmt:>41}')