import time
import re
import numpy as np

start_time = time.time()

pairs = []
with open("day4.txt") as file:
    for line in file:
        nums = (re.split('-|,', line.rstrip()))
        nums = [int(i) for i in nums]
        nums = [nums[:2], nums[2:]]
        pairs.append(nums)

#Deel 1
def check_contain(pair):
    A, B = pair[0], pair[1]
    # A containeds B
    if (A[0] <=  B[0]) and (A[1] >= B[1]):
        #print(pair)
        return True
    # B containeds  A
    if (B[0] <=  A[0]) and (B[1] >= A[1]):
        #print(pair)⌈
        return True
    return False

#Deel 2
def check_overlap(pair):
    a, b = pair[0], pair[1]
    A = range(a[0],a[1]+1)
    B = range(b[0],b[1]+1)
    overlap = list(set.intersection(set(A) & set(B)))
    print (pair,overlap)
    if len(overlap) > 0:
        return True
    return False
      

contained_pairs = len(list(filter(check_contain,pairs)))
overlap_pairs = len(list(filter(check_overlap,pairs)))
print ("Part 1 answer = ", contained_pairs)
print ("Part 2 answer = ", overlap_pairs)
