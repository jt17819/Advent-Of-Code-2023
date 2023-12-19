with open("Day 19/data.txt", "r") as file:
    data = file.read().split("\n\n")

workflow, parts = [d.split("\n") for d in data]
workflow = {w.split("{")[0]:w[:-1].split("{")[1].split(",") for w in workflow}
parts = [{a.split("=")[0]:int(a.split("=")[1]) for a in p.strip("{}").split(",")} for p in parts]
# print(workflow)
# print(parts)

ans = 0
for part in parts:
    current = "in"
    sorting = True
    while sorting:
        # print(current, workflow[current])
        for instruction in workflow[current]:
            if "<" in instruction:
                check, destination = instruction.split(":")
                category, count = check.split("<")
                if part[category] < int(count):
                    if destination == "A":
                        ans += sum(part.values())
                        sorting = False
                    elif destination == "R":
                        sorting = False
                    else:
                        current = destination
                    break
            
            elif ">" in instruction:
                check, destination = instruction.split(":")
                category, count = check.split(">")
                # print(category, part[category], count)
                if part[category] > int(count):
                    # print("dest", destination)
                    if destination == "A":
                        ans += sum(part.values())
                        sorting = False
                    elif destination == "R":
                        sorting = False
                    else:
                        current = destination
                    break
            
            else:
                if instruction == "A":
                        ans += sum(part.values())
                        sorting = False
                elif instruction == "R":
                    sorting = False
                else:
                    current = instruction
                break
print(ans)