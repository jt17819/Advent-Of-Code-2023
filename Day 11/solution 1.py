# Solution superseded by solution 2
import numpy as np

with open("Day 11/data.txt", "r") as file:
    raw_data = file.read().split("\n")
data = []
for d in raw_data:
    temp = []
    for l in d:
        temp.append(l)
    data.append(temp)

data = np.array(data)
# print(data)
galaxies = np.where(data == "#")
# print(galaxies)

cols_to_expand = [x for x in range(len(data)-1,-1,-1) if x not in galaxies[1]]
# print(cols_to_expand)
expanded_data = []
for row in data:
    for col in cols_to_expand:
        row = np.insert(row,col,".")
    expanded_data.append(row.tolist())
    if "#" not in row:
        expanded_data.append(row.tolist())
# print(expanded_data)
expanded_data = np.array(expanded_data)

galaxies = np.where(expanded_data == "#")

total = 0
for i in range(len(galaxies[0])):
    y1,x1 = galaxies[0][i],galaxies[1][i]
    for j in range(i,len(galaxies[0])):
        y2,x2 = galaxies[0][j],galaxies[1][j]
        total += abs(x1-x2) + abs(y1-y2)
print(total)