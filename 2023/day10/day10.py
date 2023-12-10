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
        'F':(1,1)}

def find_start(grid):
    rows, collumns = np.shape(grid)
    for r in range (rows):
        for c in range (collumns):
            if grid[r,c] == 'S':
                start_row, start_col =  r, c
                break

    if start_row > 0:
        if grid[start_row-1][start_col] in '|F7':
            direction = (-1,0)
            return (start_row,start_col), direction
    if start_row < rows-1:        
        if grid[start_row+1][start_col] in '|LJ':
            direction = (1,0)
            return (start_row,start_col), direction
    if start_col > 0:
        if grid[start_row][start_col-1] in '-LF':
            direction = (0,-1)
            return (start_row,start_col), direction
    if start_col < collumns-1:        
        if grid[start_row][start_col+1] in '-J7':
            direction = (0,1)
            return (start_row,start_col), direction

def link_pipes(grid, start_pos, direction):
    pipe_path = [start_pos]
    r, c = [sum(x) for x in zip(start_pos, direction)]
    pos = grid[r][c]
    
    steps = 1
    while not pos =='S':
        new_dir = [sum(x) for x in zip(pipes[pos], direction)]
        direction = [x//abs(x) if not x == 0 else 0 for x in new_dir ]

        r, c = [sum(x) for x in zip((r,c), direction)]
        pos = grid[r][c]
        steps += 1
        # pipe_path.append (r,c)

    return steps//2

def part1():
    start_pos, direction = find_start(input)
    return (link_pipes(input, start_pos, direction))


def part2():
    return None


print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))