# Packages
import pandas as pd

# Test Input
test_data = pd.DataFrame({0:["L68",
                             "L30",
                             "R48",
                             "L5",
                             "R60",
                             "L55",
                             "L1",
                             "L99",
                             "R14",
                             "L82"]})
                      
# My Input
data = pd.read_csv("Documents/AdventOfCode25/input_day1.txt", header=None)

# Part 1
position = 50                                                                  # Start at position 50
count = 0
for i in range(len(data)):
    direction = data[0].str[0][i]                                              # Get the direction
    distance = data[0].str[1:].astype(int)[i] % 100                            # Get the distance (keep only the last 2 digits as a distance of 100 ends in the same position)
    if direction == "R":
        position = position + distance                                         # If the direction is right, add the distance to the current position
        if position > 99:                                                      # If thre result is greater than 99...
            position = position - 100                                          # Take 100 from the result to get the actual position (since this means it has done a full rotation and has crossed 0 forwards)
    else:
        position = position - distance                                         # If the direction is right, take the distance away from the current position
        if position < 0:                                                       # If thre result is less than 0...
            position = 100 + position                                          # Add 100 to the result to get the actual position (since this means it has done a full rotation and has crossed 0 backwards)
    if position == 0:                                                          # If it lands on 0, add 1 to the count
        count = count + 1
print(count)

# Part 2
position = 50                                                                  # Start at position 50
count = 0
for i in range(len(data)):
    direction = data[0].str[0][i]                                              # Get the direction
    distance = data[0].str[1:].astype(int)[i] % 100                            # Get the distance (keep only the last 2 digits as a distance of 100 ends in the same position)
    count = count + data[0].str[1:].astype(int)[i] // 100                      # If the distance is more than 100, add the number of times is passes 0 to the count
    prev_position = position
    if direction == "R":
        position = position + distance                                         # If the direction is right, add the distance to the current position
        if position > 99:                                                      # If thre result is greater than 99...
            position = position - 100                                          # Take 100 from the result to get the actual position (since this means it has done a full rotation and has crossed 0 forwards)
            if prev_position != 0 and position !=0:                            # If the dial did not start or end exactly on 0, add 1 to the count
                count = count + 1
    else:
        position = position - distance                                         # If the direction is right, take the distance away from the current position
        if position < 0:                                                       # If thre result is less than 0...
            position = 100 + position                                          # Add 100 to the result to get the actual position (since this means it has done a full rotation and has crossed 0 backwards)
            if prev_position != 0 and position != 0:                           # If the dial did not start or end exactly on 0, add 1 to the count
                count = count + 1
    if position == 0:                                                          # If it lands exactly on 0, add 1 to the count
        count = count + 1 
print(count)