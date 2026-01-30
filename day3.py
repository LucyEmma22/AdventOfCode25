# Test Input
test_data = ['987654321111111',
             '811111111111119',
             '234234234234278',
             '818181911112111']

# My Input
with open("Documents/AdventOfCode25/input_day3.txt") as f:
    data = f.read().splitlines()
    
# Part 1
total_joltage = 0
for i in range(len(data)):
    nums = [int(ch) for ch in data[i]]
    digit1 = max(nums[:-1])
    pos = nums.index(digit1)
    digit2 = max(nums[pos+1:])
    joltage = digit1*10 + digit2
    total_joltage = total_joltage + joltage
print(total_joltage)

# Part 2
total_joltage = 0
for i in range(len(data)):
    nums = [int(ch) for ch in data[i]]
    digits = []
    for j in range(12):
        if j != 11:
            digit = max(nums[:j-11])
        else:
            digit = max(nums)
        digits.append(digit)
        pos = nums.index(digit)
        nums = nums[pos+1:]
    joltage = 0
    for d in digits:
        joltage = joltage * 10 + d
    total_joltage = total_joltage + joltage
print(total_joltage)