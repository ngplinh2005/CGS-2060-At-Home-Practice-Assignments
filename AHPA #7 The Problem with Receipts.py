# AHPA #7 - The Problem With Receipts
#
# Your boss at the auto repair store # has given you three receipts that # he wants you to write a Python # program to process.

# The receipts are a mess: they
# have extra spaces in them at the # start and end.

# If the receipt has a "!" in it
# then it means that this customer # is a high volume customer.

# For each receipt:
# 1. Print out just the name
# 2. Set a Boolean variable if the # customer is a high volume customer
# 3. Print out the Boolean variable
# 4. Print out how much the customer spent
# 5. Print out what the customer purchased

# Student Name: Linh Nguyen


receipt1 = "Bob Johnson  ! $127.52/ [Tires]   "
receipt2 = "             Amy Johnson     $35.18/ [Oil Change]  "
receipt3 = "      Tim Brown       ! $239.15/  [Alignment]        "

# 1. Print out just the name
receipt1 = receipt1.strip()
customer1_name = receipt1.split("!")[0]
customer1_name = customer1_name.strip()
print("Name of Customer 1 is", customer1_name)

receipt2 = receipt2.strip()
customer2_name = receipt2.split("$")[0]
customer2_name = customer2_name.strip()
print("Name of Customer 2 is", customer2_name)

receipt3 = receipt3.strip()
customer3_name = receipt3.split("!")[0]
customer3_name = customer3_name.strip()
print("Name of Customer 3 is", customer3_name)

# 2 & 3. Set a Boolean variable if the # customer is a high volume customer and print out the Boolean variables

if "!" in receipt1:
    high_volume_customer = True
else:
    high_volume_customer = False
print(customer1_name, "is a high volume customer: ", high_volume_customer)

if "!" in receipt2:
    high_volume_customer = True
else:
    high_volume_customer = False
print(customer2_name, "is a high volume customer: ", high_volume_customer)

if "!" in receipt3:
    high_volume_customer = True
else:
    high_volume_customer = False
print(customer3_name, "is a high volume customer: ", high_volume_customer)

# 4. Print out how much the customer spent

customer1_spent = receipt1.split("$")[1].split("/")[0].strip()
print(customer1_name, "spent $", customer1_spent)

customer2_spent = receipt2.split("$")[1].split("/")[0].strip()
print(customer2_name, "spent $", customer2_spent)

customer3_spent = receipt3.split("$")[1].split("/")[0].strip()
print(customer3_name, "spent $", customer3_spent)

# 5. Print out what the customer purchased

customer1_purchase = receipt1.split("[")[1].split("]")[0].strip()
print(customer1_name, "purchased", customer1_purchase)

customer2_purchase = receipt2.split("[")[1].split("]")[0].strip()
print(customer2_name, "purchased", customer2_purchase)

customer3_purchase = receipt3.split("[")[1].split("]")[0].strip()
print(customer3_name, "purchased", customer3_purchase)