from math import isclose


class line_equation():
    def __init__(self,x,y,z,vx,vy,vz) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.eq = lambda t: (vx*t + x, vy*t + y, vz*t + z)

    def prnt(self):
        print(self.x,self.y,self.z,self.vx,self.vy,self.vz)

    def intersect(self, line):
        if isclose(self.m, line.m):
            return 0

        intersection_x = (line.m * line.x - self.m * self.x + self.y - line.y) / (line.m - self.m)
        intersection_y = self.y + self.m * ( intersection_x - self.x)

        check = check_direction(self, (intersection_x, intersection_y)) and check_direction(line, (intersection_x, intersection_y))

        return check and 200000000000000 <= intersection_x <= 400000000000000 and 200000000000000 <= intersection_y <= 400000000000000


def check_direction(p1,p2):
    return (p2[0] - p1.x) / p1.vx > 0 and (p2[1] - p1.y) / p1.vy > 0


def get_vector(p1,p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]
    return(dx,dy,dz)


with open("Day 24/data.txt","r") as file:
    data = file.read().split("\n")

# print(data)

lines = []

for line in data:
    pos, vel = line.split(" @ ")
    px,py,pz = [int(p) for p in pos.split(", ")]
    vx,vy,vz = [int(v) for v in vel.split(", ")]

    lines.append(line_equation(px,py,pz,vx,vy,vz))
# lines.sort(key=lambda l: l.z)
# print([lines[i].z for i in range(len(lines))])
# print(lines[0].eq(1))
# a,b,c = lines[:3]
# t = 0

all_vx = {}
all_vy = {}
all_vz = {}
possible_x = None
possible_y = None
possible_z = None

for line in lines:
    if line.vx in all_vx and line.vx > 100:
        # all_vx[line.vx].append(line)
        diff = all_vx[line.vx].x - line.x
        new_x_set = set()
        for v in range(-1000, 1000):
            if v == line.vx:
                continue
            if diff % (v - line.vx) == 0:
                new_x_set.add(v)
        if possible_x == None:
            possible_x = new_x_set.copy()
        else:
            possible_x = possible_x & new_x_set

        # for l in all_vx[line.vx]:
            # print("X")
            # l.prnt()
    else:
        all_vx[line.vx] = line
        
    if line.vy in all_vy and line.vy > 100:
        # all_vy[line.vy].append(line)
        diff = all_vy[line.vy].y - line.y
        new_y_set = set()
        for v in range(-1000, 1000):
            if v == line.vy:
                continue
            if diff % (v - line.vy) == 0:
                new_y_set.add(v)
        if possible_y == None:
            possible_y = new_y_set.copy()
        else:
            possible_y = possible_y & new_y_set
        # for l in all_vy[line.vy]:
            # print("Y")
            # l.prnt()
    else:
        all_vy[line.vy] = line
        
    if line.vz in all_vz and line.vz > 100:
        # all_vz[line.vz].append(line)
        diff = all_vz[line.vz].z - line.z
        new_z_set = set()
        for v in range(-1000, 1000):
            if v == line.vz:
                continue
            if diff % (v - line.vz) == 0:
                new_z_set.add(v)
        if possible_z == None:
            possible_z = new_z_set.copy()
        else:
            possible_z = possible_z & new_z_set
        # for l in all_vz[line.vz]:
            # print("Z")
            # l.prnt()
    else:
        all_vz[line.vz] = line

print(possible_x, possible_y, possible_z)

stone_vx, stone_vy, stone_vz = possible_x.pop(), possible_y.pop(), possible_z.pop()

p1, p2 = lines[0], lines[1]

grad1 = (p1.vy - stone_vy) / (p1.vx - stone_vx)
grad2 = (p2.vy - stone_vy) / (p2.vx - stone_vx)
intercept1 = p1.y - grad1 * p1.x
intercept2 = p2.y - grad2 * p2.x

stone_x = (intercept2 - intercept1) / (grad1 - grad2)
stone_y = grad1 * stone_x + intercept1
time = (stone_x - p1.x) / (p1.vx - stone_vx)
stone_z = p1.z + (p1.vz - stone_vz) * time

print(round(stone_x),round(stone_y),round(stone_z))
print(sum([round(stone_x),round(stone_y),round(stone_z)]))