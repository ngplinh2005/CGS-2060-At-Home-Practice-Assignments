# AHPA #23 - The Boss' Request.py
#
# Cra-Z-Art has data on their CRA-Z-Slimy Stitch Slime Toy sales for the past 
# 12 months. They would like you to create a line graph that shows how their 
# sales have varied.
# Data: 220,000; 315,000; 375,000; 410,000; 435,000; 445,000; 505,000; 527,000; #535,000; 650,000; 785,000; 992,000
#
# The red and blue versions of the CRA-Z-Slimy Stitch Slime Toy have sold # differently for the past four months, the boss would like to see a bar chart 
# comparing these sales.
# Red: 10,000, 17,000, 29,000, 36,000
# Blue: 15,000, 22,000, 35,000, 47,000
#
# Each of the company's four regions, North, South, East, and West have sales. 
# The boss would like to see a pie chart of these sales with the West region 
# broken out.
# Norh: 543,000
# South: 732,000
# East: 902,000
# West: 826,000
#
# Student Name: Linh Nguyen
#

import matplotlib.pyplot as plt

# Line Graph: Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthly_sales = [220000, 315000, 375000, 410000, 435000, 445000, 505000, 527000, 535000, 650000, 785000, 992000]

plt.figure(figsize=(8, 5))
plt.plot(months, monthly_sales, marker='o', linestyle='-', color='b')
plt.title("Monthly Sales Data for CRA-Z-Slimy Stitch Slime Toy")
plt.xlabel("Month")
plt.ylabel("Sales (in USD)")
plt.grid()
plt.show()

# Bar Chart: Sales comparison for Red and Blue variants
categories = ["Month 1", "Month 2", "Month 3", "Month 4"]
red_sales = [10000, 17000, 29000, 36000]
blue_sales = [15000, 22000, 35000, 47000]

plt.figure(figsize=(8, 5))
bar_width = 0.4
x_indexes = range(len(categories))

plt.bar(x_indexes, red_sales, width=bar_width, label="Red", color="red")
plt.bar([x + bar_width for x in x_indexes], blue_sales, width=bar_width, label="Blue", color="blue")
plt.xticks(ticks=[x + bar_width / 2 for x in x_indexes], labels=categories)
plt.title("Sales Comparison: Red vs Blue Variants")
plt.xlabel("Months")
plt.ylabel("Sales (in USD)")
plt.legend()
plt.show()

# Pie Chart: Regional sales data
regions = ["North", "South", "East", "West"]
regional_sales = [543000, 732000, 902000, 826000]
explode = [0, 0, 0, 0.1]  # make the West region broken out

plt.figure(figsize=(6, 6))
plt.pie(regional_sales, labels=regions, explode=explode, autopct="%1.1f%%", startangle=140)
plt.title("Sales Distribution by Region")
plt.show()