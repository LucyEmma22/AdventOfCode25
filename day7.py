# Packages
import numpy as np

# Test Input
test_data = [".......S.......",
             "...............",
             ".......^.......",
             "...............",
             "......^.^......",
             "...............",
             ".....^.^.^.....",
             "...............",
             "....^.^...^....",
             "...............",
             "...^.^...^.^...",
             "...............",
             "..^...^.....^..",
             "...............",
             ".^.^.^.^.^...^.",
             "..............."]

# My Input
with open("Documents/AdventOfCode25/input_day7.txt") as f:
    data = f.read().splitlines()

# Part 1
matrix = np.array([list(row) for row in data])                                 # Convert data to a matrix
matrix[matrix == 'S'] = '|'                                                    # Replace S with |
for i in range(1, matrix.shape[0]):                                            # For each row (from second row)
    for j in range(matrix.shape[1]):                                           # For each column
        if matrix[i, j] == '.' and matrix[i-1, j] == '|':                      # If position is empty and there is a beam above...
            matrix[i, j] = '|'                                                 # Put beam in position
        if matrix[i, j] == '^' and matrix[i-1, j] == '|':                      # If position contains a splitter and there is a beam above...
            matrix[i, j-1] = '|'                                               # Put beam to left of position
            matrix[i, j+1] = '|'                                               # Put beam to right of position         
above = matrix[:-1, :]                                                         # Matrix without the last row (rows above)
below = matrix[1:, :]                                                          # Matrix without the first row (rows below)
count = np.sum((above == '|') & (below == '^'))                                # Count the number of occurrences where | is above ^
print(count)    

# Part 2
matrix = np.array([[1 if c == 'S' else 0 if c == '.' else np.nan for c in row] for row in data], dtype=float) # Convert data to numeric matrix (S=1, .=0, ^=np.nan)                                  
for i in range(1, matrix.shape[0]):                                            # For each row (from second row)
    for j in range(matrix.shape[1]):                                           # For each column                                        
        if ~np.isnan(matrix[i, j]) and matrix[i-1, j] > 0:                     # If the position is not a splitter and the position above contains a beam...          
            matrix[i, j] = matrix[i, j] + matrix[i-1, j]                       # Add the number of beams in the position above to the number of beams in that position            
        if np.isnan(matrix[i, j]) and matrix[i-1, j] > 0:                      # If the position is a splitter and the position above contains a beam...
            matrix[i, j-1] = (matrix[i, j-1] + matrix[i-1, j])                 # Add the number of beams in the position above to the splitter to the number of beams in the position left of the splitter                    
            matrix[i, j+1] = (matrix[i, j+1] + matrix[i-1, j])                 # Add the number of beams in the position above to the splitter to the number of beams in the position right of the splitter                                                
print(np.sum(matrix[-1]))                                                      # Add together the total number of beams in the last row of the matrix