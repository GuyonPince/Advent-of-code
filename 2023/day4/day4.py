import re
import time
import numpy as np

text = ""
with open("day4.txt") as file:
    text = file.read()

total_points = []
for line in text.splitlines():
    x, card_numbers, winning_numbers = re.findall(r'[^\||:]+',line)
    
    card_numbers = [int(x) for x in re.findall(r'\d+',card_numbers)]
    winning_numbers = [int(x) for x in re.findall(r'\d+',winning_numbers)]

    overlap = np.intersect1d(card_numbers,winning_numbers)
    points = int(2**(len(overlap)-1))
    total_points.append(points)

print (sum(total_points))