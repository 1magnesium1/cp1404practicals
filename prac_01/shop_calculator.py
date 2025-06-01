DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1
total = 0
number_of_items = int(input("Enter number of items you are purchasing: "))

for i in range(number_of_items):
    price_of_items = float(input("Enter price of item: "))
    total += price_of_items

if total > DISCOUNT_THRESHOLD:
    discount = total * DISCOUNT_RATE
    total -= discount

print(f"Total price for {number_of_items} items is ${total:.2f}")
