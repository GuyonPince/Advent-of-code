import re
import time
import math
import numpy as np

start_time = time.time()

with open("input.txt") as file:
    worflows, parts = file.read().split('\n\n')

worflows = [w for w in worflows.split()]
parts = [p for p in parts.split()]

worflow_dict = {}
for w in worflows:
    name, checks = w.split('{')
    checks = checks.replace('}',':').split(',')
    worflow_dict[name] = checks

def check_part(part):
    x, m, a, s = part
    dest = 'in'
    while dest != 'A' and dest != 'R':
        worflow = worflow_dict[dest]
        for check in worflow:
            check, d = check.split(':')
            if not d:
                dest = check
                break
            if eval(check) and d:
                dest = d
                break      

    return dest
           
def part1():
    accepted_parts = 0
    for part in parts:
        part = list(map(int, re.findall(r'\d+', part)))
        if check_part(part) == 'A':
            accepted_parts += sum(part)

    return accepted_parts

def part2():
    return None


print("\nSolution part 1 = ",part1())
print("Solution part 2 = ",part2())
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))