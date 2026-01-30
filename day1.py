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
position = 50
count = 0
positions = []
for i in range(len(data)):
    direction = data[0].str[0][i]
    distance = data[0].str[1:].astype(int)[i] % 100
    if direction == "R":
        position = position + distance
        if position > 99:
            position = position - 100
    else:
        position = position - distance
        if position < 0:
            position = 100 + position
    if position == 0:
        count = count + 1
    positions.append(position)
print(count)

# Part 2
position = 50
count = 0
counts = []
positions = []
for i in range(len(data)):
    direction = data[0].str[0][i]
    distance = data[0].str[1:].astype(int)[i] % 100
    count = count + data[0].str[1:].astype(int)[i] // 100
    prev_position = position
    if direction == "R":
        position = position + distance
        if position > 99:
            position = position - 100
            if prev_position != 0 and position !=0:
                count = count + 1
    else:
        position = position - distance
        if position < 0:
            position = 100 + position
            if prev_position != 0 and position != 0:
                count = count + 1
    if position == 0:
        count = count + 1
    positions.append(position)
    counts.append(count)
print(count)