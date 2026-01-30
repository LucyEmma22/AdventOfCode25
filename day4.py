# Packages
import numpy as np
from scipy.signal import convolve2d

# Test Input
test_data = ['..@@.@@@@.',
             '@@@.@.@.@@',
             '@@@@@.@.@@',
             '@.@@@@..@.',
             '@@.@@@@.@@',
             '.@@@@@@@.@',
             '.@.@.@.@@@',
             '@.@@@.@@@@',
             '.@@@@@@@@.',
             '@.@.@@@.@.']

# My Input
with open("Documents/AdventOfCode25input_day4.txt") as f:
    data = f.read().splitlines()
    
# Prep data
matrix = np.array([list(row) for row in data])                                 # Convert list of strings to a matrix
grid = (matrix == '@').astype(int)                                             # Convert @ to 1 and . to 0
kernel = np.array([[1,1,1],
                   [1,0,1],
                   [1,1,1]])                                                   # Define pattern to search for

# Part 1
neighbor_counts = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0) # Get the number of 1's adjacent to each 1 and 0's adjacent to each 0
condition = (neighbor_counts < 4) & (grid == 1)                                # Define positions where neighbor_counts is less than 4 and grid is 1 (i.e. @ with less than 4 adjacent @'s)
num = np.sum(condition)                                                        # Add them up
print(num)

# Part 2
total = 0
num = 1
while num > 0:                                                                 # While there are still rolls being removed...
    neighbor_counts = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0) # Get the number of 1's adjacent to each 1 and 0's adjacent to each 0
    condition = (neighbor_counts < 4) & (grid == 1)                            # Define positions where neighbor_counts is less than 4 and grid is 1 (i.e. @ with less than 4 adjacent @'s)
    total = total + np.sum(condition)                                          # Add them to the total 
    grid = np.where((grid == 1) & (condition == 1), 0, grid)                   # Replace 1 for 0 where condition is 1 (i.e. where a roll has been removed)
print(total)
