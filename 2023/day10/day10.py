import re
import time
import math
import numpy as np

start_time = time.time()

input = np.array([list(x.replace('\n','')) for x in open('input.txt')])

pipes = {'|':(0,0),
        '-':(0,0),
        'L':(-1,1),
        'J':(-1,-1),
        '7':(1,-1),
        'F':(1,1),
        'S':(0,0)}

def find_start(grid):
    '''Find the start position and direction of the pipe'''
    rows, collumns = np.shape(grid)
    for r in range (rows):
        for c in range (collumns):
            if grid[r,c] == 'S':
                pos =  r, c
                break
    
    start_directions = {(-1,0): '|F7', (1,0): '|LJ', (0,-1): '-LF', (0,1): '-J7'}

    for d,pipes in start_directions.items():
        pipe_pos = tuple(sum(x) for x in zip(pos, d))
        pipe = grid[pipe_pos]
        if (0 < pipe_pos[0] < rows-1) and (0 < pipe_pos[1] < collumns-1):
            if pipe in pipes:
                return pos, d


def link_pipes(grid, pos, direction):
    '''Trace the path of the pipe untill back at the start position'''
    pipe, steps = None,0
    while not pipe =='S':
        pos = tuple(sum(x) for x in zip(pos, direction))
        pipe = grid[pos]

        direction = [sum(x) for x in zip(pipes[pipe], direction)]
        steps += 1

    return steps//2


def part1():
    start_pos, direction = find_start(input)
    return (link_pipes(input, start_pos, direction))

def part2():
    return None


print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))