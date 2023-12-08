import numpy as np


def compute_map(mapping, seed_start, seed_range):
    seeds = [seed_start, seed_range]
    map_start = mapping[1]
    map_range = mapping[2]
    if map_start <= seed_start and map_start + map_range >= seed_start + seed_range:
        # print(1)
        new_seed_start_1 = mapping[0] - mapping[1] + seed_start
        seeds = [new_seed_start_1, seed_range]

    elif map_start <= seed_start and map_start + map_range - 1 >= seed_start:
        # print(2)
        new_seed_range_1 = map_start + map_range - seed_start
        new_seed_start_1 = mapping[0] - mapping[1] + seed_start
        new_seed_range_2 = seed_range - new_seed_range_1
        new_seed_start_2 = map_start + map_range
        seeds = [new_seed_start_1, new_seed_range_1, new_seed_start_2, new_seed_range_2]

    elif map_start >= seed_start and map_start + map_range <= seed_start + seed_range:
        # print(3)
        new_seed_range_1 = map_start - seed_start
        new_seed_start_1 = seed_start
        new_seed_range_2 = map_range
        new_seed_start_2 = mapping[0]
        new_seed_range_3 = seed_start + seed_range - map_start - map_range
        new_seed_start_3 = map_start + map_range
        seeds = [new_seed_start_1, new_seed_range_1, new_seed_start_2, new_seed_range_2, new_seed_start_3, new_seed_range_3]

    elif map_start >= seed_start and map_start <= seed_start + seed_range - 1:
        # print(4)
        new_seed_range_1 = seed_range + seed_start - map_start
        new_seed_start_1 = mapping[0]
        new_seed_range_2 = map_start - seed_start
        new_seed_start_2 = seed_start
        seeds = [new_seed_start_1, new_seed_range_1, new_seed_start_2, new_seed_range_2]
    
    return seeds


with open("Day 5/data.txt", "r") as file:
    data = file.read().split("\n\n")
# print(data)

category_map = {}
for category in data:
    name, values = category.split(":")
    values = values.split("\n")
    values = [np.array(value.strip().split(" "), dtype=np.int64) for value in values if value]
    category_map[name] = values

seeds = category_map.pop("seeds")[0]

# print(compute_map(category_map["seed-to-soil map"][0], seeds[0], seeds[1]))
# print(seeds)
# print(category_map)
# new_seeds = [compute_map(category_map["seed-to-soil map"][1], seeds[i], seeds[i+1]) for i in range(0,len(seeds),2)]
# print(new_seeds)

# c = "seed-to-soil map"
for c in category_map:
    # print(seeds)
    map_list = category_map[c]
    new_seeds = []
    for i in range(0, len(seeds), 2):
        seed_start = seeds[i]
        seed_range = seeds[i+1]
        mapped = False
        for mapping in map_list:
            mapped_seeds = (compute_map(mapping, seed_start, seed_range))
            if mapped_seeds != [seed_start, seed_range]:
                mapped = True
                new_seeds.extend(mapped_seeds)
        if not mapped:
            new_seeds.extend([seed_start, seed_range])

    seeds = new_seeds

# print(seeds)

locations = [seeds[i] for i in range(0, len(seeds), 2) if seeds[i]]
print(min(locations))