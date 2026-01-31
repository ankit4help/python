# ASSIGNMENT 2
# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.
number = input("Enter a number: ")
if int(number) % 2 == 0:
    print( number + " is a even number.")
else:
    print(number + " is a odd number.")

# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.

total = 0
for i in range(1, 51):
    total += i
print("The sum of numbers form 1 to 50 is:", total )