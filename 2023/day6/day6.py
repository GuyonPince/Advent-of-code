import re
import time
import numpy as np

start_time = time.time()

# part1
t, distance = [[int(x) for x in lines.split() if x.isdigit()] for lines in open('input.txt')]
# part2
t2,distance2 = [int(lines.replace(' ','').split(':')[1]) for lines in open('input.txt')]

races = list(zip(t, distance))

#part 2, small optimalisation by qitting after distance is no longer greater than the reccord
def calc_wins(t, record_distance):
    possible_wins = 0
    first_loop = True
    for press_time in range(1,t):
        distance = press_time*(t-press_time)
        if distance > record_distance:
            possible_wins += 1
            first_loop = False
        elif not first_loop:
            return possible_wins

margin = []
for t,record_distance in races:
    wins = [press_time*(t-press_time) for press_time in range(1,t) if press_time*(t-press_time) > record_distance]
    margin.append(len(wins))

calc_wins(t2,distance2)


print("\nSolution part 1 = ",np.prod(margin))
print("\nSolution part 2 = ",calc_wins(t2,distance2))
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))