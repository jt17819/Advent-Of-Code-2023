from math import lcm


with open("Day 08/data.txt", "r") as file:
    data = file.read().split("\n")

directions = data.pop(0).replace("L","0").replace("R","1")
data = [d.split(" = ") for d in data[1:]]
# print(directions)
node_map = {}

for node in data:
    node_map[node[0]] = [n.strip("()") for n in node[1].split(", ")]
# print(node_map)

locations = [start for start in node_map if start[-1] == "A"]
length = len(directions)
ans = []

for location in locations:
    steps = 0
    while location[-1] != "Z":
        location = node_map[location][int(directions[steps % length])]
        steps += 1
    ans.append(steps)

print(ans)
print(lcm(*ans))