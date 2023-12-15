import re
import time
import math
import numpy as np

start_time = time.time()

input = [*open('input.txt')][0]
initialization_sequence = input.split(',')

class Lens:
    def __init__(self,label,focal_length) -> None:
        self.label = label
        self.focal_length = int(focal_length)

class Box:
    def __init__(self, index):
        self.index = index
        self.lenses = []

    def add_lens(self,new_lens):
        for slot,lens in enumerate(self.lenses):
            if lens.label == new_lens.label:
                self.lenses[slot] = new_lens
                return
        self.lenses.append(new_lens)

    def remove_lens(self,label):
        for lens in self.lenses:
            if lens.label == label:
                self.lenses.remove(lens)

    def focal_length(self):
        focal_length = 0
        for slot,lens in enumerate(self.lenses):
            focal_length += lens.focal_length * (slot+1) * self.index
        return focal_length

def hash(string):
    hash_values = 0
    for char in string:
        hash_values += ord(char)
        hash_values = (hash_values*17) % 256
    return hash_values

def part1():
    hash_values = []
    for step in initialization_sequence:
        hash_values.append(hash(step))
    return sum(hash_values)

def part2():
    boxes = [Box(i+1) for i in range(256)]
    
    for step in initialization_sequence:
        label,f_len = re.split('[-=]',step)
        box_num = hash(label)
        if f_len:
            boxes[box_num].add_lens(Lens(label,f_len))
        else:
            boxes[box_num].remove_lens(label)

    focal_length = 0
    for box in boxes:
        f = box.focal_length()
        focal_length += f
    return focal_length


print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))