def area(corners):
    n = len(corners) # of corners
    area = 0
    perimeter = 0
    for i in range(n):
        j = (i + 1) % n
        area += ((corners[i][0])) * (corners[j][1])
        area -= (corners[j][0]) * (corners[i][1])
        perimeter += abs(corners[i][0] - corners[j][0]) + abs((corners[i][1]) - (corners[j][1]))
    area = abs(area)
    total_area = area + perimeter
    return total_area // 2 + 1


with open("Day 18/data.txt", "r") as file:
    data = file.read().split("\n")

# print(data)

directions = {"U":(-1,0),"D":(1,0),"L":(0,-1),"R":(0,1)}
verticies = [(0,0)]
for line in data:
    direction, count, colour = line.split(" ")
    new_y = verticies[-1][0] + directions[direction][0] * int(count)
    new_x = verticies[-1][1] + directions[direction][1] * int(count)
    verticies.append((new_y, new_x))

print(area(verticies))