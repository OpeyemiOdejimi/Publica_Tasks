# Task 3: Stimulate a football match ticket system
#   * Store all seats numbers (1 to 50) in a set
#   * Ask users to "book" a seat by entering the number
#   * Remove booked seats from the seat
#   * Show remaining seats after each booking.


set_of_numbers = set([i for i in range(1, 51)])
seat_number = int(input("Choose seat number of choice: "))
set_of_numbers.remove(seat_number)
print(set_of_numbers)