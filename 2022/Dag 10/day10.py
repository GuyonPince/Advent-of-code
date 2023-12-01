text = ""
with open("day10.txt") as file:
    text = file.read()

signal_strength = []
def check_cycle(cycle,value):
    global signal_strength
    cycle_list = [20,60,100,140,180,220]
    if cycle in cycle_list:
        signal_strength.append(cycle*value)
    return cycle+1

# part 1
value = 1
cycle = 1
for line in text.splitlines():
    if line.startswith('noop'):
        cycle = check_cycle(cycle,value) 
    else:
        cycle = check_cycle(cycle,value)
        cycle = check_cycle(cycle,value)  
        value += int(line.split()[-1])

print ("sum of signal strength = ", sum(signal_strength))

# Part 2
sprite = [0,1,2]
def update_sprite(index):
    _min,_max = [0,39]
    if index == _min:
        return [index,index+1]
    elif index == _max:
        return [index-1,index]
    else:
        return [index-1,index,index+1]

cycle_vals = []
x = 1
for line in text.splitlines():
    if line.startswith('noop'):
        cycle_vals.append(x)
    else:
        cycle_vals.append(x)
        cycle_vals.append(x)
        x += int(line.split()[-1])

print ('\n')
index = 0
for row in range(6):
    pixels = ''
    for col in range(40):
        sprite = update_sprite(cycle_vals[col+row*40])
        if col in sprite:
            pixels += "#"
        else:
            pixels += " "
    print(pixels)