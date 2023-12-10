with open("Day 8/data.txt", "r") as file:
    data = file.read().split("\n")


directions = data.pop(0).replace("L","0").replace("R","1")
data = [d.split(" = ") for d in data[1:]]
# print(directions)

node_map = {}

for node in data:
    node_map[node[0]] = [n.strip("()") for n in node[1].split(", ")]
# print(node_map)

location = "AAA"
steps = 0
length = len(directions)
while location != "ZZZ":
    location = node_map[location][int(directions[steps % length])]
    steps += 1
print(steps)