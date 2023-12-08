import re
import math


with open("Day 2/data.txt", "r") as file:
    data = file.read().split("\n")
# print(data)

# bag = {"red": 12, "green": 13, "blue": 14}
# id_sum = 0
total = 0

for line in data:
    bag = {"red": 0, "green": 0, "blue": 0}
    # print(line)
    id = int(re.findall("\d+", line)[0])
    pulls = line.split(": ")[1].split("; ")
    # print(pulls)

    # check = True
    for pull in pulls:
        balls = pull.split(", ")
        for ball in balls:
            number, colour = ball.split(" ")
            # print(number, colour)
            if int(number) > bag[colour]:
                # check = False
                bag[colour] = int(number)
#     if check:
#         id_sum += id
    # print(bag)
    total += math.prod(bag.values())

# print(id_sum)
print(total)