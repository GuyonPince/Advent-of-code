import re
import time
import math
import numpy as np

LEFT, RIGHT, UP, DOWN = [(0,-1),(0,1),(-1,0),(1,0)]

start_time = time.time()
mirror_grid = np.array([list(x.replace('\n','')) for x in open('input.txt')])
rows,collumns = np.shape(mirror_grid)

def valid_index(pos):
    r,c = pos
    if 0 <= r < rows and 0 <= c < collumns:
        return True   
    return False

def move(pos,dir):
    return tuple([sum(x) for x in zip(pos,dir)])

def trace_beam(pos,dir):
    queue = [(pos,dir)]
    seen = set()
    energized = set()
    while queue:
        pos,dir = queue.pop()

        while valid_index(pos):
            if (pos,dir) in seen:
                break

            seen.add((pos,dir))
            energized.add(pos)

            item = mirror_grid[pos]
            if item == '.':
                pass
            elif item == '/':
                dir = (-dir[1],-dir[0])
            elif item == '\\':
                dir = (dir[1],dir[0])
            elif item == '-' and dir[0]:
                dir, dir2 = (dir[1],dir[0]), (-dir[1],-dir[0])
                queue.append((pos,dir2))
            elif item == '|' and dir[1]:
                dir, dir2 = (dir[1],dir[0]), (-dir[1],-dir[0])
                queue.append((pos,dir2))
            pos = move(pos,dir)
    
    return energized

def part1():
    beam = trace_beam((0,0),RIGHT)
    return len(beam)

def part2():
    beam_lengths = []
    for r in range(rows):
        beam_lengths.append(len(trace_beam((r,0),(RIGHT))))
        beam_lengths.append(len(trace_beam((r,collumns-1),(LEFT))))

    for c in range(collumns):
        beam_lengths.append(len(trace_beam((0,c),(DOWN))))
        beam_lengths.append(len(trace_beam((rows-1,c),(UP))))

    return max(beam_lengths)


print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))