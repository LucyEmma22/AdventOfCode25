# Packages
import pandas as pd
import re
import numpy as np

# Test Input
data = ["123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   + "]

# My Input
with open("Documents/AdventOfCode25/input_day6.txt") as f:
    data = f.read().splitlines()

# Part 1
data1 = [re.sub(r'\s+', ' ', s).strip() for s in data] # Remove extra spaces
df = pd.DataFrame(data1)[0].str.split(" ", expand=True).T # Convert list of strings to dataframe. Split strings into different columns by spaces. Transpose dataframe
numeric_cols = df.iloc[:, :-1].astype(int) # Define numeric columns (not column containing * and +)
df['result'] = np.where(df[4] == '+', numeric_cols.sum(axis=1), numeric_cols.prod(axis=1)) # Create new column with the sum or product of numeric columns (depending on + or *)
print(sum(df['result']))

# Part 2
separator_positions = [i-1 for i, x in enumerate(data[-1]) if x in ('+', '*')][1:] # Determine positions of + or * (this is where the new problem starts)
data2 = [''.join('-' if i in separator_positions else c for i, c in enumerate(x)).split("-") for x in data] # Split strings at the position before + or *
count = 0
for i in range(len(data2[0])):
    col_values = [lst[i] for lst in data2[:-1]] # Get numbers from a single problem
    df = pd.DataFrame([list(str(x)) for x in col_values]).T # Create a dataframe with each number split into seperate columns. Transpose dataframe
    df['number'] = df.astype(str).agg(''.join, axis=1).astype(int) # Add a column that joins the transposed numbers into a single integer
    if "+" in data2[-1][i]:
        count = count + df['number'].sum() # Add sum of numbers if +
    else:
        count = count + df['number'].prod() # Add product of numbers if *
print(count)
