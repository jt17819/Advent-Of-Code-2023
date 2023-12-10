import numpy as np


with open("Day 5/data.txt", "r") as file:
    data = file.read().split("\n\n")
# print(data)

category_map = {}
for category in data:
    name, values = category.split(":")
    values = values.split("\n")
    values = [np.array(value.strip().split(" "), dtype=np.int64) for value in values if value]
    category_map[name] = values

# print(category_map)

# almanac = {}
# for c in category_map:
#     if "map" in c:
#         almanac[c] = {}
#         for mapping in category_map[c]:
#             for i in range(int(mapping[2])):
#                 almanac[c][int(mapping[1]) + i] = int(mapping[0]) + i

# print(almanac)

seeds = category_map.pop("seeds")[0]
# print(seeds)
# print(category_map)
ans = float("inf")
for seed in seeds:
    current = int(seed)
    for c in category_map:
        map_list = category_map[c]
        for mapping in map_list:
            if current >= mapping[1] and current < mapping[1] + mapping[2]:
                current += mapping[0] - mapping[1]
                break
    ans = min(ans, current)

print(ans)