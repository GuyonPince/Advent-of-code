import re
import time
from heapq import heappush, heappop

start_time = time.time()

LEFT, RIGHT, UP, DOWN = [(0,-1),(0,1),(-1,0),(1,0)]

start_time = time.time()
city_map = [list(map(int,line.strip())) for line in open('input.txt')]

rows = len(city_map)
collumns = len(city_map[0])

def valid_index(r,c):
    if 0 <= r < rows and 0 <= c < collumns:
        return True   
    return False

def bfs(min_n, max_n):
    heat_loss, r, c, dr, dc, n = 0, 0, 0, 0, 0, 0
    
    queue = [(heat_loss, r, c, dr, dc, n)]
    seen = set()

    while queue:
        heat_loss, r, c, dr, dc, n = heappop(queue)

        if (r,c) == (rows-1,collumns-1) and n >= min_n:
            break
        
        if (r, c, dr, dc, n) in seen:
            continue
        
        # DONT INCLUDE THE VALUE FOR CHECKING IN THE SEEN SET !!!
        # IN THIS CASE HEAT_LOSS
        seen.add((r, c, dr, dc, n)) 

        for ndr, ndc in [UP, LEFT, DOWN, RIGHT]:
            nr = r + ndr
            nc = c + ndc
            if not valid_index(nr,nc):
                continue

            if (ndr, ndc) == (dr, dc):
                if n < max_n:
                    heappush(queue,(heat_loss + city_map[nr][nc], nr, nc, ndr, ndc, n+1))
                continue
            if n >= min_n or (dr, dc) == (0, 0):
                if (ndr, ndc) != (-dr,-dc) :
                    heappush(queue,(heat_loss + city_map[nr][nc], nr, nc, ndr, ndc, 1))

    return heat_loss

def part1():
    return bfs(0,3)
def part2():
    return bfs(4,10)


print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))