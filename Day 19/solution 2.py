from math import prod


def process_workflow(current, old_part):
    ans = 0
    # print(current, old_part)
    for instruction in workflow[current]:
        if "<" in instruction:
            check, destination = instruction.split(":")
            category, count = check.split("<")
            low, high = old_part[category]
            if high < int(count):
                new_part = dict(old_part)
                if destination == "A":
                    # print(new_part)
                    return ans + prod([b - a + 1 for a,b in new_part.values()])
                elif destination == "R":
                    return ans
                else:
                    return ans + process_workflow(destination, new_part)
            elif low < int(count):
                new_part = dict(old_part)
                new_part[category] = [new_part[category][0], min(high, int(count) - 1)]
                old_part[category] = [new_part[category][1] + 1, old_part[category][1]]
                if destination == "A":
                    # print(new_part)
                    ans += prod([b - a + 1 for a,b in new_part.values()])
                    pass
                    # return sum(new_part.values()) # add sum to ans
                elif destination == "R":
                    pass
                else:
                    ans += process_workflow(destination, new_part)

        elif ">" in instruction:
            check, destination = instruction.split(":")
            category, count = check.split(">")
            low, high = old_part[category]
            if low > int(count):
                new_part = dict(old_part)
                if destination == "A":
                    # print(new_part)
                    return ans + prod([b - a + 1 for a,b in new_part.values()])
                elif destination == "R":
                    return ans
                else:
                    return ans + process_workflow(destination, new_part)
            elif high > int(count):
                new_part = dict(old_part)
                new_part[category] = [max(low, int(count) + 1), new_part[category][1]]
                old_part[category] = [old_part[category][0], new_part[category][0] - 1]
                if destination == "A":
                    # print(new_part)
                    ans += prod([b - a + 1 for a,b in new_part.values()])
                    pass
                    # return sum(new_part.values())
                elif destination == "R":
                    pass
                else:
                    ans += process_workflow(destination, new_part)

        else:
            if instruction == "A":
                # print(old_part)
                return ans + prod([b - a + 1 for a,b in old_part.values()])
            elif instruction == "R":
                return ans
            else:
                return ans + process_workflow(instruction, old_part)

    return ans


with open("Day 19/data.txt", "r") as file:
    data = file.read().split("\n\n")

workflow, _ = [d.split("\n") for d in data]
workflow = {w.split("{")[0]:w[:-1].split("{")[1].split(",") for w in workflow}
part = {"x": [1,4000], "m": [1,4000], "a": [1,4000], "s": [1,4000]}
# print(workflow)

current = "in"
print(process_workflow(current, part))
# print(ans)