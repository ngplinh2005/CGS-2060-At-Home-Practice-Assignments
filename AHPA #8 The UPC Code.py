# AHPA #8 - The UPC Code
#
# Student Name: Linh Nguyen

"""
Part 1: 

Your assignment is to take a UPC code, divide it up into its four parts, then print them out in separate fields on a single line. 

Use this UPC code:
(020357122682)

Note: the program has to work for ANY UPC code in this formatâ€¦

Part 2: 

Assume that this item costs $275.15. I would like to buy 12 of them. On a single line print out quantity to purchase, unit cost, and total cost (7 digits, 2 digits of precision, with commas separating thousands)
"""

# Part 1

UPCCode = "020357122682"
part1 = UPCCode[:1]
part2 = UPCCode[1:6]
part3 = UPCCode[6:11]
part4 = UPCCode[11:]

print("Four parts of the UPC Code are: {0}, {1}, {2}, {3}".format(part1, part2, part3, part4))

# Part 2

quantity = 12
unit_cost = 275.15
total_cost = quantity * unit_cost

print("Quantity to purchase: {0}, Unit Cost: {1}, Total Cost: {2:,.2f}".format(quantity, unit_cost, total_cost))
