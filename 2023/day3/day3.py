import re
import time
import numpy as np


class Number:
    def __init__(self, value, start_index,length):
        self.value = int(value)
        self.start_index = start_index
        self.length = length
        self.neighbours = []

    def check_neighbours(self):
        for r in [self.start_index[0]-1,self.start_index[0],self.start_index[0]+1]:
            if r < 0: continue
            if r > max_row-1: continue
            for c in range(self.start_index[1]-1,self.start_index[1]+self.length+1):
                if c < 0: continue
                if c > max_col-1: continue
                self.neighbours.append(engine_layout[r][c])

    def is_partnumber (self):
        if all(x.isdigit() or x == '.' for x in self.neighbours):
            return False
        else:
            return True

    def add_digit (self,digit):
        self.length += 1
        self.value = self.value*10+int(digit)


start_time = time.time()

text = ""
with open("day3.txt") as file:
    text = file.read()

engine_layout = []
for line in text.splitlines():
    engine_layout.append(list(line))

engine_layout = np.array(engine_layout)
numbers = []
max_row, max_col = engine_layout.shape
num = Number(0,[0, 0],0)
new_num = True

for row in range(max_row):
    for col in range (max_col):
        if engine_layout[row][col].isdigit() and new_num:
            new_num = False
            num = Number(engine_layout[row][col],[row, col],1)
        elif engine_layout[row][col].isdigit():
            num.add_digit(engine_layout[row][col])
        elif not new_num:
            new_num = True
            num.check_neighbours()    
            numbers.append(num) 

part_numbers = []
for num in numbers:
    if num.is_partnumber():
        part_numbers.append(num.value)

print (sum(part_numbers))
