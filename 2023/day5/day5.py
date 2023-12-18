import re
import time
import numpy as np
import sys

start_time = time.time()

text = ""
with open("sample.txt") as file:
    text = file.read()

# Yield successive n-sized 
# chunks from l. 
def divide_chunks(lst, n):     
    # looping till length l 
    for i in range(0, len(lst), n):  
        yield lst[i:i + n] 

def intserctions(src,seed_map):
    s, e = s
    dest, seed_src, n = seed_map 

    mapped_ranges = []
    si, ei = max(s, se), min(e, ed)
    if si < ei:
        mapped_ranges.append((s,si))
        mapped_ranges.append((si,ei))
        mapped_ranges.append((ei,ed))
    else:
        mapped_ranges.append(s,e)

    return mapped_ranges

# part 1 algorithm
def find_endpos (location,maps):
    for map in maps:
        for steps in map:
            dest,source,n = steps
            if source <= location < source+n:
                location = dest+(location-source)
                break
    return location

def part1():
    maps = []
    seeds,*chunks = text.split("\n\n")
    seeds = list(map(int, seeds.split()[1:]))

    for chunk in chunks:
        instructions = [[int(x) for x in i[1:]] for i in re.findall(r'((\d+) (\d+) (\d+))',chunk)]
        maps.append(instructions)
        instructions = sorted(instructions, key = lambda x: x[1])

    final_locations = [find_endpos(s,maps) for s in seeds]
    return min(final_locations)

def part2():
    seeds,*chunks = text.split("\n\n")
    seeds = list(map(int, seeds.split()[1:]))

    seed_ranges = sorted([(s, s+n) for s, n in list(divide_chunks(seeds,2))])
    print (seed_ranges)

    source = seeds
    dest = []
    for chunk in chunks:
        seed_map = [[int(x) for x in i[1:]] for i in re.findall(r'((\d+) (\d+) (\d+))',chunk)]
        for m in seed_map:
            dest, src, n = m 
            
            
        print (seed_map)
    return

print("\nSolution part 1 = ",part1())
print("\nSolution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))


# 4213184 is fout