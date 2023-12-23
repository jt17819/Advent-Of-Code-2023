with open("Day 23/data.txt", "r") as file:
    data = file.read().split("\n")

# print(data)

start = (0, data[0].index("."))
end = (len(data)-1, data[-1].index("."))

memo = {}

steps = 0
open_list = [start]

directions = {"v": (1,0), "^":(-1,0), ">":(0,1), "<":(0,-1)}
history = [[]]
while open_list:
# for _ in range(20):
    new_history = []
    new_open_list = []
    for pos in open_list:
        h = history.pop(0)
        # pos = open_list.pop()
        if pos == end:
            memo[pos] = max(memo.get(pos,0), steps)
            # print(h)
            continue
        # print("history",h, "pos", pos)
        if data[pos[0]][pos[1]] in directions:
            y, x = directions[data[pos[0]][pos[1]]]
            new_pos_list = [(pos[0]+y, pos[1]+x)]
        else:
            new_pos_list = [(pos[0]+y, pos[1]+x) for y,x in directions.values()]
        for new_pos in new_pos_list:
            if data[new_pos[0]][new_pos[1]] != "#" and new_pos not in h:
                new_open_list.append(new_pos)
                new_history.append(h + [pos])

        memo[pos] = max(memo.get(pos,0), steps)

    # print(new_open_list)
    open_list = new_open_list
    history = new_history
    steps += 1
    # break

# print(memo)
print(memo[end])


# arr = np.zeros((len(data),len(data[0])))
# for y,x in memo.keys():
#     arr[y][x] = 1
# print(arr)