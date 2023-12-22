# import numpy as np
import re


# data = np.loadtxt("Day 03/data.txt", dtype=str)
with open("Day 03/data.txt", "r") as file:
    data = file.read().split("\n")

total = 0
special_chars = "!£$%^&*()|?\/<>#~@=+-_"
non_special_chars = ".0123456789"
line_count = 0
data_length = len(data)
# print(data)
for line in data:
    max_length = len(line)
    # print(line)
    digits = re.findall("\d+", line)
    # print(digits)
    index = []

    for i in range(len(digits)):
        if index:
            start = index[-1] + len(digits[i-1])
        else:
            start = 0
        index.append(line[start:].index(digits[i]) + start)

    # print(index)
    top_row = max(0 ,line_count - 1)
    bot_row = min(data_length - 1, line_count + 1)
    for i in range(len(digits)):
        length = len(digits[i])
        left = max(0, index[i]-1)
        right = min(max_length - 1, index[i] + length)
        # print(left, right)

        if data[line_count][left] in special_chars or data[line_count][right] in special_chars:
            total += int(digits[i])
            continue

        for d in range(left, right + 1):
            # print(d)
            if data[top_row][d] in special_chars or data[bot_row][d] in special_chars:
                total += int(digits[i])
                break
    line_count += 1

print(total)