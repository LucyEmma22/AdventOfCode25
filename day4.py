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
matrix = np.array([list(row) for row in data])
grid = (matrix == '@').astype(int)
kernel = np.array([[1,1,1],
                   [1,0,1],
                   [1,1,1]])

# Part 1
neighbor_counts = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
condition = (neighbor_counts < 4) & (grid == 1)
num = np.sum(condition)
print(num)

# Part 2
total = 0
num = 1
while num > 0:
    neighbor_counts = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
    condition = (neighbor_counts < 4) & (grid == 1)
    num = np.sum(condition)
    grid = np.where((grid == 1) & (condition == 1), 0, grid)
    total = num + total
print(total)
