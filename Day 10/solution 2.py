# import numpy as np


def move(data, direction, pos):
    dirs = {"north":[-1,0], "south":[1,0], "east":[0,1], "west":[0,-1]}
    pipe = ""
    steps = 0

    while pipe != "S":
        if direction == "north" and pipe in north_movement:
            # data[pos[0]][pos[1]] = "^" if pipe == "|" else "S"
            direction = north_movement[pipe]
        elif direction == "east" and pipe in east_movement:
            # data[pos[0]][pos[1]] = "/" if pipe == "-" else "S"
            direction = east_movement[pipe]
        elif direction == "south" and pipe in south_movement:
            # data[pos[0]][pos[1]] = "^" if pipe == "|" else "S"
            direction = south_movement[pipe]
        elif direction == "west" and pipe in west_movement:
            # data[pos[0]][pos[1]] = "/" if pipe == "-" else "S"
            direction = west_movement[pipe]
        pos[0], pos[1] = pos[0] + dirs[direction][0], pos[1] + dirs[direction][1]
        # print(pos)
        pipe = data[pos[0]][pos[1]]
        steps += 1
        memo.append(pos[:])

    return steps // 2, direction


with open("Day 10/data.txt","r") as file:
    data = file.read().split("\n")
new_data = []
for d in data:
    temp = []
    for l in d:
        temp.append(l)
    new_data.append(temp)
data = new_data
# print(data)

for i, row in enumerate(data):
    if "S" in row:
        pos = [i, row.index("S")]

print(pos)

north_movement = {"|":"north", "7":"west",  "F":"east"}
east_movement  = {"-":"east",  "J":"north", "7":"south"}
south_movement = {"|":"south", "L":"east",  "J":"west"}
west_movement  = {"-":"west",  "L":"north", "F":"south"}
memo = []

# print(move(data, "east", pos))
dirs_map = {"north":{v:k for k,v in north_movement.items()}, "south":{v:k for k,v in south_movement.items()}, 
            "east":{v:k for k,v in east_movement.items()}, "west":{v:k for k,v in west_movement.items()}}

if data[pos[0]-1][pos[1]] in north_movement:
    steps, dir = move(data, "north", pos)
    data[pos[0]][pos[1]] = dirs_map[dir]["north"]

elif data[pos[0]][pos[1]+1] in east_movement:
    steps, dir = move(data, "east", pos)
    data[pos[0]][pos[1]] = dirs_map[dir]["east"]

elif data[pos[0]+1][pos[1]-1] in south_movement:
    steps, dir = move(data, "south", pos)
    data[pos[0]][pos[1]] = dirs_map[dir]["south"]

elif data[pos[0]][pos[1]-1] in west_movement:
    steps, dir = move(data, "west", pos)
    data[pos[0]][pos[1]] = dirs_map[dir]["west"]
print(steps)

# with open("Day 10/pipe.txt","w") as file:
#     file.write("\n".join(["".join(line)for line in data]))

total = 0
flip_map = {"F":"J","L":"7"}
cont_map = {"F":"7","L":"J"}

inside = False
flip = False
i = 0
# temp = np.zeros_like(data)
for line in data:
    j = 0
    for pipe in line:
        if [i,j] in memo and pipe in flip_map:
            flip = flip_map[pipe]
            cont = cont_map[pipe]
        if ([i,j] in memo and pipe == flip) or ([i,j] in memo and pipe == "|"):
            inside = not inside
        if inside and [i,j] not in memo:
            # temp[i,j] = "I"
            total += 1
        # else:
        #     temp[i,j] = "0"
        j += 1
    i += 1

print(total)
# # print(temp)
# with open("Day 10/pipe.txt","w") as file:
#     file.write("\n".join(["".join(line)for line in temp]))