import random


with open("Day 25/data.txt","r") as file:
    data = file.read().split("\n")

# print(data)

connections = {}

for line in data:
    key, wires = line.split(": ")
    for wire in wires.split(" "):
        if key in connections and wire not in connections[key]:
            connections[key].append(wire)
        else:
            connections[key] = [wire]
        if wire in connections and key not in connections[wire]:
            connections[wire].append(key)
        else:
            connections[wire] = [key]
# print(connections)

nodes = list(connections.keys())
edge_count = {}

for _ in range(1000):
    seen = set()
    start, end = random.choices(nodes, k=2)
    q = [(start, [start])]
    while q:
        node, path = q.pop(0)
        if node == end:
            for a,b in zip(path[:-1], path[1:]):
                if (min(a,b),max(a,b)) in edge_count:
                    edge_count[(min(a,b),max(a,b))] += 1
                else:
                    edge_count[(min(a,b),max(a,b))] = 1
            break
        seen.add(node)
        q.extend((connection, path + [connection]) for connection in connections[node] if connection not in seen)

to_remove = [edge[0] for edge in sorted(edge_count.items(), reverse=True, key=lambda x: x[1])[:3]]

print(to_remove)
for a, b in to_remove:
    connections[a].remove(b)
    connections[b].remove(a)

a = set()
b = set()

to_add = [random.choice(list(connections.keys()))]
while to_add:
    wire = to_add.pop(0)
    a.add(wire)
    for c in connections[wire]:
        if c not in a:
            to_add.append(c)
        
# print(a)

for k in connections.keys():
    if k not in a:
        to_add = [k]
        break
    
while to_add:
    wire = to_add.pop(0)
    b.add(wire)
    for c in connections[wire]:
        if c not in b:
            to_add.append(c)
    
# print(b)
print(len(a) * len(b))