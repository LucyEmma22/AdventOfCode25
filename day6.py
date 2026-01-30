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
data1 = [re.sub(r'\s+', ' ', s).strip() for s in data]
df = pd.DataFrame(data1)[0].str.split(" ", expand=True).T
numeric_cols = df.iloc[:, :-1].astype(int)
df['result'] = np.where(df[4] == '+', numeric_cols.sum(axis=1), numeric_cols.prod(axis=1))
print(sum(df['result']))

# Part 2
separator_positions = [i-1 for i, x in enumerate(data[-1]) if x in ('+', '*')][1:]
data2 = [''.join('-' if i in separator_positions else c for i, c in enumerate(x)) for x in data]
data2 = [x.split("-") for x in data2]
count = 0
for i in range(len(data2[0])):
    df = pd.DataFrame(pd.DataFrame([lst[i] for lst in data2[:-1]])[0].astype(str).apply(list).tolist()).T
    df['number'] = df.astype(str).agg(''.join, axis=1).astype(int)
    if "+" in data2[-1][i]:
        count = count + df['number'].sum()
    else:
        count = count + df['number'].prod()
print(count)
