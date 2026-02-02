# Packages
import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist

# Test Input
test_data = ["162,817,812",
             "57,618,57",
             "906,360,560",
             "592,479,940",
             "352,342,300",
             "466,668,158",
             "542,29,236",
             "431,825,988",
             "739,650,466",
             "52,470,668",
             "216,146,977",
             "819,987,18",
             "117,168,530",
             "805,96,715",
             "346,949,466",
             "970,615,88",
             "941,993,340",
             "862,61,35",
             "984,92,344",
             "425,690,689"]

# My Input
with open("Documents/AdventOfCode25/input_day8.txt") as f:
    data = f.read().splitlines()

# Part 1
coords = np.array([list(map(int, s.split(','))) for s in data], dtype=float)   # Convert list of strings to array of coordinates
dists = pdist(coords)                                                          # Calculate the distance between each point and every other point
i, j = np.triu_indices(len(coords), k=1)                                       # Get the points corresponding to the above distances
df = pd.DataFrame({"point_1": i,
                   "point_2": j,
                   "distance": dists
                   }).sort_values("distance", ignore_index=True)               # Create a dataframe with each point and its distance to ever other point, sorted by distance
circuits = [] 
i = 0
while i < 1000:                                                                # Run until 1000 connections have been made
    p1, p2 = df['point_1'][i], df['point_2'][i]
    containing_circuits = [c for c in circuits if p1 in c or p2 in c]          # Find which existing circuits contain p1 or p2
    if not containing_circuits:                                                # If neither point is in a circuit...
        circuits.append(set([p1, p2]))                                         # Create new circuit
    elif len(containing_circuits) == 1:                                        # If one point is already in a circuit but the other point is not...
        containing_circuits[0].update([p1, p2])                                # Add the other point to that circuit. If they are both in the same circuit this does nothing
    else:                                                                      # If both points are in different circuits...
        new_circuit = set().union(*containing_circuits)                        # Merge the circuits
        circuits = [c for c in circuits if c not in containing_circuits]       # Remove the two unmerged circuits
        circuits.append(new_circuit)                                           # Add the new merged circuit
    i += 1

product = 1
for x in sorted(circuits, key=len, reverse=True)[:3]:                          # Get the three longest circuits
    product = product * len(x)                                                 # Multiply their lengths
print(product)

# Part 2
circuits = [] 
i=0
max_circuit = 0
while max_circuit < len(coords):                                               # Run until there is one circuit containing all points
    p1, p2 = df['point_1'][i], df['point_2'][i]
    containing_circuits = [c for c in circuits if p1 in c or p2 in c]          # Find which existing circuits contain p1 or p2
    if not containing_circuits:                                                # If neither point is in a circuit...
        circuits.append(set([p1, p2]))                                         # Create new circuit
    elif len(containing_circuits) == 1:                                        # If one point is already in a circuit but the other point is not...
        containing_circuits[0].update([p1, p2])                                # Add the other point to that circuit. If they are both in the same circuit this does nothing
    else:                                                                      # If both points are in different circuits...
        new_circuit = set().union(*containing_circuits)                        # Merge the circuits
        circuits = [c for c in circuits if c not in containing_circuits]       # Remove the two unmerged circuits
        circuits.append(new_circuit)                                           # Add the new merged circuit
    i += 1
    max_circuit = max(len(x) for x in circuits)                                # Calculate the length of the longest circuit

print(coords[p1][0] * coords[p2][0])                                           # Multiply the x coordinate of the last 2 points