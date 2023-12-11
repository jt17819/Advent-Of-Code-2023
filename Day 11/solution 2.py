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
rows_to_expand = [y for y in range(len(data)-1,-1,-1) if y not in galaxies[0]]

total = 0
expansion = 999999 # num of additional rows and cols
for i in range(len(galaxies[0])):
    y1,x1 = galaxies[0][i],galaxies[1][i]
    for j in range(i,len(galaxies[0])):
        y2,x2 = galaxies[0][j],galaxies[1][j]
        total += abs(x1-x2) + abs(y1-y2)
        for col in cols_to_expand:
            if min(x1,x2) < col and max(x1,x2) > col:
                total += expansion
        for row in rows_to_expand:
            if min(y1,y2) < row and max(y1,y2) > row:
                total += expansion
print(total)