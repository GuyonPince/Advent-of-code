import re
import numpy as np
import time
from multiprocessing import Process, Queue

start_time = time.perf_counter()

text = ""
with open("day15.txt") as file:
    text = file.read()  

class sensor:
    def __init__(self,pos,s_range) -> None:
        self.pos = pos
        self.s_range = s_range

def manhattan_dist(sensor, point):
    xs,ys = sensor
    xb,yb = point
    return abs(xs-xb) + abs(ys-yb)

sb_pairs = []
sensors = []
for line in text.splitlines():
    s,b = line.split(':')
    s = tuple([int(x) for x in re.findall('-?\d+',s )])
    b = tuple([int(x) for x in re.findall('-?\d+',b )])
    s_range = manhattan_dist(s,b)
    sb_pairs.append(((s,b),s_range))
    sensors.append(sensor(s,s_range))


def in_range(s,point):  
    dist = manhattan_dist(s.pos,point)
    return dist <= s.s_range

def move_out_of_range(s,y):
    y_dif = abs(s.pos[1] - y)
    length = s.s_range - y_dif
    return s.pos[0] + length + 1 


def check_for_hole(q,y_range):
    y,y_end = y_range
    x = 0
    point_in_range = True
    while point_in_range and y < y_end:
        point_in_range = False
        for s in sensors:
            if in_range(s,(x,y)):
                x = move_out_of_range(s,y)
                point_in_range = True
                break

        if x >= y_end:
            x, y = 0, y+1

    if point_in_range:
        q.put(None)
    else:
        q.put((x,y))

def main():
    field_size = 4_000_000
    start = 0
    chunk = 250_000
    queue = Queue()
    NP = 0
    subprocesses = []
    while start < field_size:
        p = Process(target=check_for_hole, args=(queue, (start, start+chunk)))
        NP +=1
        print ('delegated %s:%s to subprocess %s' % (start, start+chunk, NP))
        p.start()
        start += chunk
        subprocesses.append(p)
        x,y = 0,0
    for _ in range(NP):
        value = queue.get()
        if value != None:
            x,y = value

    print (f'\nPart2 : frequency = {x * 4_000_000 + y} at pos x = {x}, y = {y}')

    end_time = time.perf_counter()
    print (f'exe time = {end_time - start_time} seconds\n')
    while subprocesses:
      subprocesses.pop().join()


if __name__ == '__main__':
    main()