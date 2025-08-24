'''
Task 2

Comment the code below appropriately, and using docstring, explain what the code is doing.
Adapt the code to the case below
Federal Government Scholarship Key Eligibility Requirements:
   Citizenship:
     Applicant must be a citizen of Nigeria.
   Enrollment:
      Must be registered, full-time undergraduate student in a recognized Nigerian university.

   Other Scholarships:
      Applicants cannot be currently recieveing any other scholarship from an entity in the Oil and Gas industry, whether national or international.
   Academic Qualification:
    For undergraduate vourses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.
'''

name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))

eligibility = (age < 18) and (score > 70)
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

# The code above will run True if the age of the student is less than 18 and socre is greater than 70. Any other condition will come out as false.
