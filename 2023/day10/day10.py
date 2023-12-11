import re
import time
import math
import numpy as np
import cv2 as cv

start_time = time.time()

input = np.array([list(x.replace('\n','')) for x in open('input.txt')])
pipeline = []

pipe_directions = {'|':(0,0),
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
                start_pos =  r, c
                break
    
    start_directions = {(-1,0): '|F7', (1,0): '|LJ', (0,-1): '-LF', (0,1): '-J7'}

    directions = []
    for direction,pipes in start_directions.items():
        pipe_pos = tuple(sum(x) for x in zip(start_pos, direction))
        pipe = grid[pipe_pos]
        if (0 <= pipe_pos[0] < rows) and (0 <= pipe_pos[1] < collumns):
            if pipe in pipes:
                directions.append(direction)
                
    return start_pos, directions


def link_pipes(grid, pos, direction):
    '''Trace the path of the pipe untill back at the start position'''
    pipe, steps = None,0
    while not pipe =='S':
        pipeline.append(pos)
        pos = tuple(sum(x) for x in zip(pos, direction))
        pipe = grid[pos]
        
        direction = tuple(sum(x) for x in zip(pipe_directions[pipe], direction))
        steps += 1

    return steps//2

def find_enclosed_positions(grid):
    '''For each position in the grid, determine if the position is enclosed by the loop.
    A position is enclosed if it passes throuh the pipe en uneven amount of times'''
    rows, collumns = np.shape(grid)
    barriers = ['JL''7F','FJ','L7']
    non_barriers = ['LJ', 'F7']
    enclosed_positions = []
    for r in range (rows):
        passes = 0
        previous_val = '.'     
        for c in range (collumns):
            val = grid[r,c]
            if val == '-':
                continue

            if val == '.' and passes % 2:
                enclosed_positions.append((r,c))
            
            if val == '|' or previous_val+val in barriers:
                passes += 1

            if previous_val+val in non_barriers or previous_val+val in barriers:
                previous_val = '.'
            else:    
                previous_val = val

    return enclosed_positions



def part1():
    start_pos, directions = find_start(input)
    return (link_pipes(input, start_pos, directions[0]))

def part2():
    _, directions = find_start(input)

    # replace S with the appropiate pipe piece
    s_placeholder = {((-1,0),(1,0)): '|',
                     ((0,-1),(0,1)): '-',
                     ((-1,0),(0,1)): 'L',
                     ((-1,0),(0,-1)): 'J',
                     ((1,0),(0,-1)): '7',
                     ((1,0),(0,1)): 'F',}
    
    s = s_placeholder[tuple(directions)]

    rows, collumns = np.shape(input)
    filtered_input = np.zeros_like(input)

    # remove all useless pipes
    for r in range (rows):
        for c in range (collumns):
            if (r,c) in pipeline:
                if input[r,c] == 'S':
                    filtered_input[r,c] = s
                else:
                    filtered_input[r,c] = input[r,c]
            else:
                filtered_input[r, c] = '.'

    enclosed = find_enclosed_positions(filtered_input)
    return len(enclosed)
    

print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))