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
fresh_ranges = data[:data.index("")]
starts, ends = zip(*(map(int, x.split("-")) for x in fresh_ranges))
available = [int(x) for x in data[data.index("")+1:]]
fresh = []
for i in range(len(available)):
    valid_starts = [idx for idx, x in enumerate(starts) if x <= available[i]]
    valid_ends = [idx for idx, x in enumerate(ends) if x >= available[i]]
    if len(set(valid_starts) & set(valid_ends)) > 0:
        fresh.append(available[i])
print(len(fresh))

# Part 2
df = pd.DataFrame(fresh_ranges)
df[['start', 'end']] = df[0].str.split('-', expand=True).astype(int)
df = df.sort_values(by='start').reset_index(drop=True)
start = df['start'][0]
end = df['end'][0]
count = 0
for i in range(len(df)):
    if i == len(df)-1:
        count = count + (end - start + 1)
    elif df['start'][i+1] <= end and df['end'][i+1] >= end:
        end = df['end'][i+1]
    elif df['start'][i+1] > end:
        count = count + (end - start + 1)
        start = df['start'][i+1]
        end = df['end'][i+1]
print(count)