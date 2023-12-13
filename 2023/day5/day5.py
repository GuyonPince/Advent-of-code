import re
import time
import numpy as np
import sys

start_time = time.time()

text = ""
with open("sample.txt") as file:
    text = file.read()

class seed_map():
    def __init__(self, destination, source):
        self.destination_range = destination
        self.source_range = source
        self.children = []

    def add_child(self,seed_map):
        self.children.append(seed_map)
            
# part 1 algorithm
def find_endpos (location):
    for map in maps:
        for steps in map:
            dest,source,n = steps
            if source <= location < source+n:
                location = dest+(location-source)
                break
    return location

def intserctions(ranges):
    overlap = []
    for x in ranges:
         for y in ranges:
            if not x == y:
                r = range(max(x[0], y[0]), min(x[-1], y[-1])+1)
                if len(r): overlap.append(r)
    return overlap

maps = []
locations = []
seeds,*chunks = text.split("\n\n")
seeds = list(map(int, seeds.split()[1:]))

for chunk in chunks:
    instructions = [[int(x) for x in i[1:]] for i in re.findall(r'((\d+) (\d+) (\d+))',chunk)]
    maps.append(instructions)
    instructions = sorted(instructions, key = lambda x: x[1])
    locations.append([[[dest, dest+n],[source, source+n]] for dest, source, n in instructions])

final_locations = [find_endpos(s) for s in seeds]

print("\nSolution part 1 = ",min(final_locations))
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))


# 4213184 is fout