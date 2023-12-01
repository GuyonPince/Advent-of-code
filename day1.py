import re
import time

start_time = time.time()

text = ""
with open("day1.txt") as file:
    text = file.read()


#### PART 1a ###
calibration_values_raw = []

for line in text.splitlines():
    calibration_values_raw.append([int(x) for x in re.findall(r'\d',line)])

calibration_val1 = 0
for values in calibration_values_raw:
    if len(values) > 1:
        calibration_val1 += values[0]*10 + values[-1]
    else:
        calibration_val1 += values[0]*11

### PART 1b ###
# calibration_val1 = 0
# for line in text.splitlines():
#     first_digit = 0
#     last_digit = 0
#     for char in line:
#         if not char.isdigit():
#             continue
#         if first_digit == 0:
#             first_digit = int(char)
#             last_digit = int(char)
#         else:
#             last_digit = int(char)
    
#     calibration_val1 += first_digit*10 + last_digit


### PART 2 ###
calibration_val2 = 0
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


    first_digit = 0
    last_digit = 0
    for char in line:
        if not char.isdigit():
            continue
        if first_digit == 0:
            first_digit = int(char)
            last_digit = int(char)
        else:
            last_digit = int(char)
    
    calibration_val2 += first_digit*10 + last_digit
    # print (line, first_digit,last_digit)


print("Solution part 1 = ", calibration_val1)
print("Solution part 2 = ", calibration_val2)
print("--- %s millis ---" % ((time.time() - start_time) * 1000))

### Deel 2 
# 55194 fout
# 55686 goed