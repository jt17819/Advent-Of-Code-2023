import re
import math


with open("Day 02/data.txt", "r") as file:
    data = file.read().split("\n")
# print(data)

bag = {"red": 12, "green": 13, "blue": 14}
id_sum = 0

for line in data:
    # print(line)
    id = int(re.findall("\d+", line)[0])
    pulls = line.split(": ")[1].split("; ")
    # print(pulls)

    check = True
    for pull in pulls:
        balls = pull.split(", ")
        for ball in balls:
            number, colour = ball.split(" ")
            # print(number, colour)
            if int(number) > bag[colour]:
                check = False
    if check:
        id_sum += id
    # print(bag)

print(id_sum)