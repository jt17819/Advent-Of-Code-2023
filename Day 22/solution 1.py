def get_block_pos(b):
    x_range, y_range, z_range = b
    dx = abs(x_range[1] - x_range[0]) + 1
    dy = abs(y_range[1] - y_range[0]) + 1
    dz = abs(z_range[1] - z_range[0]) + 1
    pos = []
    for z in range(min(z_range), min(z_range)+ dz):
        for y in range(min(y_range), min(y_range)+ dy):
            for x in range(min(x_range), min(x_range)+ dx):
                pos.append((x,y,z))

    return pos


def check_intersect(b1, b2):
    b1_pos = [(xy[0],xy[1]) for xy in get_block_pos(b1)]
    b2_pos = [(xy[0],xy[1]) for xy in get_block_pos(b2)]
    for pos in b1_pos:
        if pos in b2_pos:
            return True
    return False


def simulate(block_list, floor):
    fallen = []
    while block_list:
        b = block_list.pop(0)
        while not any(z == 1 for (_, _, z) in b) and not any((x, y, z - 1) in floor for (x, y, z) in b):
            b = [(x, y, z - 1) for (x, y, z) in b]
        fallen.append(b)
        floor.update(b)
    return fallen


with open("Day 22/data.txt", "r") as file:
    data = file.read().split("\n")

# print(data)
blocks = []
height = 0
for line in data:
    start, end = [l.split(",") for l in line.split("~")]
    blocks.append([(int(a), int(b)) for a, b in zip(start,end)])
    height = max(height,max(blocks[-1][2]))
blocks = sorted(blocks, key=lambda z: min(z[2]))
blocks = [get_block_pos(b) for b in blocks]
collapsed = simulate(blocks, set())

# print(collapsed)

removed = 0
for i, brick in enumerate(collapsed):
    floor = set([x for b in collapsed[:i] for x in b if x not in brick])
    # floor = [b for b in collapsed[:i] if b not in brick]
    bricks_above = collapsed[i + 1 :]
    result = simulate(bricks_above[:], floor)
    removed += result == bricks_above

print(removed)

# tower = [[] for _ in range(height+1)]
# # print(len(tower))
# count = 0
# for block in blocks:
#     # block_pos = get_block_pos(block)
#     placed = False
#     # for index, layer in enumerate(tower):
#     for index in range(max(block[2]),-1,-1):
#         intersect = False
#         for b in tower[index]:
#             if check_intersect(block, b):
#                 intersect = True

#         if intersect:
#             dz = abs(block[2][1] - block[2][0]) + 1
#             block[2] = (index + 1, index + dz)
#             for idz in range(index, index + dz):
#                 tower[idz+1].append(block)
#             placed = True

#         if placed:
#             break

#     if not placed:
#         block[2] = (1, abs(block[2][1] - block[2][0]) + 1)
#         tower[0].append(block)

# while tower[-2] == []:
#     tower.pop()
# print(tower[:-2])

# removed = []
# for index in range(len(tower)-2,-1,-1):
#     for block in reversed(tower[index]):
#         removable = True
#         for above_block in tower[index+1]:
#             if check_intersect(block, above_block):
#                 removable = False
#         if removable and block not in removed:
#             removed.append(block)

#         if index > 0:
#             count = 0
#             for supported_block in tower[index-1]:
#                 if check_intersect(block, supported_block):
#                     count += 1
#             if count > 1:
#                 tower[index].remove(block)
    
# # print(removed)
# print(len(removed))