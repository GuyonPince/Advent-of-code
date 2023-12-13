import re
import time
import math
import numpy as np

start_time = time.time()

with open("input.txt") as file:
    input = file.read().split('\n\n')

input = [f.splitlines() for f in input]
fields = []
for field in input:
    fields.append(np.array([list(x) for x in field]))


class mirror:
    def __init__(self,value,smudged) -> None:
        self.value = value
        self.smudged = smudged 

def lists_equal(a,b):
    rows, collumns = np.shape(a)
    count = 0
    for r in range(rows):
        for c in range(collumns):
            if not a[r,c] == b[r,c]:
                count+=1
    if count == 0: # clean mirror
        return True, False
    elif count == 1: # smudged mirror
        return True, True
    else: #no mirror
        return False, False 

def find_mirror(field):
    rows, collumns = np.shape(field)
    mirrors = []
    for r in range(1,rows):
        left_margin, right_margin  = r, (rows - r-1)

        if left_margin <= right_margin:
            left = field[:r,:]
            right = field[r:r+left_margin,:]
        elif left_margin > right_margin:
            left = field[r-right_margin-1:r,:]
            right = field[r:,:]

        mir, smudged = lists_equal(left, np.flip(right,axis=0))
        if mir:
            mirrors.append(mirror(r*100,smudged))

    for c in range(1,collumns):
        left_margin, right_margin  = c, (collumns - c - 1)     

        if left_margin <= right_margin:
            left = field[:,:c]
            right = field[:,c:c+left_margin]
        elif left_margin > right_margin:
            left = field[:,c-right_margin-1:c]
            right = field[:,c:]
            
        mir, smudged = lists_equal(left, np.flip(right,axis=1))
        if mir:
            mirrors.append(mirror(c,smudged))
                
    return mirrors


mirrors = []
for field in fields:
     mirrors.extend(find_mirror(field))

def part1():
    total_value = sum([mir.value for mir in mirrors if mir.smudged == False])
    return total_value

def part2():
    total_value = sum([mir.value for mir in mirrors if mir.smudged])
    return total_value

print("\nSolution part 1 = ",part1()) # 27505
print("Solution part 2 = ",part2()) # 22906
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))