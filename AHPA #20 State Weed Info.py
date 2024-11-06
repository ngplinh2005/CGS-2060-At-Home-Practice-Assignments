# AHPA #20 - State Weed Info
#
# Open the state data file and create 3 separate dictionaries: 
# one for population, one for representatives, and one for  % of U.S. population.
#
# Answer the following questions:
# 1. What % of the U.S. lives in the original 13 colonies?
# [New Hampshire, Massachusetts, Connecticut, Rhode Island, New York, New Jersey, Pennsylvania, Delaware, 
# Maryland, Virginia, North Carolina, South Carolina, Georgia]
#
# 2. If California fell into the ocean, what % of our population would we lose?
# 
# 3. If President Biden needs to get a bill passed and only California, Texas, Florida, and New York support it, will it pass in the House? 
# [There are 435 representatives]
#
# 4. What percentage of representatives come from Florida?
# 
# 5. Four states have legalized marijuana for recreational use (Washington , Oregon , Colorado, and Alaska). How many people can legally use weed?
#
# Student Name: Linh Nguyen
#

# Open file
file = open("AHPA #20 - State Data.txt", "r")

# Create 3 separarte dictionaries
population_dict = {}
representatives_dict = {}
us_population_percent_dict = {}

# Find total U.S. population 
total_population = 0
for line in file:
    state, population, representatives = line.split("\t")
    population = int(population)
    representatives = int(representatives)
    
    population_dict[state] = population
    representatives_dict[state] = representatives
    total_population += population

# Calculate population percentage for each state
for state in population_dict:
    us_population_percent_dict[state] = (population_dict[state] / total_population) * 100

# Close file
file.close()

# 1. What % of the U.S. lives in the original 13 colonies?
colonies = ["New Hampshire", "Massachusetts", "Connecticut", "Rhode Island", 
            "New York", "New Jersey", "Pennsylvania", "Delaware", 
            "Maryland", "Virginia", "North Carolina", "South Carolina", "Georgia"]

colonies_population = 0
for state in colonies:
    colonies_population += population_dict[state]
colonies_population_percent = (colonies_population / total_population) * 100
print(f"Percentage of U.S. lives in the original 13 colonies: {colonies_population_percent:.2f}%")

# 2. If California fell into the ocean, what % of our population would we lose?
california_population_percent = us_population_percent_dict["California"]
print(f"Percentage of population lost if California fell into the ocean: {california_population_percent:.2f}%")

# 3. If President Biden needs to get a bill passed and only California, Texas, Florida, and New York support it, 
# will it pass in the House? 
supporting_states = ["California", "Texas", "Florida", "New York"]
total_representatives_support = 0
for state in supporting_states:
    total_representatives_support += representatives_dict[state]
if total_representatives_support > 435 / 2:
    will_pass = "Yes"
else:
    will_pass = "No"
print(f"If only CA, TX, FL, and NY support, will the bill pass? {will_pass}")

# 4. What percentage of representatives come from Florida?
florida_representatives_percent = (representatives_dict["Florida"] / 435) * 100
print(f"Percentage of representatives from Florida: {florida_representatives_percent:.2f}%")

# 5. Four states have legalized marijuana for recreational use (Washington , Oregon , Colorado, and Alaska). 
# How many people can legally use weed?
legal_states = ["Washington", "Oregon", "Colorado", "Alaska"]
legal_population = 0
for state in legal_states:
    legal_population += population_dict[state]
print(f"Population in states with legalized recreational marijuana: {legal_population}")