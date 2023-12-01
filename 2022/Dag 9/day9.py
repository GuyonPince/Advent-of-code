import numpy as np

def calc_tail(head_pos,tail_pos):
    head_pos = np.array(head_pos)
    tail_pos = np.array(tail_pos)
    dif = np.subtract(head_pos,tail_pos)
    move = [0,0]
    if 2 in dif or -2 in dif:
        move = [val//2 if abs(val)>1 else val for val in dif]
    new_tail = np.add(move,tail_pos)

    return new_tail


text = ""
with open("day9.txt") as file:
    text = file.read()

commands = [line.split() for line in text.splitlines()]

dir = [0,0]
for opdr,segments in enumerate([2,10]):
    rope_parts = [[0,0]]*segments
    tail_end_positions = [[0,0]]

    for c in commands:
        steps = int(c[1])
        match c[0]:
            case 'L':
                dir = np.array([-1,0])
            case 'R':
                dir = np.array([1,0])
            case 'U':
                dir = np.array([0,-1])
            case 'D':
                dir = np.array([0,1])
        for step in range(steps):
            rope_parts[0] = np.add(rope_parts[0], dir)
            for idx,part in enumerate(rope_parts):
                rope_parts[idx+1] = calc_tail(part,rope_parts[idx+1])
                if idx == len(rope_parts)-2:
                    break

            if not(list(rope_parts[-1]) in tail_end_positions):
                    tail_end_positions.append(list(rope_parts[-1]))
            
    print (f'Part {opdr+1}, {segments} rope segemnts: The tail has reached {len(tail_end_positions)} diferent positions')


