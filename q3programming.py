'''
File name: q3programming.py
Author: Henry Libman
Date: 10/22/2020
Python Version: 3.8.5
'''

import re

# Open the file to read from
file = open('./output.txt', 'rt')
# Read from file
file_contents = file.read()

# Define and initialize all the output variables
file_name = file.name
num_lines = 0
num_chars = len(file_contents)
num_letters = 0
num_figures = 0
num_other = 0
num_words = 0
num_lengths = {}

# Iterate through each character in the file
for char in file_contents:
    # If the character is a letter, increment the number of letters
    if char.isalpha():
        num_letters += 1
    # If the character is a figure, increment the number of figures
    elif char.isdigit():
        num_figures += 1
    # If the character is something else, incrememnt the number of other characters
    else:
        num_other += 1

# Break file into a list of lines
lines = file_contents.split("\n")

# Iterate through every line
for line in lines:
    # Increment the number of lines
    if line:
        num_lines += 1
    # Break each line into list of words
    words  = line.split(" ")
    # Iterate through each word in the line
    for word in words:
        # Remove punctuation from each word
        word = re.sub(r"[^\w\s]", "", word)
        # Increment the number of words
        if word:
            num_words += 1
        # Check if a word of that length is not in the dictionary already
        if not len(word) in num_lengths and word.isalnum():
            # Add the length of word to the dictionary with a count of 1
            num_lengths[len(word)] = 1
        elif word.isalnum():
            # Increment count of that length of word by 1
            num_lengths[len(word)] += 1

# Print out all the totals
print("File name: " + file_name)
print("Number of lines: " + str(num_lines))
print("Number of chars(total): " + str(num_chars))
print("Number of letters: " + str(num_letters))
print("Number of figures: " + str(num_figures))
print("Number of other characters: " + str(num_other))
print("Number of words: " + str(num_words))
# Sort the keys in the dictionary and print out the number of occurences of each length of word
for num in sorted(num_lengths.keys()):
    print("Number of " + str(num) + " letter words: " + str(num_lengths[num]))


