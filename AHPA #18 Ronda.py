# Task 1: Function sanitize
def sanitize(time_string):
    if "-" in time_string:
        return time_string.replace("-", ".")
    elif ":" in time_string:
        return time_string.replace(":", ".")
    return time_string

# Task 2: Read and process the data

file = open("AHPA #18 - Rousey Data.txt", "r")
fights = []
for line in file:
    data = line.strip().split(",") 
    opponent, method, round_num, total_time = data
    sanitized_time = float(sanitize(total_time)) 
    fights.append((sanitized_time, opponent, method, round_num))

file.close()

# Task 3: Filter, Sort, and Output the Top 3 Fastest Wins

fights.sort()  

top_3_fastest = fights[:3]  
for sanitized_time, opponent, method, round_num in top_3_fastest:
    print("Opponent: {0}, Method: {1}, Round: {2}, Time: {3}".format(opponent, method, round_num, sanitized_time))
