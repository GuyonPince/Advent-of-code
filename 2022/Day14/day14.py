import numpy as np
np.set_printoptions(threshold=np.inf)
import re
import ast

class sand:
    global rocks
    global sand_at_rest
    global cave_shape

    def __init__(self,pos) -> None:
        self.pos = pos
        self.atrest = False
        self.to_the_abbys = False

    def fall(self,pos):
        y,x = pos
        floor = (y+1,x)
        left = (y+1,x-1)
        right = (y+1,x+1)

        if y >= cave_shape[0]-2:
            self.to_the_abbys = True
            return None
        elif floor not in rocks and floor not in sand_at_rest:
            self.pos = floor
            return self.fall(floor)
        elif left not in rocks and left not in sand_at_rest:
            self.pos = left
            return self.fall(left)
        elif right not in rocks and right not in sand_at_rest:
            self.pos = right
            return self.fall(right)
        else:
            self.atrest = True

rocks = []
sand_at_rest = []
faling = []
def draw_trace(trace):
    for idx,_ in enumerate(trace[:-1]):
        y_start,x_start = np.array(trace[idx])
        y_end,x_end = np.array(trace[idx+1])
    
        if y_start > y_end:
            y_start, y_end = y_end, y_start
        if x_start > x_end:
            x_start, x_end = x_end, x_start
        if y_start == y_end:
            for y in range(x_start,x_end+1):
                rocks.append((y_start,y))        
        elif x_start == x_end:
            for x in range(y_start,y_end+1):
                rocks.append((x,x_start))                         

def print_visualisation():
    x = np.full(cave_shape,'.')
    x[source] = '+'
    for r in rocks:
        x[r] = '#'
    for s in sand_at_rest[:-1]:
        x[s] = 'o'
    x[sand_at_rest[-1]] = '0'
    for l in x[:,480:600]:
        print (''.join(l))


text = ""
with open("day14.txt") as file:
    text = file.read()  

traces = []
cave_shape = [0,0]
for line in text.splitlines():
    trace = [tuple(reversed(ast.literal_eval(x))) for x in line.split(' -> ')]
    traces.append(tuple(reversed(trace)))
    for t in trace:
        if t[0] > cave_shape[0]: cave_shape[0] = t[0]+1
        if t[1] > cave_shape[1]: cave_shape[1] = t[1]+1

cave_shape = (cave_shape[0]+2,cave_shape[1]+2)

for trace in traces:
    draw_trace(trace)
print (cave_shape)

print(len(sand_at_rest))
# falling sand:
overflowing = False
source = (0,500)
while not overflowing:
# for _ in range(25):
    s = sand(source)
    s.fall(s.pos)
    if s.atrest: 
        sand_at_rest.append(s.pos)
    overflowing = s.to_the_abbys

print_visualisation()
print (len(sand_at_rest))
# 1069 = High
# 507 = Low
# 1068 is goed