import re
import time
import math
import numpy as np

start_time = time.time()

nodes_dict = {}

instructions,*nodes = [*open('input.txt')]
instructions = instructions.replace('L','0').replace('R','1')
instructions = [int(i) for i in instructions if i.isdigit()]

#start and end for part 2
start_positions = []

for n in nodes:
    if n.split():
        node_id, l, r = re.findall(r'[A-Z\d]+', n)
        nodes_dict[node_id] = [l, r]
        if node_id[-1] == 'A':
            start_positions.append(node_id)

# part 1
def part1():
    pos = 'AAA'
    steps = 0
    while not pos == 'ZZZ':
        x = instructions[steps % len(instructions)]
        pos = nodes_dict[pos][x]
        steps+=1
    return steps


# Part 2, first try: brute force. took way to long
# second try, with a hint from reddit: LCM. For each start point determine the steps to the first point ending wiht Z
def part2(): 
    steps_list = []
    for pos in start_positions:
        steps = 0
        while not pos[-1] == 'Z':   
            x = instructions[steps % len(instructions)]
            pos = nodes_dict[pos][x]
            steps+=1
        steps_list.append(steps)
    return math.lcm(*steps_list)

print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))