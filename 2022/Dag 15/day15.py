import re
import numpy as np
import time

start_time = time.perf_counter()

text = ""
with open("day15.txt") as file:
    text = file.read()  

class sensor:
    def __init__(self,pos,s_range) -> None:
        self.pos = pos
        self.s_range = s_range


def manhattan_dist(sensor, point):
    result = [x1 - x2 for x1, x2 in zip(point, sensor)]
    return abs(result[0]) + abs(result[1])

# line  = 'Sensor at x=8, y=7: closest beacon is at x=2, y=10'
sb_pairs = []
sensors = []
for line in text.splitlines():
    s,b = line.split(':')
    s = tuple(reversed([int(x) for x in re.findall('-?\d+',s )]))
    b = tuple(reversed([int(x) for x in re.findall('-?\d+',b )]))
    s_range = manhattan_dist(s,b)
    sb_pairs.append(((s,b),s_range))
    sensors.append(sensor(s,s_range))

# for s in sensors:
#     print (s.pos,s.s_range)


def manhattan_dist(sensor, point):
    result = [x1 - x2 for x1, x2 in zip(point, sensor)]
    return abs(result[0]) + abs(result[1])

def in_range(s,point):  
    dist = manhattan_dist(s.pos,point)
    return dist <= s.s_range

def move_out_of_range(s,y):

    y_dif = abs(s.pos[0] - y)
    length = s.s_range - y_dif
    return s.pos[1] + length + 1 

# part 1
no_beacon = []
def part1(sb,radius):
    sensor,beacon = sb
    # y_range = range(s[0]-radius,s[0]+radius+1) # full range
    # y_range = range(sensor[0],sensor[0]+1)
    # for y in y_range:
    y = 2_000_000
    # y = 10
    y_dif = abs(sensor[0]-y)
    length = radius - y_dif
    x_start,x_end = sensor[1]-length, sensor[1] + length
    # if y_dif < radius:
        # print (f'S{sensor}, B{beacon} ___> Left = {s[1]-length} Right = {s[1] + length} r = {radius}')
    for x in range(x_start,x_end+1):
        if (y,x) != sensor and (y,x) != beacon: 
            no_beacon.append((y,x))

for sb,r in sb_pairs:
    positions = part1(sb,r)

print(f'part 1 = {len(set(no_beacon))}')
end_time = time.perf_counter()
print (f'exe time = {end_time-start_time} seconds')

start_time = time.perf_counter()

x,y = 0,0
field_size = 4_000_000
point_in_range = True
while point_in_range and y < field_size:#4_000_000:
    point_in_range = False
    for s in sensors:
        if in_range(s,(y,x)):
            x = move_out_of_range(s,y)
            point_in_range = True
            break

    if x >= field_size:
        x, y = 0, y+1

print (f'Part2 : frequency = {x * 4_000_000 + y} at pos x = {x}, y = {y}')

end_time = time.perf_counter()
print (f'exe time = {end_time - start_time} seconds')

# x = np.full((30,30),'.')
# for nb in no_beacon:
#     if not any(x < 0 for x in nb):
#         x[nb] = '#'

# x = np.fliplr(np.rot90(np.rot90(np.rot90(x))))
# for row in x:
#     print (''.join(c for c in row))

# 3245601 = low
# 2887170 = low
# 5367037 = correct