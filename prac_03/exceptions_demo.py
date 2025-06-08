"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Value error occurs when a string or floating point is entered.
2. When will a ZeroDivisionError occur?
Occurs when division by zero is attempted.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
You could use a while loop. To loop while a zero is entered."""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Invalid, cannot divide by zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
