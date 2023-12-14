import re
import time
import math
import numpy as np

start_time = time.time()

input = np.array([list(x.replace('\n','')) for x in open('input.txt')])
sort_weight = ['#', 'O','.']


def roll_stones (field,direction):
    '''Direction 0 = north, 1 = west, 2 = south, 3 = east'''
    if direction == 0:
        field = np.array(field).T
    elif direction == 1:
        field = field
    elif direction == 2:
        field = np.flip(np.array(field).T, axis=1)
    elif direction == 3:
        field = np.flip(field, axis=1)   

    rows,_ = np.shape(field)
    rolled_field = []
    for r in range(rows):
        stones = ''.join(field[r,:])
        stone_segments = []
        last_index = 0
        for i,stone in enumerate(stones):
            if stone == '#':
                stone_segments.append(stones[last_index:i])
                last_index = i
        stone_segments.append(stones[last_index:])

        rolled = []
        for s in stone_segments:
            rolled.extend(sorted(s, key=lambda x: sort_weight.index(x)))
        rolled_field.append(rolled)

    if direction == 0:   
        return np.array(rolled_field).T
    elif direction == 1:
        return np.array(rolled_field)
    elif direction == 2:
        return np.flip(rolled_field,axis=1).T
    elif direction == 3:
        return np.flip(rolled_field,axis=1)

    return None
    
def calc_load(field):
    loads = []
    rows, collumns = np.shape(field)
    for r in range(rows):
        for c in range(collumns):
            if field[r,c] == 'O':
                loads.append (rows-r)
    
    return sum(loads)


def part1():
    rolled_field = (roll_stones(input,direction=0))
    return calc_load(rolled_field)

def part2():
    rolled_field = input
    checked_fields = []

    # Check fields for a repeating pattern
    while True:
        for i in range(4):
            rolled_field = roll_stones(rolled_field,direction=i)
        if any([np.array_equal(rolled_field,x) for x in checked_fields]):
            break
        else:
            checked_fields.append(rolled_field)

    # Extract the pattern form the checked fields
    pattern = []
    cycles = 1_000_000_000 - 1
    for i,x in enumerate(checked_fields):
        if np.array_equal(rolled_field,x):
            pattern = checked_fields[i:]
            cycles -= i
    period = len(pattern)

    return calc_load(pattern[cycles % period])


print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))