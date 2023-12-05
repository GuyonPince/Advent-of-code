import re
import time
import numpy as np
from multiprocessing import Pool

start_time = time.time()

text = ""
with open("day5.txt") as file:
    text = file.read()

class Seed_map:

    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions
        self.destinations = []
        self.sources = []
        
        self.create_list()

    def create_list(self):
        for i in self.instructions:
            destination, source, steps = i

            self.destinations.append(range(destination, destination + steps))
            self.sources.append(range(source,source + steps))

    def next_position(self, position):
        for i,source in enumerate(self.sources):
            for index, value in enumerate(source):
                if position == value:
                    return self.destinations[i][index]
        return position

                
def find_endpos (seed):
    position = seed
    for map in maps:
        position = map.next_position(position)
    return position



maps = []
if __name__ == '__main__':
    seeds = []

    chunks = text.split("\n\n")
    seeds = [int(x) for x in re.findall(r'\d+',chunks[0])]
    for chunk in chunks[1:]:
        name = re.findall(r'(\w+-\w+-\w+)',chunk)[0]
        instructions = [[int(x) for x in i[1:]] for i in re.findall(r'((\d+) (\d+) (\d+))',chunk)]

        maps.append(Seed_map(name,instructions))

    final_locations = []
    with Pool(1) as p:
        final_locations = p.map(find_endpos, seeds)
    
        print("\nSolution part 1 = ",min(final_locations))
        # print("Solution part 2 = ",sum(total_cards))
        print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))


# 4213184 is fout