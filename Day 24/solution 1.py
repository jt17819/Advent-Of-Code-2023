from math import isclose


class line_equation():
    def __init__(self,x,y,vx,vy) -> None:
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.m = vy / vx

    def intersect(self, line):
        if isclose(self.m, line.m):
            return 0

        intersection_x = (line.m * line.x - self.m * self.x + self.y - line.y) / (line.m - self.m)
        intersection_y = self.y + self.m * ( intersection_x - self.x)

        check = check_direction(self, (intersection_x, intersection_y)) and check_direction(line, (intersection_x, intersection_y))

        return check and 200000000000000 <= intersection_x <= 400000000000000 and 200000000000000 <= intersection_y <= 400000000000000


def check_direction(p1,p2):
    return (p2[0] - p1.x) / p1.vx > 0 and (p2[1] - p1.y) / p1.vy > 0


with open("Day 24/data.txt","r") as file:
    data = file.read().split("\n")

# print(data)

lines = []

for line in data:
    pos, vel = line.split(" @ ")
    px,py,pz = [int(p) for p in pos.split(", ")]
    vx,vy,vz = [int(v) for v in vel.split(", ")]

    lines.append(line_equation(px,py,vx,vy))

ans = 0
for i in range(len(lines)-1):
    for j in range(i+1, len(lines)):
        ans += lines[i].intersect(lines[j])

print(ans)