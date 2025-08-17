# Task 4: Create a Unique Voter Registration System
# * Ask for voters name and store in a set
# * If a voter tries to register twice, display a warning
# * After registration, display the total number of unique voters.




#Create a set of names
voter_names = {"Aishat", "Segun"}
new_name = input("Enter your name here: ")
if new_name in voter_names:
    print("You already registered abeg!")
#Add name to set
voter_names.add(new_name)
print(voter_names)