import numpy as np


def find_path(maze, heat_loss_map):
    directions = {"UP":(-1,0),"DOWN":(1,0),"LEFT":(0,-1),"RIGHT":(0,1)}
    possible_turns = {"UP"   :["UP","LEFT","RIGHT"],
                      "DOWN" :["DOWN","LEFT","RIGHT"],
                      "LEFT" :["LEFT","UP","DOWN"],
                      "RIGHT":["RIGHT","UP","DOWN"]}
    
    to_check = list(heat_loss_map.keys())
    while to_check:
        new_to_check = []

        for direction, steps, y, x in to_check:
            turns = possible_turns[direction][:]
            if steps < 4:
                turns = [direction]
            elif steps == 10:
                # print(direction,y,x)
                turns.remove(direction)

            for turn in turns:
                dy, dx = directions[turn]
                next_y = y + dy
                next_x = x + dx
                if not (0 <= next_y < len(maze)) or not (0 <= next_x < len(maze[0])):
                    continue
                
                next_steps = steps + 1 if turn == direction else 1
                next_key = (turn, next_steps, next_y, next_x)
                next_heat_loss = heat_loss_map[(direction, steps, y, x)] + maze[next_y][next_x]
                
                if next_key not in heat_loss_map or heat_loss_map[next_key] > next_heat_loss:
                    heat_loss_map[next_key] = next_heat_loss
                    new_to_check.append((turn, next_steps, next_y, next_x))
                    
        to_check = new_to_check
        
    return

with open("Day 17/data.txt", "r") as file:
    data = file.read().split("\n")

for i, line in enumerate(data):
    data[i] = [int(char) for char in line]

# print(np.array(data))

heat_loss_map = {}
heat_loss_map["LEFT", 10, 0, 0] = 0
heat_loss_map["DOWN", 10, 0 ,0] = 0
end = (len(data) - 1, len(data[0]) - 1)

find_path(data, heat_loss_map)
# print(heat_loss_map)
print(min(value for (_, steps, y, x), value in heat_loss_map.items() if (y, x) == end and steps > 3))