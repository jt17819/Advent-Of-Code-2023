import numpy as np
# import matplotlib.pyplot as plt


def move(grid, points, marker):
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    new_points = []
    for point in points:
        for m in moves:
            y,x = point[0] + m[0], point[1] + m[1]
            if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
                if grid[y][x] == "." or grid[y][x] == "S":
                    grid[y][x] = marker
                    new_points.append((y,x))
    return grid, new_points

with open("Day 21/data.txt", "r") as file:
    data = file.read().split("\n")

for i, line in enumerate(data):
    data[i] = [char for char in line] * 7

new_data = []
for _ in range(7):
    new_data.extend(data)

data = np.array(new_data) #,dtype="<U8")
start = np.where(data=="S")
idx = len(start[0]) // 2
data = np.char.replace(data, "S", ".") #.astype("<U8")

# with open("Day 21/temp.txt","w") as file:
#     file.write("\n".join(["".join(line)for line in data]))

open_points = [(start[0][idx], start[1][idx])]

growth = []
data_points = (65,196,327)
for i in range(328):
# i = 0
# while open_points:
    # i += 1
    data, open_points = move(data, open_points, (i+1)%2)
    if i in data_points:
        growth.append(np.count_nonzero(data==str(i%2)))
    # print(i,open_points)
# print(np.count_nonzero(data=="0"))

# with open("Day 21/temp2.txt","w") as file:
#     file.write("\n".join(["".join(line)for line in data]))

# data = np.char.replace(data, "0", "T")
# data = np.char.replace(data, "1", "0")
# data = np.char.replace(data, "T", "1")

# with open("Day 21/temp3.txt","w") as file:
#     file.write("\n".join([" ".join(line)for line in data]))

x = np.arange(len(growth))
y = np.array(growth,dtype=np.int32)
# plt.plot(x,y)
# plt.show()

poly_coeffs = np.polyfit(x,y,2)

ans = np.polyval(poly_coeffs, (26501365 - 65) // 131)
print(np.ceil(ans).astype(np.int64))