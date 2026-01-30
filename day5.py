# Packages
import pandas as pd

# Test Input
test_data = ['3-5',
             '10-14',
             '16-20',
             '12-18',
             '',
             '1',
             '5',
             '8',
             '11',
             '17',
             '32']

# My Input
with open("Documents/AdventOfCode25/input_day5.txt") as f:
    data = f.read().splitlines()

# Part 1
fresh_ranges = data[:data.index("")]                                           # Get input before the empty line (fresh food ranges)
starts, ends = zip(*(map(int, x.split("-")) for x in fresh_ranges))            # Split ranges into 2 integers by '-'
available = [int(x) for x in data[data.index("")+1:]]                          # Get input after empty line (available ingredients)
fresh = []
for i in range(len(available)):                                                # For each available ingredient...
    valid_starts = [idx for idx, x in enumerate(starts) if x <= available[i]]  # Find the fresh ingredient ranges that start before the available ingredient (returns a list of positions)
    valid_ends = [idx for idx, x in enumerate(ends) if x >= available[i]]      # Find the fresh ingredient ranges that end after the available ingredient (returns a list of positions)
    if len(set(valid_starts) & set(valid_ends)) > 0:                           # If 1 or more positions appear in both lists, the available ingredient is fresh
        fresh.append(available[i]) 
print(len(fresh))

# Part 2
df = pd.DataFrame(fresh_ranges)                                                # Create a data frame containing the fresh food ranges
df[['start', 'end']] = df[0].str.split('-', expand=True).astype(int)           # Split ranges into 2 integer columns by '-'
df = df.sort_values(by='start').reset_index(drop=True)                         # Sort rows in order of range start
start = df['start'][0]                                                         # Set start as start of the first range
end = df['end'][0]                                                             # Set end as end of the first range
count = 0
for i in range(len(df)):                                                       # For each range...
    if i == len(df)-1:                                                         # If its the last range
        count = count + (end - start + 1)                                      # Add the number of ingredients in the range
    elif df['start'][i+1] <= end and df['end'][i+1] >= end:                    # If the start of the next range is less than the end of the current range and the end of the next range is greater than the end of the current range (i.e. ranges overlap)
        end = df['end'][i+1]                                                   # Update end to be the end of the next range (i.e. join ranges into one)
    elif df['start'][i+1] > end:                                               # If the start of the next range is greater than the end of the current range (i.e. ranges don't overlap)
        count = count + (end - start + 1)                                      # Add the number of ingredients in the range
        start = df['start'][i+1]                                               # Update start to be the start of the next range
        end = df['end'][i+1]                                                   # Update end to be the end of the next range
print(count)