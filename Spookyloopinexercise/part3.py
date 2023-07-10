#!/usr/bin/python3

# Open the file in read mode
with open('dracula.txt', 'r') as file:
    # Loop over each line in the file
    for line in file:
        # Check if the word 'vampire' is in the line
        if 'vampire' in line:
            # Print the line
            print(line)

