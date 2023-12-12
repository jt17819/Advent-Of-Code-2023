import numpy as np, itertools


def check_spring(map_to_check, expected):
    count = 0
    consec_springs = []
    for s in map_to_check:
        if s == "#":
            count += 1
        elif count:
            consec_springs.append(count)
            count = 0
    if count:
        consec_springs.append(count)
    return consec_springs == expected


with open("Day 12/data.txt", "r") as file:
    data = file.read().split("\n")

total_arrangements = 0
for line in data:
    spring_map, springs = line.split(" ")
    spring_map = np.array([s for s in spring_map])
    springs = [int(s) for s in springs.split(",")]
    # print(spring_map, springs)
    total_missing = np.where(spring_map=="?")[0]
    springs_missing = sum(springs) - np.count_nonzero(spring_map=="#")
    # print(total_missing, springs_missing)

    # print([c for c in itertools.combinations(total_missing, springs_missing)])
    for c in itertools.combinations(total_missing, springs_missing):
        temp = ["#" if i in c else spring_map[i] for i in range(len(spring_map))]
        # print(check_spring(temp, springs))
        total_arrangements += check_spring(temp, springs)
print(total_arrangements)