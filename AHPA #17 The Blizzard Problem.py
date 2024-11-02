# AHPA #17: The Blizzard Problem
#
# 1. Print out the lists: one item per line.
#
# 2. In the Candy Cravers list, print the Heath item's location.
#
# 3. In the Classic Creations list, print the Royal Rocky Road item's location.
#
# 4. Add a new Classic Creation: "red licorice". 
#
# 5. Print new list.
#
# 6. Remove the Heath Blizzard from Candy Cravers. 
#
# 7. Print new list.
#
# 8. Combine the lists and print on one line
#
# 9. Print a count of the total number of treats provided
#
# Student Name: Linh Nguyen
#

candyCravers = ["Reese's Peanut ButterCup", "Butterfinger", "Oreo", "Heath", "M&M's"]

classicCreations =["Banana Split", "Salted Caramel Truffle", "M&M's Peanut Butter Monster Cookie", 
"Georgia Mud Fudge", "Double Fudge Cookie Dough", "Chocolate Xtreme",
"Peanut Butter Cookie Dough Smash", "Chocolate Chip Cookie Dough", "Royal Rocky Road", "Chocolate Covered Strawberry", "Choco Covered Strawberry", "Royal Rocky Road",
"Turtle Pecan Cluster", "Mint Oreo", "Royal New York Cheesecake", "Royal Oreo"]

#1: Print out the lists: one item per line.
print("Items in candyCravers list: ")
for item in candyCravers:
    print(item)

print("Items in classicCreations list: ")
for item in classicCreations:
    print(item)

#2: In the Candy Cravers list, print the Heath item's location.
print(candyCravers.index("Heath"))

#3: In the Classic Creations list, print the Royal Rocky Road item's location.
print(classicCreations.index("Royal Rocky Road"))

#4 + 5: Add a new Classic Creation: "red licorice" + print new list
classicCreations.append("red licorice")
print("New classicCreations list: {0}".format(classicCreations))

#6 + 7: Remove the Heath Blizzard from Candy Cravers + print new list
candyCravers.remove("Heath")
print("New candyCravers list: {0}".format(candyCravers))

#8: Combine the lists and print on one line
combination = candyCravers + classicCreations
print(combination)

#9: Print a count of the total number of treats provided
print("The number of treats provided is {0}".format(len(combination)))