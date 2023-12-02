import re
import time
import numpy as np

start_time = time.time()

text = ""
with open("day2.txt") as file:
    text = file.read()

possible_games = []
block_powers = []
max_blocks = np.array([12, 13, 14])
for line in text.splitlines():
    game_id = int(re.findall(r'Game (\d+):',line)[0])
    red_blocks = max(([int(x) for x in re.findall(r'(\d+) red',line)]))
    green_blocks = max(([int(x) for x in re.findall(r'(\d+) green',line)]))
    blue_blocks = max(([int(x) for x in re.findall(r'(\d+) blue',line)]))

    blocks = np.array([red_blocks, green_blocks, blue_blocks])
    block_powers.append(blocks.prod())

    if not False in (blocks <= max_blocks):
        possible_games.append(game_id) 

print("\nSolution part 1 = ",sum(possible_games))
print("Solution part 2 = ",sum(block_powers))
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))