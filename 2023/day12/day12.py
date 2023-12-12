import re
import time
import math
import numpy as np

start_time = time.time()

input = np.array([list(x.replace('\n','')) for x in open('sample.txt')])

def gen_string (string):
    print (string)
    if not '?' in string:
        return check_string (string)
    
    str_a = string
    str_b = string
    for i,char in enumerate(string):
        if char == '?':
            str_a[i] = '#'
            str_b[i] = '.'
            return gen_string(str_a), gen_string(str_b)
        elif char == ' ':
            break


def check_string (string):
    s, chunk_sizes = ''.join(string).split()
    chunk_sizes = eval(f'[{chunk_sizes}]')
    chunks = [len(x) for x in re.findall(r'#+', s)]
    if chunks == chunk_sizes:
        return True
    else:
        return False

def part1():
    # print (input[0])
    gen_string(input[0])
    return None

def part2():
    return None


print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))