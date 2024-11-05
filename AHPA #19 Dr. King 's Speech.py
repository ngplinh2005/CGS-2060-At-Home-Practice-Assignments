# AHPA #19: Dr. King's Speech
#
# 1. Using sets I want you to calculate how many unique words there are in Dr. King's "I Have A Dream" speech.
#
# 2. Using sets I want you to calculate how many unique words there are in Dr. King's "Letter From the Birmingham City Jail" text.
#
# 3. Next, I'd like to know how many of the words in the "I have a dream speech" were also used in the "Letter From the Birmingham City Jail" text (count).
#
# 4. Now tell me what words that were used in the "I have a dream" speech were NOT used in the "Letter From the Birmingham City Jail" text (list).
#
# Student Name: Linh Nguyen

# Function to process files
def process_text(file):
    word_set = set()
    for line in file:
        lower_line = line.lower()
        stripped_line = lower_line.strip(".,\n")
        list_line = stripped_line.split() 
        word_set.update(list_line)    
    return word_set

# Open files
file_dream = open("AHPA #19 Dr. King's Speech.txt", "r")
file_letter = open("AHPA #19 Letter From the Birmingham City Jail Speech.txt", "r")

# Process files
dream_words = process_text(file_dream)
letter_words = process_text(file_letter)

# Close files
file_dream.close()
file_letter.close()

# Task 1 and 2: Count the number of unique words in each speech
unique_dream_words_count = len(dream_words)
unique_letter_words_count = len(letter_words)

# Task 3: Count common words
common_words = dream_words & letter_words

# Task 4: List out all unique words
unique_to_dream = dream_words - letter_words

# Print the results
print("Unique words in 'I Have a Dream':", unique_dream_words_count)
print("Unique words in 'Letter from Birmingham Jail':", unique_letter_words_count)
print("Common words between the two texts:", len(common_words))
print("Words in 'I Have a Dream' not in 'Letter from Birmingham Jail':", sorted(unique_to_dream))