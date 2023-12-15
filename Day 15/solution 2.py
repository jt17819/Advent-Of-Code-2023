def lens_hash(lens):
    hashed = 0
    for c in lens:
        hashed = ((hashed + ord(c)) * 17) % 256
    return hashed


with open("Day 15/data.txt", "r") as file:
    data = file.read().strip().split(",")

# print(data)

boxes = {n:[] for n in range(256)}

for s in data:
    if "=" in s:
        box, focal_length = s.split("=")
        if box not in [b[0] for b in boxes[lens_hash(box)]]:
            boxes[lens_hash(box)].append((box,focal_length))
        else:
            ind = [b[0] for b in boxes[lens_hash(box)]].index(box)
            boxes[lens_hash(box)][ind] = (box,focal_length)
    else:
        box, _ = s.split("-")
        if box in [b[0] for b in boxes[lens_hash(box)]]:
            ind = [b[0] for b in boxes[lens_hash(box)]].index(box)
            boxes[lens_hash(box)].pop(ind)
            
total = 0
for box_num, lenses in boxes.items():
    for i, lens in enumerate(lenses):
        total += (box_num + 1) * (i + 1) * int(lens[1])
print(total)
