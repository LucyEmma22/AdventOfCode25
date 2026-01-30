# Packages
import re

# Test Input
test_data = ['11-22',
             '95-115',
             '998-1012',
             '1188511880-1188511890',
             '222220-222224',
             '1698522-1698528',
             '446443-446449',
             '38593856-38593862',
             '565653-565659',
             '824824821-824824827',
             '2121212118-2121212124']
        
# My Input
with open("Documents/AdventOfCode25/input_day2.txt") as f:
    data = [x.strip() for x in f.read().split(",")]
  
# Functions
def sum_invalid(data, pattern):
    invalid = []
    for j in range(len(data)):
        start, end = data[j].split("-")                                        # Seperate the start and end of the range
        for i in range(int(start), int(end) + 1):                              # For each number in the range...
            if(bool(re.fullmatch(pattern, str(i)))):                           # Check if it contains the pattern
                invalid.append(i)                                              # If it does, add to the list of invalid numbers 
    return(sum(invalid))
    
# Part 1
print(sum_invalid(data, r'(\d+)\1'))                                           # Run function where pattern is a sequence repeated exactly twice

# Part 2
print(sum_invalid(data, r'(\d+)\1+'))                                          # Run function where pattern is a sequence repeated more than once