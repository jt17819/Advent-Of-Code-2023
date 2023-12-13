import numpy as np


with open("Day 13/data.txt", "r") as file:
    data = file.read().split("\n\n")

# print(data)
pattern_array = []
i = 0
for pattern in data:
    arr = []
    for line in pattern.split("\n"):
        arr.append([a for a in line])
    pattern_array.append(np.array(arr))
    i += 1

# print(pattern_array)

# sym_lines = []
total = 0
for pattern in pattern_array:
    for i in range(len(pattern)-1):
        if np.all(pattern[i] == pattern[i+1]):
            check_sym = True
            length = min(i+1,len(pattern)-i-1)
            for di in range(length):
                if np.any(pattern[i-di] != pattern[i+di+1]):
                    check_sym = False
            if check_sym:
                # sym_lines.append((i+1)*100)
                total += (i+1)*100
        
    for j in range(len(pattern[0])-1):
        if np.all(pattern[:,j] == pattern[:,j+1]):
            check_sym = True
            length = min(j+1,len(pattern[0])-j-1)
            for dj in range(length):
                if np.any(pattern[:,j-dj] != pattern[:,j+dj+1]):
                    check_sym = False
            if check_sym:
                # sym_lines.append(j+1)
                total += j+1

# print(sym_lines)
print(total)