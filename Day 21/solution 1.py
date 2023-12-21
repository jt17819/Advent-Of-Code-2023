import numpy as np


def move(grid, points, marker):
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    new_points = []
    for point in points:
        for m in moves:
            y,x = point[0] + m[0], point[1] + m[1]
            if grid[y][x] == "." or grid[y][x] == "S":
                grid[y][x] = marker
                new_points.append((y,x))
    return grid, new_points

with open("Day 21/data.txt", "r") as file:
    data = file.read().split("\n")

for i, line in enumerate(data):
    data[i] = [char for char in line]

data = np.array(data)

start = np.where(data=="S")

open_points = [(start[0][0], start[1][0])]
# print(open_points)

for i in range(64):

    data, open_points = move(data, open_points, (i+1)%2)
    # print(data,open_points)
print(np.count_nonzero(data=="0"))