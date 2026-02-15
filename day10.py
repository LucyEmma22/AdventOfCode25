from itertools import product
from collections import defaultdict 
from ortools.sat.python import cp_model

# Test Input
test_data = ["[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
             "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
             "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"]

# My Input
with open("Documents/AdventOfCode25/input_day10.txt") as f:
    data = f.read().splitlines()

# Part 1
# Function that takes a button configuration, where each button has a value of 1 ('on') or 0 ('off')
# For each indicator, get the number of buttons which affect the indicator and are on 
# Return true if all indicators match their target (where target 0 = even total and target 1 = odd total)
def satisfies(button_config):
    return all(sum(button_config[i] for i in buttons_affecting_indicator) % 2 == indicator_target for buttons_affecting_indicator, indicator_target in constraints) 

best = 0
for i in range(len(data)):                                                     # For each machine...
    indicator_targets = [0 if x == '.' else 1 for x in list(data[i].split()[0].strip('[]'))] # Get the target (1 or 0) for each indicator
    buttons = data[i].split()[1:-1]                                            # Get the buttons and which indicators they affect 
    
    result = defaultdict(list)                                                 # Initialise empty dictionary
    for index, button in enumerate(buttons):                                   # For each button...
        affected_indicators = button.strip("()").split(",")                    # Get the indicators the button affects
        for indicator in affected_indicators:                                  # For each indicator...
            result[indicator].append(index)                                    # Add the index of the button to the list of buttons that affect the indicator in the result dictionary
    buttons_affecting_indicators = [result[k] for k in sorted(result, key=int)]# Sort the dictionary by indicator and extract the buttons affecting each indicator as a list of lists
    
    constraints = list(zip(buttons_affecting_indicators, indicator_targets))   # Create a list of tuples where the first element of each tuple is the buttons affecting an indicator, and the second element is the target of the indicator
    solutions = [button_config for button_config in product([0, 1], repeat = len(buttons)) if satisfies(button_config)] # For every possible button configuration... add it to the solutions if all indicators match their target
    best += sum(min(solutions, key=sum))                                       # Get the number of buttons 'on' for the button configuration with the fewest buttons 'on', and add to the total across all machines
print(best)


# Part 2
def solve_row(constraints):
    model = cp_model.CpModel()                                                 # Create a new constraint programming model
    max_target = max(joltage_target for _, joltage_target in constraints)      # Define the maximum button value (this is equal to the maximum joltage target)
    x = [model.NewIntVar(0, max_target, f"x{i}") for i in range(len(buttons))] # For each button, create a variable representing the possible number of times a button can be pushed (0 - maximum button value)
    for constraint in constraints:                                             # For every constraint (therefore for every joltage target)...
        model.Add(sum(x[i] for i in constraint[0]) == constraint[1])           # Add up the total button pushes for each possible number of times each button in the constraint can be pushed. Keep combinations where this equals the joltage target in the constraint.
    model.Minimize(sum(x))                                                     # Among all possible valid solutions, pick the one where the total number of button presses minimum
    solver = cp_model.CpSolver()                                               # Create the solver
    status = solver.Solve(model)                                               # Solve the model (get the minimum number of button pushes where all constraints are satisfied)
    return sum(solver.Value(v) for v in x)                                     # Add up the number of times each button is pushed 

best = 0
for i in range(len(data)): 
    joltage_targets = [int(x) for x in data[i].split()[-1].strip('{}').split(',')] # Get the target joltage for each counter
    buttons = data[i].split()[1:-1]                                            # Get the buttons and which counters they affect 
    
    result = defaultdict(list)                                                 # Initialise empty dictionary
    for index, button in enumerate(buttons):                                   # For each button...
        affected_indicators = button.strip("()").split(",")                    # Get the indicators the button affects
        for indicator in affected_indicators:                                  # For each indicator...
            result[indicator].append(index)                                    # Add the index of the button to the list of buttons that affect the indicator in the result dictionary
    buttons_affecting_indicators = [result[k] for k in sorted(result, key=int)]# Sort the dictionary by indicator and extract the buttons affecting each indicator as a list of lists
    
    constraints = list(zip(buttons_affecting_indicators, joltage_targets))     # Create a list of tuples where the first element of each tuple is the buttons affecting an indicator, and the second element is the target of the indicator
    best += solve_row(constraints)                                             # Solve for the list of constraints using the function described above

print(best)