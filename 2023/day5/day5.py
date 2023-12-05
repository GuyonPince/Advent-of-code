import re
import time
import numpy as np
from multiprocessing import Pool

start_time = time.time()

text = ""
with open("day5.txt") as file:
    text = file.read()

                
def find_endpos (location):
    for map in maps:
        for steps in map:
            dest,source,n = steps
            if source <= location < source+n:
                location = dest+(location-source)
                break
    return location


maps = []
if __name__ == '__main__':
    seeds = []

    seeds,*chunks = text.split("\n\n")
    # seeds = list(map(int, seeds.split()[1:]))

    for chunk in chunks:
        instructions = [[int(x) for x in i[1:]] for i in re.findall(r'((\d+) (\d+) (\d+))',chunk)]
        maps.append(instructions)

    final_locations = [find_endpos(s) for s in map(int,seeds.split()[1:])]

    
    print("\nSolution part 1 = ",min(final_locations))
    # print("Solution part 2 = ",sum(total_cards))
    print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))


# 4213184 is fout