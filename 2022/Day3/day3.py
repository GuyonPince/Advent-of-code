import time
start_time = time.time()

lines = []
with open("day3.txt") as file:
    for line in file:
        lines.append(line)

def calculate_value(x):
    val = ord(x) - 96
    if val < 1:
        val = ord(x) - 38
    return val

#Part 1
value1 = 0
for line in lines:
    backpackSize = len(line)
    middle = int(backpackSize/2)
    firstCompartment,secondCompartment  = line[:middle],line[middle:]

    for item in firstCompartment:
        if secondCompartment.__contains__(item):
            value1 += calculate_value(item)
            break

#Part 2
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

elfGroups = list(divide_chunks(lines,3))
value2 = 0
for group in elfGroups:
    for item in group[0]:
        if group[1].__contains__(item) and group[2].__contains__(item):
            value2 += calculate_value(item)
            break

print("Total value part 1 = ",value1)
print("Total value part 2= ",value2)
print("--- %s millis ---" % ((time.time() - start_time) * 1000))
