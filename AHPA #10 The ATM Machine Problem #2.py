# AHPA #10: The ATM Machine Problem #2

# Create software that will provide 
# an ATM user with the proper
# change_amount for any dollar amount.

# Create two separate solutions: 
# one that uses a While loop and 
# one that uses a For loop.

# Example: run the code for $1917,
# $550, and $23.
#
# Student Name: Linh Nguyen     

# Solution 1: Using a While loop

amount = float(input("Enter the dollar amount: "))

if amount < 0:
    print("Invalid input")
else:
    hundreds = fifties = twenties = tens = fives = ones = 0
    
    while amount >= 100:
        hundreds += 1
        amount -= 100
    
    while amount >= 50:
        fifties += 1
        amount -= 50
    
    while amount >= 20:
        twenties += 1
        amount -= 20
    
    while amount >= 10:
        tens += 1
        amount -= 10
    
    while amount >= 5:
        fives += 1
        amount -= 5
    
    while amount >= 1:
        ones += 1
        amount -= 1
    
    print("The change_amount for this dollar amount is: {0} x $100, {1} x $50, {2} x $20, {3} x $10, {4} x $5, {5} x $1 ".format(hundreds, fifties, twenties, tens, fives, ones))

# Solution 2: Using a For loop

amount = float(input("Enter the dollar amount: "))

if amount < 0:
    print("Invalid input")
else:
    hundreds = fifties = twenties = tens = fives = ones = 0

    for i in range(int(amount)):
        if amount >= 100:
            hundreds += 1
            amount -= 100
        elif amount >= 50:
            fifties += 1
            amount -= 50
        elif amount >= 20:
            twenties += 1
            amount -= 20
        elif amount >= 10:
            tens += 1
            amount -= 10
        elif amount >= 5:
            fives += 1
            amount -= 5
        elif amount >= 1:
            ones += 1
            amount -= 1

    print("The change for this dollar amount is: {0} x $100, {1} x $50, {2} x $20, {3} x $10, {4} x $5, {5} x $1 ".format(hundreds, fifties, twenties, tens, fives, ones))
