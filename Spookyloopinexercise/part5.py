#!/usr/bin/python3

# Initialize a line count and word count
line_count = 0
word_count = 0

# Open the file in read mode
with open('dracula.txt', 'r') as file:
    # Loop over each line in the file
    for line in file:
        # Check if the word 'vampire' is in the line (ignoring case)
        if 'vampire' in line.lower():
            # Increment the line count
            line_count += 1
            # Increment the word count
            word_count += line.lower().count('vampire')

print('Number of lines with the word vampire:', line_count)
print('Total occurrence of the word vampire:', word_count)

