import ast
import time

start_time = time.perf_counter()

text = ""
with open("day13.txt") as file:
    text = file.read()

def split_to_chunks(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

def compare(l1,l2):
    zipped = list(zip(l1,l2))
    for z in zipped:
        val1,val2 = z
        if any(isinstance(x,list) for x in z):
            val1,val2 = [[x] if isinstance(x,int) else x for x in z]
            if val1 == val2:
                continue # both lists are the same. Try next
            return compare(val1,val2)
        elif val1 < val2:
            return True # Packets are in the right order
        elif val1 > val2:
            return False # Packets are in the wrong order
        # values are the same, try the next values 
        
    if len(l1) > len(zipped):
        return False # list 2 ran out before list 1

    return True # list 1 ran out before list 2 

packets = [ast.literal_eval(x) for x in list(filter(lambda x: x != '' ,text.splitlines()))] 

# Part 1
idx_sum = 0
for idx,s in enumerate(list(split_to_chunks(packets,2))):
    if compare(s[0],s[1]):
        idx_sum += idx+1

print ('\nPart 1: Sum of indexes of sets that are in order =',idx_sum)
end_time = time.perf_counter()
print (f'---- duration = {end_time - start_time} seconds')

# Part 2, try 1
# Bubbel sorting the packets
start_time = time.perf_counter()

packets.extend([[[2]],[[6]]])
sorting = True
while sorting:
    packets_moved = False
    for idx,p in enumerate(packets):
        if idx == len(packets)-1:
            continue
        a = packets[idx]
        b = packets[idx+1]
        if not compare(a,b):
            packets_moved = True
            packets[idx] = b
            packets[idx+1] = a

    sorting = packets_moved

decoder_key = 1
for idx,p in enumerate(packets):
    if p in [[[2]],[[6]]]:
        decoder_key *= idx+1

print (f'\nPart 2: Bubbel sort decoder key = {decoder_key}')
end_time = time.perf_counter()
print (f'---- duration = {end_time - start_time} seconds')

# Part 2 try 2
# How many keys are above [[2]] and [[6]]
start_time = time.perf_counter()

key1 = 1
key2 = 2
for p in packets:
    key1 += compare(p,[[2]])
    key2 += compare(p,[[6]])

print (f'\nPart 2: Count how many are above decoder key = {key1 * key2}')
end_time = time.perf_counter()
print (f'---- duration = {end_time - start_time} seconds')
