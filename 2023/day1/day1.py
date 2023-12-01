import re
import time

start_time = time.time()

text = ""
with open("day1.txt") as file:
    text = file.read()

#### PART 1a ###
# Extract numbers using regex
# running total
calibration_val = 0
for line in text.splitlines():
    values = ([int(x) for x in re.findall(r'\d',line)])

    if len(values) > 1:
        calibration_val += values[0]*10 + values[-1]
    else:
        calibration_val += values[0]*11

print("\nSolution part 1 = ", calibration_val)
print("--- %s millis ---" % ((time.time() - start_time) * 1000))

### PART 2 ###
# this time no regex, but check for digits in each line
# keep track of only first and last digits. running total
calibration_val = 0
for line in text.splitlines():
    line = line.replace("one","o1e")
    line = line.replace("two","t2o")
    line = line.replace("three","t3e")
    line = line.replace("four","f4r")
    line = line.replace("five","f5e")
    line = line.replace("six","s6x")
    line = line.replace("seven","s7n")
    line = line.replace("eight","e8t")
    line = line.replace("nine","n9e")

    first_digit, last_digit = 0, 0
    for char in line:
        if not char.isdigit():
            continue
        if first_digit == 0:
            first_digit = int(char)
            last_digit = int(char)
        else:
            last_digit = int(char)
    
    calibration_val += first_digit*10 + last_digit

print("\nSolution part 2 = ", calibration_val)
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))

### Deel 2 
# 55194 fout
# 55686 goed
