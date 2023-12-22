import numpy as np


def find_next_num_in_seqn(seqn):
    # print(seqn)
    if not any(seqn):
        # print(seqn)
        return 0
    diff = [seqn[i+1] - seqn[i] for i in range(len(seqn) - 1)]
    
    # print(seqn[-1] + find_next_num_in_seqn(diff))
    
    return seqn[-1] + find_next_num_in_seqn(diff)


with open("Day 09/data.txt", "r") as file:
    data = file.read().split("\n")
data = np.array([d.split(" ") for d in data], dtype=np.int64)
# print(data)

ans = 0
for pattern in data:
    ans += find_next_num_in_seqn(pattern)
    # print(find_next_num_in_seqn(pattern))
print(ans)