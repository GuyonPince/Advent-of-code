import re
import time
import math
import numpy as np

start_time = time.time()

input = [[int(x) for x in lines.split()] for lines in open('input.txt')]

def extrapolate(value_history,part):
    prev_val, diff = 0, []
    for i,val in enumerate(value_history):
        if i > 0:
            diff.append(val-prev_val)
        prev_val = val
    
    if not any(diff):
        return 0
    else:
        if part == 1:
            return extrapolate(diff,part1) + diff[-1]
        else:
            return diff[0] - extrapolate(diff,part1)


def part1():
    end_values = []
    for i in input:
        end_values.append(i[-1]+extrapolate(i,part=1))

    return sum(end_values)

def part2():
    end_values = []
    for i in input:
        end_values.append(i[0] - extrapolate(i,part=2))

    return sum(end_values)


print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())     # 385450922 = high
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))
