def move(data, direction, pos):
    dirs = {"north":[-1,0], "south":[1,0], "east":[0,1], "west":[0,-1]}
    pipe = ""
    steps = 0

    while pipe != "S":
        if direction == "north" and pipe in north_movement:
            direction = north_movement[pipe]

        elif direction == "east" and pipe in east_movement:
            direction = east_movement[pipe]

        elif direction == "south" and pipe in south_movement:
            direction = south_movement[pipe]

        elif direction == "west" and pipe in west_movement:
            direction = west_movement[pipe]

        pos[0], pos[1] = pos[0] + dirs[direction][0], pos[1] + dirs[direction][1]
        pipe = data[pos[0]][pos[1]]
        steps += 1

    return steps // 2


with open("Day 10/data.txt","r") as file:
    data = file.read().split("\n")
# print(data)

for i, row in enumerate(data):
    if "S" in row:
        pos = [i, row.index("S")]

print(pos)

north_movement = {"|":"north", "7":"west",  "F":"east"}
east_movement  = {"-":"east",  "J":"north", "7":"south"}
south_movement = {"|":"south", "L":"east",  "J":"west"}
west_movement  = {"-":"west",  "L":"north", "F":"south"}

# memo = []

if data[pos[0]-1][pos[1]] in north_movement:
    print(move(data, "north", pos))

elif data[pos[0]][pos[1]+1] in east_movement:
    print(move(data, "east", pos))

elif data[pos[0]+1][pos[1]-1] in south_movement:
    print(move(data, "south", pos))

elif data[pos[0]][pos[1]-1] in west_movement:
    print(move(data, "west", pos))
