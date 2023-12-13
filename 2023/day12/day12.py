import re
import time
import math
import numpy as np

start_time = time.time()

input = [list(x.replace('\n','')) for x in open('sample.txt')]

def gen_string (string):
    
    if not '?' in string:
        return check_string (string)
    
    str_a = list(string)
    str_b = list(string)
    for i,char in enumerate(string):
        if char == '?':
            str_a[i], str_b[i] = '#', '.'
            return gen_string(str_a) + gen_string(str_b)


def check_string (string):
    s, chunk_sizes = ''.join(string).split()
    chunk_sizes = eval(f'[{chunk_sizes}]')
    chunks = [len(x) for x in re.findall(r'#+', s)]
    if chunks == chunk_sizes:
        return True
    else:
        return False

def part1():
    arrangements = []
    for x in input:
        arrangements.append(gen_string(x))
    return sum(arrangements)

def part2():
    return None


print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000_000))