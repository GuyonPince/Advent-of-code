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


def lists_equal(a,b):
    rows, collumns = np.shape(a)
    count = 0
    for r in range(rows):
        for c in range(collumns):
            if not a[r,c] == b[r,c]:
                count+=1
    if count == 0:
        return True, False
    elif count == 1:
        return True, True
    else:
        return False, False 

def find_mirror(field):
    rows, collumns = np.shape(field)
    mirrors = 0
    smudged_mirrors = 0
    for r in range(1,rows):
        left_margin, right_margin  = r, (rows - r-1)

        if left_margin <= right_margin:
            left = field[:r,:]
            right = field[r:r+left_margin,:]
        elif left_margin > right_margin:
            left = field[r-right_margin-1:r,:]
            right = field[r:,:]

        equal, smudged = lists_equal(left, np.flip(right,axis=0))
        if equal:
            if smudged:
                smudged_mirrors += r*100
            else:
                mirrors += r*100


    for c in range(1,collumns):
        left_margin, right_margin  = c, (collumns - c - 1)     

        if left_margin <= right_margin:
            left = field[:,:c]
            right = field[:,c:c+left_margin]
        elif left_margin > right_margin:
            left = field[:,c-right_margin-1:c]
            right = field[:,c:]
            
        equal, smudged = lists_equal(left, np.flip(right,axis=1))
        if equal:
            if smudged:
                smudged_mirrors += c
            else:
                mirrors += c
                

 
    # if mirrors == 0:
    #     for l in field:
    #         print (''.join(l))
    #     print ('\n')
    return mirrors, smudged_mirrors

def part1():
    mirrors = []
    for field in fields:
        mirrors.append(find_mirror(field)[0])

    return sum(mirrors)

def part2():
    smudged_mirrors = []
    for field in fields:
        smudged_mirrors.append(find_mirror(field)[1])

    return sum(smudged_mirrors)

print("\nSolution part 1 = ",part1()) # 27505
print("Solution part 2 = ",part2()) # 22906
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))