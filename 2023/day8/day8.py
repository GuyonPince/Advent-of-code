import re
import time
import numpy as np

start_time = time.time()

nodes_dict = {}

instructions,*nodes = [*open('input.txt')]
instructions = instructions.replace('L','0').replace('R','1')
instructions = [int(i) for i in instructions if i.isdigit()]

#start and end for part 1
start = 'AAA'
end = 'ZZZ'

#start and end for part 2
start_positions = []

for n in nodes:
    if n.split():
        node_id, l, r = re.findall(r'[A-Z\d]+', n)
        nodes_dict[node_id] = [l, r]
        if node_id[-1] == 'A':
            start_positions.append(node_id)

# part 1
steps1 = 0
while not start == end:
    x = instructions[steps1 % len(instructions)]
    start = nodes_dict[start][x]
    steps1+=1
print("\nSolution part 1 = ",steps1)
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))
start_time = time.time()

# part 2 
steps2 = 0
while True:
    end_positions = []
    for i,p in enumerate(start_positions):
        x = instructions[steps2 % len(instructions)]
        end_positions.append(nodes_dict[p][x])
    start_positions = end_positions
    steps2+=1
    if all([endpos[-1]=='Z' for endpos in end_positions]):
        break
    


print("Solution part 2 = ",steps2)
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))