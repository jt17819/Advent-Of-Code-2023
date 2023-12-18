def area(corners):
    n = len(corners) # of corners
    area = 0
    perimeter = 0
    for i in range(n):
        j = (i + 1) % n
        area += ((corners[i][0])) * (corners[j][1])
        area -= (corners[j][0]) * (corners[i][1])
        # print(corners[i],corners[j])
        perimeter += abs(corners[i][0] - corners[j][0]) + abs((corners[i][1]) - (corners[j][1]))
        # print(perimeter)
    area = abs(area)
    total_area = area + perimeter
    return total_area // 2 + 1


with open("Day 18/data.txt", "r") as file:
    data = file.read().split("\n")

# print(data)

directions = {"3":(-1,0),"1":(1,0),"2":(0,-1),"0":(0,1)}
verticies = [(0,0)]
for line in data:
    direction, count, colour = line.split(" ")
    direction, count = colour.strip("()")[-1],colour.strip("(#)")[:-1]
    # print(direction, count, colour)
    new_y = verticies[-1][0] + directions[direction][0] * int(count,16)
    new_x = verticies[-1][1] + directions[direction][1] * int(count,16)
    verticies.append((new_y, new_x))
# print(verticies)
print(area(verticies))