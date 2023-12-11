import re
import time
import math
import numpy as np

start_time = time.time()

input = np.array([list(x.replace('\n','')) for x in open('sample.txt')])

def expand_skymap(skymap):
    rows, collumns = np.shape(skymap)

    rows_to_add = []
    cols_to_add = []
    for r in range(rows):
        if all([x=='.' for x in skymap[r,:]]):
            rows_to_add.append(r)
    for c in range(collumns):
        print (skymap[:,c])
        if all([x=='.' for x in skymap[:,c]]):
            cols_to_add.append(c)

    for i,r in enumerate(rows_to_add):
        skymap = np.insert(skymap,r+i,'.',axis=0)
    for i,c in enumerate(cols_to_add):
        skymap = np.insert(skymap,c+i,'.',axis=1)

    return skymap

def find_galaxys(skymap):
    rows, collumns = np.shape(skymap)
    galaxys = []
    for r in range(rows):
        for c in range(collumns):
            if skymap[r,c] == '#':
                galaxys.append((r,c))
    return galaxys

def measure(a,b):
   
    difference = np.diff([a,b],axis=0)[0]
    print(a,b, abs(sum(difference)))
    return abs(sum(difference))


def part1():
    skymap = expand_skymap(input)
    galaxys = find_galaxys(skymap)
    
    total_distance = 0
    while galaxys:      
        galaxy = galaxys.pop()
        for g in galaxys:
            total_distance += measure(galaxy,g)
    return total_distance

def part2():
    return None


print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))