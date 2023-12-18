import time
import numpy as np

LEFT, RIGHT, UP, DOWN = [(0,-1),(0,1),(-1,0),(1,0)]

start_time = time.time()
instructions = [*open('input.txt')]
direction = {'L': LEFT, 'R': RIGHT, 'U': UP, 'D': DOWN,
             '0': RIGHT,'1': DOWN, '2': LEFT, '3': UP}

# First try for part 1.
# FLoodfill, like BFS but without endpoint
# Worked, but was way to slow for part 2
def fill(bounds): 
    start_col = min([c for r, c in bounds if r == 0])
    r, c = 1, start_col +1
    queue = [(r,c)]
    filled = set()
    while queue:
        r, c = queue.pop(0)
        if (r, c) in filled or (r, c) in bounds:
            continue
        
        filled.add((r, c))

        for dr, dc in [LEFT, RIGHT, UP, DOWN]:
            nr = r + dr
            nc = c + dc
            queue.append((nr,nc))

    pool = filled.union(bounds)
    return pool

# Second attempt, Shoelace algorithm to find the erea.
# This does not include the area of the perimeter!
# 
# Each square on the perimeter contibutes 0.5 to the erea
# outside corners add 0.25, inside corners subtract 0.25
# Pick's theorem
def shoelaceArea(vertices):
    sum1 = 0
    sum2 = 0
    for i in range(len(vertices)-1):
        sum1 += vertices[i][0] * vertices[i+1][1]
        sum2 += vertices[i][1] * vertices[i+1][0]

    area = abs(sum1 - sum2) // 2 
    return area
    x = np.empty((max_r,max_c),dtype=str)
    x[:] = '.'
    lines = []
    for p in positions:
        x[p] = '#'
    # for t in trace:
    #     x[t] = '0'

    for r in range(max_r):
        lines.append(''.join(x[r]))
    f = open("map.txt", "w")
    f.write('\n'.join(lines))
    f.close()

def dig_trech(instr):
    trench = []
    r, c = 0, 0
    for i in instr:
        d, n = i    
        dr, dc = direction[d]
        r,c = r+dr*n, c+dc*n
        trench.append((r, c))
    return trench

def part1():
    instr = []
    perimeter = 0
    for i in instructions:
        d, n, _ = i.split()
        instr.append((d,int(n)))
        perimeter += int(n)
    trench = dig_trech(instr)
    area = shoelaceArea(trench)
    return area + perimeter // 2 + 1

def part2():
    instr = []
    perimeter = 0
    for i in instructions:
        val = i.split()[-1]
        val = val[1:-1].replace('#','0x')
        d, n = val[-1], int(val[:-1], 16)
        instr.append((d, n))
        perimeter += n

    trench = dig_trech(instr)
    area = shoelaceArea(trench)
    return area + perimeter // 2 + 1


print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))