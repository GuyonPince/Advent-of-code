import re
import time
import numpy as np

numbers = []
potential_gears = []

class Number:
    def __init__(self, value: int, start_index):
        self.value = value
        self.start_index = start_index
        self.length = 1
        self.neighbours = []
        self.is_partnumber = False

    # get all neighbours
    # Determine if number is a partnumber
    # determine if neighbours contain a gear

    def check_neighbours(self):
        for r in range(self.start_index[0]-1, self.start_index[0]+2):
            if r < 0 or r > max_row-1: continue
            for c in range(self.start_index[1]-1,self.start_index[1]+self.length+1):
                if c < 0 or c > max_row-1: continue
                val = engine_layout[r][c]
                self.neighbours.append(Neighbour(val,[r,c]))
                if val == '*':
                    potential_gears.append([r, c])

        if all(x.value.isdigit() or x.value == '.' for x in self.neighbours):
            self.is_partnumber = False
        else:
            self.is_partnumber = True
   
    def add_digit (self,digit):
        self.length += 1
        self.value = self.value*10+int(digit)

class Neighbour:
    def __init__(self, value, index):
        self.value = value
        self.index = index
    

start_time = time.time()

text = ""
with open("day3.txt") as file:
    text = file.read()

engine_layout = []
for line in text.splitlines():
    engine_layout.append(list(line))

engine_layout = np.array(engine_layout)
max_row, max_col = engine_layout.shape
num = None
new_num = True

# exctract all numbers and gears from engine layout
for row in range(max_row):
    for col in range (max_col):
        val = engine_layout[row][col]
        if val.isdigit() and new_num:
            new_num = False
            num = Number(int(val),[row, col])
        elif val.isdigit():
            num.add_digit(int(val))
        elif not new_num:
            new_num = True
            num.check_neighbours()    
            numbers.append(num) 

# part 1, determine part numbers
part_numbers = [x.value for x in numbers if x.is_partnumber]


### Part 2 ###
potential_gears, count = np.unique(potential_gears, return_counts=True, axis=0)

gears = []
for i,gear in enumerate(potential_gears):
    if count[i] > 1:
        gears.append(gear.tolist())
        
gear_ratios = []
for gear in gears:
    teeth = []
    for num in numbers:
        if any(x.index == gear for x in num.neighbours):
            teeth.append(num.value)
            
    gear_ratios.append (np.prod(teeth))


print ("\nSolution part 1 = ", sum(part_numbers))
print ("Solution part 2 = ", sum(gear_ratios))
print ("--- %s millis ---\n" % ((time.time() - start_time) * 1000))