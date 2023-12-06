import re
import time
import numpy as np
import sys

start_time = time.time()

text = ""
with open("sample.txt") as file:
    text = file.read()

def list_chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
            
# part 1 algorithm
def find_endpos (location):
    for map in maps:
        for steps in map:
            dest,source,n = steps
            if source <= location < source+n:
                location = dest+(location-source)
                break
    return location

class seed_map():
    def __init__(self, destination, source):
        self.destination_range = destination
        self.source_range = source
        self.children = []

    def add_child(self,seed_map):
        self.children.append(seed_map)

def reverse_search(locations):
    for i in locations[::-1]:
        print (i)
    min_val = sys.maxsize    
    min_dest = None
    prev_dest = None
    first_run = True
    for location_set in locations[::-1]:
        print ("\n")
        for d,s in location_set:
            if first_run:
                if d[0] < min_val:
                    min_dest = seed_map(d,s)
                    min_val = d[0]
                    prev_dest = min_val

            else:
                if max(prev_dest.destination_range[0], s[0]) <  min(prev_dest.destination_range[-1], s[-1]):
                    prev_dest.add_child(d,s)
                elif d[0] < prev_dest.source_range:
                    prev_dest.add_child(d,s)
                    
        first_run = False


            # if prev_dest:
            #     prev_d, prev_s = prev_dest
            #     overlap = range(max(prev_d[0], s[0]), min(prev_d[-1], s[-1]))+1
            #     if (not len(overlap)) and prev_d > s:
            #         min_dest = [d,s]
            # else:
            #     if not min_dest:
            #         min_dest = [d,s]
            #     elif d < min_dest[0]:
            #         min_dest = [d,s]
            #     min_dest = seed_map(d,s)
            #     prev_dest = min_dest

        print ("*", min_dest)
        prev_dest = min_dest


def check_opverlap(seed_collections, locations):
    return
    # smallest_start = reverse_search(locations)
    # print ("-",smallest_start)  

maps = []
sources = []
destinations = []
locations = []
seeds,*chunks = text.split("\n\n")
# seeds = list(map(int, seeds.split()[1:]))

for chunk in chunks:
    instructions = [[int(x) for x in i[1:]] for i in re.findall(r'((\d+) (\d+) (\d+))',chunk)]
    maps.append(instructions)
    instructions = sorted(instructions, key = lambda x: x[1])
    locations.append([[[dest, dest+n],[source, source+n]] for dest, source, n in instructions])
    

seed_collections = list(list_chunks(list(map(int,seeds.split()[1:])),2))
seed_collections = [[x, x+n] for x,n in seed_collections]

check_opverlap(seed_collections, locations)

final_locations = [find_endpos(s) for s in map(int,seeds.split()[1:])]

print("\nSolution part 1 = ",min(final_locations))
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))


# 4213184 is fout