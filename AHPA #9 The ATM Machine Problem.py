# AHPA #9 - The ATM Machine Problem
#
# Create software that will provide 
# an ATM user with the proper change 
# for any dollar amount up to $200.

# Example: Run the code for $19, $55, and $200.
#
# Student Name: Linh Nguyen
#

amount = float(input("Enter the dollar amount up to $200: "))

if amount < 0 or amount > 200:
    print("Invalid. Amount entered should be between $0 and $200.")
else:
    if amount >= 100:
        hundreds = int(amount // 100)
        amount %= 100
    else:
        hundreds = 0

    if amount >= 50:
        fifties = int(amount // 50)
        amount %= 50
    else:
        fifties = 0

    if amount >= 20:
        twenties = int(amount // 20)
        amount %= 20
    else:
        twenties = 0

    if amount >= 10:
        tens = int(amount // 10)
        amount %= 10
    else:
        tens = 0

    if amount >= 5:
        fives = int(amount // 5)
        amount %= 5
    else:
        fives = 0

    if amount >= 1:
        ones = int(amount)
    else:
        ones = 0

print("Amount of change for this amount is: {0} x $100, {1} x $50, {2} x $20, {3} x $10, {4} x $5, {5} x $1 ".format(hundreds, fifties, twenties, tens, fives, ones))