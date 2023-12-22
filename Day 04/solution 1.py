with open("Day 04/data.txt", "r") as file:
    data = file.read().split("\n")

total = 0
for line in data:
    # print(line)
    score = 0
    cards = line.split(": ")[1]
    win_nums, scratch_nums = cards.split(" | ")
    win_nums = [win_nums[num:num + 2].strip() for num in range(0,len(win_nums),3)]
    scratch_nums = [scratch_nums[num:num + 2].strip() for num in range(0,len(scratch_nums),3)]
    # print(win_nums, scratch_nums)
    for num in scratch_nums:
        if num in win_nums:
            score += 1
    # print(score)
    if score:
        total += 2 ** (score - 1)

print(total)