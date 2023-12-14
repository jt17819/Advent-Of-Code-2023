def tilt_table(table):
    for _ in range(4):
        for i in range(len(table[0])):
            column = [c[i] for c in table]
            pointer = 0
            for j, space in enumerate(column):
                if space == "#":
                    pointer = j + 1
                if space == "O":
                    table[j][i] = "."
                    table[pointer][i] = "O"
                    pointer += 1
        table = [list(a) for a in zip(*table[::-1])]
    return table


with open("Day 14/data.txt", "r") as file:
    str_data = file.read().split("\n")

data = []
for line in str_data:
    data.append([s for s in line])

# print(np.array(data))

# cycle = ["north", "west", "south", "east"]
memo = ["".join(["".join(a) for a in data])]
for i in range(1000000000):
    data = tilt_table(data)
    mem = "".join(["".join(a) for a in data])
    if mem in memo:
        remainder = 1000000000 - (i+1)
        cycle_length = (i+1) - memo.index(mem)
        str_data = memo[remainder % cycle_length + memo.index(mem)]
        length = len(data)
        for n in range(length):
            data[n] = ([s for s in str_data[n*length:(n+1)*length]])
        break
    memo.append(mem)

total = 0
val = len(data) 
for row in data:
    total += val * row.count("O")
    val -= 1

print(total)
