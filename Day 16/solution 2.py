def move(layout, position, direction, memo):
    while 0 <= position[0] < len(layout) and 0 <= position[1] < len(layout[0]) and direction not in memo.get(position, []):
        # directions [(1,0),(-1,0),(0,1),(0,-1)]
        if position in memo:
            memo[position].append(direction)
        else:
            memo[position] = [direction]

        space = layout[position[0]][position[1]]
        
        if space == "/":
            # reflections: {"10":(0,-1), "-10":(0,1), "01":(-1,0), "0-1":(1,0)}
            direction = (-direction[1], -direction[0])
        elif space == "\\":
            # reflections: {"10":(0,1), "-10":(0,-1), "01":(1,0), "0-1":(-1,0)}
            direction = (direction[1], direction[0])
        elif space == "-":
            if abs(direction[0]) == 1:
                # left: (0,-1)
                move(layout, (position[0],position[1] - 1), (0,-1), memo)
                # right: (0,1)
                direction = (0,1)
        elif space == "|":
            if abs(direction[1]) == 1:
                # up: (-1,0)
                move(layout, (position[0] - 1,position[1]), (-1,0), memo)
                # down: (1,0)
                direction = (1,0)
        position = (position[0] + direction[0], position[1] + direction[1])

    return len(memo)


with open("Day 16/data.txt", "r") as file:
    layout = file.read().split("\n")

ans = 0
# starting_beams = [((0,0), (0,1))]
starting_beams  = [((l,0), (0,1)) for l in range(len(layout))]
starting_beams += [((0,l), (1,0)) for l in range(len(layout[0]))]
starting_beams += [((l,len(layout)-1), (0,-1)) for l in range(len(layout))]
starting_beams += [((len(layout[0])-1,l), (-1,0)) for l in range(len(layout[0]))]
for beams in starting_beams:
    memo = {}
    ans = max(ans, move(layout,beams[0],beams[1],memo))
print(ans)