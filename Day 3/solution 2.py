import numpy as np
import re


# data = np.loadtxt("Day 3/data.txt", dtype=str)
with open("Day 3/data.txt", "r") as file:
    data = file.read().split("\n")

new_data = []
for d in data:
    temp = []
    for l in d:
        temp.append(l)
    new_data.append(temp)

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
        left = max(0, index[i])
        right = min(max_length - 1, index[i] + length)
        # print(left, right)

        for j in range(length):
            new_data[line_count][left + j] = digits[i]
        # if data[line_count][left] in special_chars or data[line_count][right] in special_chars:
        #     total += int(digits[i])
        #     continue

        # for d in range(left, right + 1):
        #     print(d)
        #     if data[top_row][d] in special_chars or data[bot_row][d] in special_chars:
        #         total += int(digits[i])
        #         break
    line_count += 1

# print(new_data)
line_count = 0

for line in data:
    max_length = len(line)
    # print(line)
    asterisks = re.findall("\*", line)
    # print(asterisks)
    index = []

    for i in range(len(asterisks)):
        if index:
            start = index[-1] + len(asterisks[i-1])
        else:
            start = 0
        index.append(line[start:].index(asterisks[i]) + start)

    # print(index)
    top_row = max(0 ,line_count - 1)
    bot_row = min(data_length - 1, line_count + 1)
    for i in range(len(asterisks)):
        # length = len(digits[i])
        left = max(0, index[i] - 1)
        right = min(max_length - 1, index[i] + 1)
        # print(left, right)

        nums = []

        if re.search("\d",new_data[line_count][left]):
            nums.append(new_data[line_count][left])

        if re.search("\d",new_data[line_count][right]):
            nums.append(new_data[line_count][right])

        for d in range(left, right + 1):
            # print(d,new_data[top_row][d],new_data[bot_row][d])
            if re.search("\d",new_data[top_row][d]):
                nums.append(new_data[top_row][d])
            if re.search("\d",new_data[bot_row][d]):
                nums.append(new_data[bot_row][d])
        # print("nums",nums)
        nums = set(nums)
        if len(nums) == 2:
            nums = [int(num) for num in nums]
            total += nums[0] * nums[1]

    line_count += 1
print(total)