import numpy as np


with open("Day 04/data.txt", "r") as file:
    data = file.read().split("\n")

total_cards = []
copies = [1] * len(data)
for line in range(len(data)):
    # print(data[line])
    score = 0
    cards = data[line].split(": ")[1]
    win_nums, scratch_nums = cards.split(" | ")
    win_nums = [win_nums[num:num + 2].strip() for num in range(0,len(win_nums),3)]
    scratch_nums = [scratch_nums[num:num + 2].strip() for num in range(0,len(scratch_nums),3)]
    # print(win_nums, scratch_nums)
    for num in scratch_nums:
        if num in win_nums:
            score += 1
    # print(score)
    # if score:
    for i in range(line + 1, line + score + 1):
        # print(line, i)
        copies[i] += 1 * copies[line]

print(sum(copies))