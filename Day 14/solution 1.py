with open("Day 14/data.txt", "r") as file:
    data = file.read().split("\n")

# print(data)

total = 0
for i in range(len(data[0])):
    column = [c[i] for c in data]
    start = len(column)
    count = 0
    for j, space in enumerate(column):
        if space == "#":

            total += sum(range(start,start-count,-1))
            start = len(column) - j - 1
            count = 0
        if space == "O":
            count += 1

    total += sum(range(start,start-count,-1))
print(total)
