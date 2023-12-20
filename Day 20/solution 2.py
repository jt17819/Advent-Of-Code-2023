import math


class Broadcaster:
    def __init__(self, destinations) -> None:
        self.state = None
        self.destinations =  destinations

    def emit_pulse(self):
        return False


class FlipFlop:
    def __init__(self, destinations) -> None:
        self.state = False
        self.destinations = destinations

    def emit_pulse(self, pulse, _):
        if pulse == 0:
            self.state = not self.state
            return self.state
        else:
            return None


class Conjunction:
    def __init__(self, destinations) -> None:
        self.state = {}
        self.destinations = destinations

    def emit_pulse(self, pulse, source):
        self.state[source] = pulse
        if all(self.state.values()):
            return False
        else:
            return True


def connect_conjunction_input(connected_modules):
    conjuntions = [d.split(" -> ")[0][1:] for d in data if d[0] == "&"]
    for module_name, module in connected_modules.items():
        for destination in module.destinations:
            if destination in conjuntions:
                connected_modules[destination].state[module_name] = False
    return connected_modules


with open("Day 20/data.txt", "r") as file:
    data = file.read().split("\n")

# print(data)

modules = {}
for line in data:
    key, value = line.split(" -> ")
    module_type, module_name = key[0], key[1:]
    if module_type == "%":
        modules[module_name] = FlipFlop(value.split(", "))
    elif module_type == "&":
        modules[module_name] = Conjunction(value.split(", "))
    else:
        modules[key] = Broadcaster(value.split(", "))

modules = connect_conjunction_input(modules)

loops = 0
rx_check = {}

for _ in range(5000):
    queue = [("broadcaster", False)]
    loops += 1
    while queue:
        # if sum(modules["nc"].state.values()) > 0:
        #     print(modules["nc"].state, loops)
        new_queue = []
        for current, pulse in queue:

            for destination in modules[current].destinations:
                if destination not in modules:
                    continue
                if destination == "nc" and pulse and current not in rx_check:
                    rx_check[current] = loops

                new_pulse = modules[destination].emit_pulse(pulse, current)
                if new_pulse != None:
                    new_queue.append((destination, new_pulse))
        queue = new_queue

print(rx_check)
print(math.lcm(*rx_check.values()))