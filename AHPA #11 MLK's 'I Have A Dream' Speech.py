# AHPA #11: MLK's "I Have A Dream" Speech
# Student Name: Linh Nguyen

# 1. Print the total number of characters in the speech.

file = open("MLK Speech.txt","r")
count = 0
lines = file.readlines() 
file.close()
for line in lines:
  temp = line.replace(" ", "").replace("\n","")
  for c in temp:
    count += 1
print(count)

# 2. Open another file for output.

outfile = open("MLK Speech_first paragraph.txt", "w")

# 3. Write only the first paragraph of this speech to that file.

first_pararaph = ""
for line in lines:
  if line.strip() == "":
    break
  first_pararaph += line

outfile.write(first_pararaph)
outfile.close()