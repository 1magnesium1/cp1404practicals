"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

BONUS_THRESHOLD = 1000
LOW_BONUS = 0.1
HIGH_BONUS = 0.15

value_of_sales = float(input("Enter your total value of sales: "))

while value_of_sales >= 0:
    if value_of_sales >= BONUS_THRESHOLD:
        bonus = value_of_sales * HIGH_BONUS
    else:
        bonus = value_of_sales * LOW_BONUS

    print(f"Your sales were {value_of_sales}. This gets you a bonus of ${bonus}.")
    value_of_sales = float(input("Enter your total value of sales: "))

