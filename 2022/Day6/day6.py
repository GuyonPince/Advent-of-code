import time
start_time = time.time()

transmission = ""
with open("day6.txt") as file:
    transmission = file.read()

def findUnique_n(msg,n):
    for i in range(n,len(msg)):
        temp = set(msg[i-n:i])
        if len(temp) == n:
            return (i)

print ("Transmission Start found at: ",findUnique_n(transmission,4))
print ("Msg Start found at: ",findUnique_n(transmission,14))
print("--- %s millis ---" % ((time.time() - start_time) * 1000))