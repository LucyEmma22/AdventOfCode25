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
for i in range(len(data)):                                                     # For each string in the list (i.e. each pack)...
    nums = [int(ch) for ch in data[i]]                                         # Create a list of integers from the string
    digit1 = max(nums[:-1])                                                    # Get the maximum integer that is not in the last position
    pos = nums.index(digit1)                                                   # Get the position of that integer
    digit2 = max(nums[pos+1:])                                                 # Get the maximum integer after that position
    joltage = digit1*10 + digit2                                               # Join the digits to get the joltage
    total_joltage = total_joltage + joltage                                    # Add to total joltage
print(total_joltage)

# Part 2
total_joltage = 0
for i in range(len(data)):                                                     # For each string in the list (i.e. each pack)...
    nums = [int(ch) for ch in data[i]]                                         # Create a list of integers from the string
    digits = []
    for j in range(12):                                                        # Repeat the following 12 times for 12 digits
        if j != 11: 
            digit = max(nums[:j-11])                                           # If j is not 11, get the maximum integer excluding the last j-11 integers
        else:
            digit = max(nums)                                                  # If j is 11 get the maximum integer 
        digits.append(digit)                                                   # Add the integer to the list of digits
        pos = nums.index(digit)                                                # Get the position of the integer
        nums = nums[pos+1:]                                                    # Remove all integers before this position
    joltage = 0
    for d in digits:
        joltage = joltage * 10 + d                                             # Join the digits to get the joltage
    total_joltage = total_joltage + joltage                                    # Add to total joltage
print(total_joltage)