with open("Day 15/data.txt", "r") as file:
    data = file.read().strip().split(",")

# print(data)
total = 0
for s in data:
    hashed = 0
    for c in s:
        hashed = ((hashed + ord(c)) * 17) % 256
    total += hashed

print(total)
