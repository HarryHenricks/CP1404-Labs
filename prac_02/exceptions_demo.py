"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When either numerator or denominator aren't in the integer type e.g. floats, strings and booleans will all cause the program to crash
2. When will a ZeroDivisionError occur? When the denominator is equal to 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes, add an if statement that returns "error not valid input"
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        denominator = int(input("Please enter a non zero term for the denominator"))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")