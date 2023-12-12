def check_spring(map_to_check, expected):
    if ("".join(map_to_check), "".join([str(e) for e in expected])) in memo:
        return memo[("".join(map_to_check), "".join([str(e) for e in expected]))]

    # invalid if more blocks needed but no space left, valid if no more needed
    if not map_to_check:
        return 0 if expected else 1
    
    # no more blocks of damaged springs (#) needed, spring map invalid if contains if contains any #, otherwise all ? set to . so 1 valid combination can be made
    elif not expected:
        return 0 if "#" in map_to_check else 1
    total = 0

    # spring is . or can be set to . (?)
    if map_to_check[0] == "." or map_to_check[0] == "?":
        total += check_spring(map_to_check[1:], expected[:])

    # spring is # or can be set to # (?)
    if map_to_check[0] == "#" or map_to_check[0] == "?":
        # check if consec block possible
        if len(map_to_check) < sum(expected):
            return total
        if "." in map_to_check[:expected[0]]:
            return total

        # check if finished
        if len(map_to_check) == expected[0]:
            return total + 1
        # check if consec block has ended - must be followed by .
        if map_to_check[expected[0]] == "." or map_to_check[expected[0]] == "?":
            total += check_spring(map_to_check[expected[0]+1:],expected[1:])
        # else invalid
        else:
            return total

    memo[("".join(map_to_check), "".join([str(e) for e in expected]))] = total
    return total

with open("Day 12/data.txt", "r") as file:
    data = file.read().split("\n")
    
total_arrangements = 0
for line in data:
    memo = {}
    spring_map, springs = line.split(" ")
    # spring_map = [s for s in spring_map]
    spring_map = (("?" + spring_map) * 5)[1:]
    springs = [int(s) for s in springs.split(",")] * 5
    
    # print(spring_map, springs)

    total_arrangements += check_spring(spring_map,springs)

print(total_arrangements)