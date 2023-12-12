import re
import time
import math
import numpy as np

start_time = time.time()

input = np.array([list(x.replace('\n','')) for x in open('input.txt')])


def expand_skymap(skymap,expansion_factor):
    '''Expand the actual skymap, good for part 1, not so much part 2...'''
    empty_rows, empty_cols = find_empty(skymap)
    expansion_factor = int(expansion_factor-1)

    for i,r in enumerate(empty_rows):
        r = r+i*expansion_factor
        for n in range(expansion_factor):
            skymap = np.insert(skymap,r,'.',axis=0)
    for i,c in enumerate(empty_cols):
        c = c+i*expansion_factor
        for n in range(expansion_factor):
            skymap = np.insert(skymap,c,'.',axis=1)

    return skymap


def find_empty(skymap):
    '''Find emptry rows and collumns in the skymap'''
    rows, collumns = np.shape(skymap)
    empty_rows = []
    empty_cols = []
    for r in range(rows):
        if all([x=='.' for x in skymap[r,:]]):
            empty_rows.append(r)
    for c in range(collumns):
        if all([x=='.' for x in skymap[:,c]]):
            empty_cols.append(c)

    return empty_rows, empty_cols

def find_galaxys(skymap):
    '''Find galaxies in the skymap'''
    rows, collumns = np.shape(skymap)
    galaxys = []
    for r in range(rows):
        for c in range(collumns):
            if skymap[r,c] == '#':
                galaxys.append((r,c))
    return galaxys

def find_galaxys_expand(skymap,expansion_factor):
    '''Find galaxies in the skymap.
        Apply expansion factor to the empty spaces'''
    rows, collumns = np.shape(skymap)
    expansion_factor = int(expansion_factor-1)
    empty_rows, empty_cols = find_empty(skymap)

    galaxys = []
    row_offset = 0 
    for r in range(rows):
        if r in empty_rows:
            row_offset += expansion_factor
        col_offset = 0
        for c in range(collumns):
            if c in empty_cols:
                col_offset = (empty_cols.index(c)+1) * expansion_factor
            if skymap[r,c] == '#':
                galaxys.append((r+row_offset,c+col_offset))

    return galaxys

def measure_distance(a,b):
    '''Retruns the distance from a to b. a and b are tuple of (row,col)'''
    difference = np.diff([a,b],axis=0)[0]
    return sum([int(abs(x)) for x in difference])


def part1():
    skymap = expand_skymap(input,2)
    galaxys = find_galaxys(skymap)

    total_distance = 0
    while galaxys:      
        galaxy = galaxys.pop()
        for g in galaxys:
            total_distance += measure_distance(galaxy,g)
    return total_distance

def part2():
    galaxys = find_galaxys_expand(input,1e6)

    total_distance = 0
    while galaxys:      
        galaxy = galaxys.pop()
        for g in galaxys:
            total_distance += measure_distance(galaxy,g)
    return total_distance

print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))