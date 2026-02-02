# Packages
import numpy as np
import pandas as pd
from shapely.geometry import Polygon

# Test Input
test_data = ["7,1",
             "11,1",
             "11,7",
             "9,7",
             "9,5",
             "2,5",
             "2,3",
             "7,3"]

# My Input
with open("Documents/AdventOfCode25/input_day9.txt") as f:
    data = f.read().splitlines()
    
# Part 1
coords = np.array([list(map(int, s.split(','))) for s in data], dtype=float)   # Convert list of strings to array of coordinates
diff = np.abs(coords[:, None, :] - coords[None, :, :]) + 1                     # Get the distance between each x and y value and every other x and y value (add 1 so distance includes both points)
product_matrix = diff[:, :, 0] * diff[:, :, 1]                                 # Multiply x and y values to get rectangle area
i, j = np.triu_indices(len(coords), k=1)                                       # Map area to coordinates
df = pd.DataFrame({"point_1": i,
                   "point_2": j,
                   "product": product_matrix[i, j]                             # Create a data frame containing each point and the size of the area formed with every other point
                   }).sort_values("product", ascending=False).reset_index(drop=True) # Sort data frame by area
print(df['product'][0])                                                        # Print the largest area

# Part 2
shape = Polygon(coords)                                                        # Outline of the shape joining all red squares
for i in range(len(df)):                                                       # For each set of points (in order of area)...
    p1 = coords[df['point_1'][i]]
    p2 = coords[df['point_2'][i]]
    x_min, x_max = sorted([p1[0], p2[0]])
    y_min, y_max = sorted([p1[1], p2[1]])
    rect_coords = np.array([[x_min, y_min],
                            [x_min, y_max],
                            [x_max, y_max],
                            [x_max, y_min]])                                   # Coordinates of the rectangle corners
    rect = Polygon(rect_coords)                                                # Outline of the rectangle the points make
    if shape.covers(rect):                                                     # If the rectangle is in the shape, stop looking
        break
print(df['product'][i])                                                        # Print the area of the current rectangle