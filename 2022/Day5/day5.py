import time
import re
import numpy as np

start_time = time.time()

text = ""
with open("day5.txt") as file:
    text = file.read()

# Fill instruction list
instructions = []
for line in text.splitlines():
    # Get all int's from each line
    instruction =  [int(x) for x in re.findall(r"[\d]+",line)]
    # if line contains 3 strings, add to instruction list
    if len(instruction) == 3:
        instructions.append(instruction)      

# Extract the crate structure form the first 9 lines, replace all 4 consecutive spaces with a single space
# Split each line at each space, now every item in each row is aligned at the index nr. of each crate stack
data = [x.replace("    "," ").split(" ") for x in text.splitlines()[0:8]]
# Rotate the extracted list 90 deg clockwise to get a list of each stack
tmpCrates = np.rot90(np.flipud(np.fliplr(data)))

#create lists for manipulation by crane; remove all empty values
crates1 = []
crates2 = []
for data in tmpCrates:
    crates1.append(list(np.delete(data, np.where(data == ""))))
    crates2.append(list(np.delete(data, np.where(data == ""))))

#part 1
for instruction in instructions:
    # Get instruction set
    quantity, FromStack, ToStack = instruction

    # Place last crate of FromStack at the end of ToStack
    # Delete the moved crate fron FromStack
    for i in range(0,quantity):
        crates1[ToStack-1].append( crates1[FromStack-1][-1])
        del crates1[FromStack-1][-1]

#part 2
for instruction in instructions:
    # Get instruction set
    quantity, FromStack, ToStack = instruction

    # Get last x crates from FromStack
    temp = crates2[FromStack-1][-quantity:]
    # Place on ToStack
    crates2[ToStack-1].extend(temp)
    # Remove from old stack
    del crates2[FromStack-1][-quantity:]


solustion1 = ""
solustion2 = ""
for crate in crates1:
    solustion1 +=crate[-1].replace("[",'').replace("]",'')
for crate in crates2:
    solustion2 +=crate[-1].replace("[",'').replace("]",'')
print("Solution part 1 = ",solustion1)
print("Solution part 2 = ",solustion2)
print("--- %s millis ---" % ((time.time() - start_time) * 1000))