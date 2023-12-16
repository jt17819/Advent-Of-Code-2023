# def move(layout, position, direction):
#     if (position, direction) in memo:
#         return
#     # directions [(1,0),(-1,0),(0,1),(0,-1)]
#     memo.append((position,direction))

#     new_pos = (position[0] + direction[0], position[1] + direction[1])
#     if new_pos[0] < 0 or new_pos[0] >= len(layout) or new_pos[1] < 0 or new_pos[1] >= len(layout[0]):
#         return
#     space = layout[new_pos[0]][new_pos[1]]
    
#     if space == ".":
#         move(layout, new_pos, direction)
#     elif space == "/":
#         reflections = {"10":(0,-1), "-10":(0,1), "01":(-1,0), "0-1":(1,0)}
#         move(layout, new_pos, reflections["".join([str(d) for d in direction])])
#     elif space == "\\":
#         reflections = {"10":(0,1), "-10":(0,-1), "01":(1,0), "0-1":(-1,0)}
#         move(layout, new_pos, reflections["".join([str(d) for d in direction])])
#     elif space == "-":
#         if abs(direction[0]) == 1:
#             move(layout, new_pos, (0,-1))
#             move(layout, new_pos, (0,1))
#         else:
#             move(layout, new_pos, direction)
#     elif space == "|":
#         if abs(direction[1]) == 1:
#             move(layout, new_pos, (-1,0))
#             move(layout, new_pos, (1,0))
#         else:
#             move(layout, new_pos, direction)
#     return


with open("Day 16/data.txt", "r") as file:
    layout = file.read().split("\n")

# print(layout)

memo = []
beams = [((0,-1), (0,1))]

while beams:
    new_beams = []
    for position, direction in beams:
        if (position, direction) in memo:
            continue
        
        # directions [(1,0),(-1,0),(0,1),(0,-1)]
        memo.append((position,direction))

        new_pos = (position[0] + direction[0], position[1] + direction[1])
        if new_pos[0] < 0 or new_pos[0] >= len(layout) or new_pos[1] < 0 or new_pos[1] >= len(layout[0]):
            continue
        
        space = layout[new_pos[0]][new_pos[1]]
        
        if space == ".":
            new_beams.append((new_pos, direction))
        elif space == "/":
            reflections = {"10":(0,-1), "-10":(0,1), "01":(-1,0), "0-1":(1,0)}
            new_beams.append((new_pos, reflections["".join([str(d) for d in direction])]))
        elif space == "\\":
            reflections = {"10":(0,1), "-10":(0,-1), "01":(1,0), "0-1":(-1,0)}
            new_beams.append((new_pos, reflections["".join([str(d) for d in direction])]))
        elif space == "-":
            if abs(direction[0]) == 1:
                new_beams.append((new_pos, (0,-1)))
                new_beams.append((new_pos, (0,1)))
            else:
                new_beams.append((new_pos, direction))
        elif space == "|":
            if abs(direction[1]) == 1:
                new_beams.append((new_pos, (-1,0)))
                new_beams.append((new_pos, (1,0)))
            else:
                new_beams.append((new_pos, direction))
    beams = new_beams

# print(memo)
energised_spaces = set([m[0] for m in memo])
# print(energised_spaces)

print(len(energised_spaces)-1)