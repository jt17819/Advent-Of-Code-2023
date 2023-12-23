def find_path(graph, start, path, distance, end):
    # print(start)
    if start == end:
        print(distance, path)
        return distance
    path.append(start[0])
    directions = graph[start[0]]
    for direction in directions:
        # distance += direction[1]
        if direction[0] in path:
            continue
        
        distance = max(distance, find_path(graph, direction, path[:], distance + direction[1], end))
    return distance

with open("Day 23/data.txt", "r") as file:
    data = file.read().split("\n")

# print(data)

start = (0, data[0].index("."))
end = (len(data)-1, data[-1].index("."))

memo = {}

steps_list = [0]
open_list = [start]

directions = {"v": (1,0), "^":(-1,0), ">":(0,1), "<":(0,-1)}
# history = []
history = [[]]
# path = {start: node(steps)}
junctions = [start]
graph = {}

while open_list:
# for _ in range(20):
    new_history = []
    new_open_list = []
    new_junctions = []

    for pos in open_list:
        # history.append(pos)
        h = history.pop(0)
        junction = junctions.pop(0)
        steps = steps_list.pop(0)

        if pos == end:
            if junction in graph:
                if (pos, steps) not in graph[junction]:
                    graph[junction].append((pos, steps))
            else:
                graph[junction] = [(pos, steps)]
            
            if pos in graph:
                if (junction, steps) not in graph[pos]:
                    graph[pos].append((junction, steps))
            else:
                graph[pos] = [(junction, steps)]
            # memo[pos] = max(memo.get(pos,0), steps)
            continue
        
        if data[pos[0]][pos[1]] in directions:
            y, x = directions[data[pos[0]][pos[1]]]
            new_pos_list = [(pos[0]+y, pos[1]+x)]
        else:
            new_pos_list = [(pos[0]+y, pos[1]+x) for y,x in directions.values()]
        path_count = 0
        for new_pos in new_pos_list:
            if data[new_pos[0]][new_pos[1]] != "#" and new_pos not in h:
                new_open_list.append(new_pos)
                new_history.append(h + [pos])
                path_count += 1

        # memo[pos] = max(memo.get(pos,0), steps)

        if path_count > 1:
            if junction in graph:
                if (pos, steps) not in graph[junction]:
                    graph[junction].append((pos, steps))
            else:
                graph[junction] = [(pos, steps)]
            
            if pos in graph:
                if (junction, steps) not in graph[pos]:
                    graph[pos].append((junction, steps))
            else:
                graph[pos] = [(junction, steps)]
            for _ in range(path_count):
                new_junctions.append(pos)
                steps_list.append(1)

        elif path_count == 1:
            steps += 1
            new_junctions.append(junction)
            steps_list.append(steps)

    # print(new_open_list)
    open_list = new_open_list
    history = new_history
    junctions = new_junctions
    # break

# print(memo)
# print(memo[end])
# print(history)
# print(find_path(graph, ((0,1),0), [], 0, end))

# open_nodes = graph[start]
# open_nodes = [[((0, 1), 15), ((13, 5), 22), ((3, 11), 22)]]
open_nodes = [(0, 1)]
distances = [0]
history = [[]]

ans = 0
queue = [(start, 0, {start})]
while queue:
    curr, steps, visited = queue.pop()
    if curr == end:
        print(visited)
        ans = max(steps, ans)
        continue
    for next, distance in graph[curr]:
        if next not in visited:
            queue.append((next, steps+distance, visited|{next}))
    
print(ans)