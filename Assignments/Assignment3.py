import math

# Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.
def factorial(number1):
    result = 1
    for i in range(1, number1 + 1):
        result *= i
    return result

n = int(input("Enter a number : "))
print(f"Factorial of {n} is: {factorial(n)}")

# Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)

number2 = int(input("Enter a number : "))
def square_root(num):
    return num ** 0.5
def natural_log(num):
    return math.log(num)
def sine(num):
    return math.sin(num)
print(f"Square root :  {square_root(number2)}")
print(f"Logarithm :  {natural_log(number2)}")
print(f"Sine : {sine(number2)}")
