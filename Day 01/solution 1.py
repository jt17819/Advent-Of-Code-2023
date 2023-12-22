import numpy as np
import re

data = np.loadtxt("Day 01/data.txt", dtype=str)

sum = 0
number_map = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
for line in data:
    digits = re.findall("\d", line)
    first_digit = number_map.get(digits[0], digits[0])
    last_digit  = number_map.get(digits[-1], digits[-1])
    if first_digit and last_digit:
        sum += int(first_digit[0] + last_digit[0])

print(sum)