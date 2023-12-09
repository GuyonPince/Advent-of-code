import re
import time
import math
import numpy as np

start_time = time.time()

input = [[int(x) for x in lines.split()] for lines in open('sample.txt')]

def extrapolate(value_history, end_value,right):
    diff = []
    prev_val = 0
    for i,val in enumerate(value_history):
        if i > 0:
            diff.append(val-prev_val)
        prev_val = val

    if right:
        end_value += diff[-1]
        print (value_history, end_value)
    else:
        end_value += diff[0]
        print (diff[0],end_value,value_history)

    
    if not any(diff):
        return (end_value)
    else:
        return extrapolate(diff,end_value,right)


def part1():
    end_values = []
    for i in input:
        end_values.append(i[-1]+extrapolate(i,0,True))

    return sum(end_values)

def part2():
    end_values = []
    for i in input:
        end_values.append(extrapolate(i,0,False)-i[0])

    return sum(end_values)


print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())     # 912927543 = high
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))