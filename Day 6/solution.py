import math


with open("Day 6/data.txt", "r") as file:
    data = file.read().split("\n")

print(data)

time  = [int(d) for d in data[0].split(":")[1].split(" ") if d]
distance = [int(d) for d in data[1].split(":")[1].split(" ") if d]
print(time, distance)

total = []
for i in range(len(time)):
    d = 0
    t = -1
    while d <= distance[i]:
        t += 1
        d = (time[i] - t) * t
    total.append((time[i] + 1) - (t * 2))

print(total)
print(math.prod(total))