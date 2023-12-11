import re
import time
import math
import numpy as np

start_time = time.time()

input = np.array([list(x.replace('\n','')) for x in open('input.txt')])

def expand_skymap(skymap,expansion_factor):
    rows, collumns = np.shape(skymap)
    expansion_factor = int(expansion_factor-1)

    rows_to_add = []
    cols_to_add = []
    for r in range(rows):
        if all([x=='.' for x in skymap[r,:]]):
            rows_to_add.append(r)
    for c in range(collumns):
        if all([x=='.' for x in skymap[:,c]]):
            cols_to_add.append(c)

    for i,r in enumerate(rows_to_add):
        r = r+i*expansion_factor
        for n in range(expansion_factor):
            skymap = np.insert(skymap,r,'.',axis=0)
    for i,c in enumerate(cols_to_add):
        c = c+i*expansion_factor
        for n in range(expansion_factor):
            skymap = np.insert(skymap,c,'.',axis=1)

    return skymap

def find_galaxys(skymap):
    rows, collumns = np.shape(skymap)
    galaxys = []
    for r in range(rows):
        for c in range(collumns):
            if skymap[r,c] == '#':
                galaxys.append((r,c))
    print ('found the galaxys!')
    return galaxys

def measure(a,b):
    difference = np.diff([a,b],axis=0)[0]
    # print(a,b, abs(sum(difference)))
    return sum([abs(x) for x in difference])


def part1():
    skymap = expand_skymap(input,2)
    galaxys = find_galaxys(skymap)
    # for l in skymap:
    #     print (''.join(l))
    total_distance = 0
    while galaxys:      
        galaxy = galaxys.pop()
        for g in galaxys:
            total_distance += measure(galaxy,g)
    return total_distance

def part2():
    skymap = expand_skymap(input,1e6)
    galaxys = find_galaxys(skymap)

    total_distance = 0
    while galaxys:      
        galaxy = galaxys.pop()
        for g in galaxys:
            total_distance += measure(galaxy,g)
    return total_distance




print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))