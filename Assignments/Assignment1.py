# ASSIGNMENT 1:
# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
Addition = number_1 + number_2
Subtraction = number_1 - number_2
Multiplication = number_1 * number_2
Division = number_1 / number_2
print(" Addition: ", Addition)
print(" Subtraction: ", Subtraction)
print(" Multiplication: ", Multiplication)
print(" Division: ", Division)

# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print(" Hello," + full_name + " ! Welcome to the Python program")