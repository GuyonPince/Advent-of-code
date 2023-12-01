import collections
import numpy as np
import asyncio
import time
from math import sqrt

start_time = time.perf_counter()
text = ""
with open("day12.txt") as file:
    text = file.read()

height_map = np.array([list(line) for line in text.splitlines()])
max_lat,max_lon = height_map.shape
# Determine the start end end positions
start_pos = [0,0]
end_pos = [0,0]
for lat,row in enumerate(height_map):
    for lon,item in enumerate(row):
        if height_map[lat,lon] == 'S':
            # hight_map[lat,lon] = 'a' # deze had ik nodig voor de eerste poging
            start_pos = [lat,lon]
        elif height_map[lat,lon] == 'E':
            # hight_map[lat,lon] = 'z' # deze had ik nodig voor de eerste poging
            end_pos = [lat,lon]



#%% first try, didn't work for large data set
map_size = list(height_map.shape)
def options(pos,_visited,check):
    global height_map
    lat,lon = pos
    value = ord(height_map[lat,lon])
    left = [lat,lon-1]
    right = [lat,lon+1]
    up = [lat-1,lon]
    down = [lat+1,lon]
    option_list = list(filter(lambda x: not( -1 in x ) and (x[0] < map_size[0] and x[1] < map_size[1]),[left,right,up,down]))
    if check:
        option_list = list(filter(lambda x:not(x in _visited),option_list))
    option_list = list(filter(lambda x: ord(height_map[x[0]][x[1]]) <= value+1,option_list))
    return option_list

def distance_to_target(pos):
    global end_pos
    dif = np.subtract(end_pos,pos)
    if any(dif):
        return sqrt((dif[0])**2 + (dif[1])**2)
    return 0

def distance_to_target(pos):
    global end_pos
    dif = np.subtract(end_pos,pos)
    if any(dif):
        return sqrt((dif[0])**2 + (dif[1])**2)
    return 0


succesfull_path = []
def walk_path(pos,path,skip_double_steps,visited):
    global succesfull_path
    visited.append(pos)
    temp_visited = [x for x in visited]

    if len(options(pos,visited,skip_double_steps)):
        for option in sorted(options(pos,visited,skip_double_steps),key=lambda x: distance_to_target(x)): 
            temp_path = [x for x in path] 
            temp_path.append(option)
            temp_visited.append(option)
            # visited.append(option)
            if option == end_pos:
                print (f'found a path!, it took {len(temp_path)} steps!')
                succesfull_path = temp_path # Arrived
                return
            if len(temp_path) + distance_to_target(option) < len(succesfull_path) or len(succesfull_path) == 0:
                if option in path:
                    pass # Path backtracking or running in circles
                else:
                    walk_path(option,temp_path,skip_double_steps,temp_visited)# Simulate next steps

# print ('\nGoing on a big inefficient walk...')
# walk_path(start_pos,[],True,[])
# print (f'Shotest path = {len(succesfull_path)}')

#%% BFS is the way to go, hints van redit bekeken want ik kwam er zelf niet uit...
def bfs(grid, start,end_val):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        lat, lon = path[-1]
        if grid[lat][lon] == end_val:
            print('found the end point!')
            return path[:-1]

        for lat2, lon2 in ((lat+1,lon), (lat-1,lon), (lat,lon+1), (lat,lon-1)):
            if lat2 >= max_lat or lat2 < 0  or lon2 >= max_lon or lon2 < 0:
                continue
            
            value = grid[lat2][lon2]
            prev_val = grid[lat][lon]
            if value == 'S':
                value = 'a'
            if value == 'E':
                value = 'z'
            if prev_val == 'S':
                prev_val = 'a'
            if prev_val == 'E':
                prev_val = 'z'

            if ord(value) <= ord(prev_val)+1 and (lat2, lon2) not in seen and end_val == 'E':
                queue.append(path + [(lat2, lon2)])
                seen.add((lat2, lon2))
            if (ord(value) >= ord(prev_val) or ord(value) == ord(prev_val)-1) and (lat2, lon2) not in seen and end_val == 'a':

                queue.append(path + [(lat2, lon2)])
                seen.add((lat2, lon2))



print ('\nGoing on a walk...')
succesfull_path = bfs (height_map,tuple(start_pos),'E')
print (f'Shotest path from start point is {len(succesfull_path)} steps')

print ('\nFinding a hiking path...')
succesfull_path = bfs (height_map,tuple(end_pos),'a')
print (f'The hiking path is {len(succesfull_path)} steps')

end_time = time.perf_counter()
print (f'\n---- duration = {end_time - start_time}')