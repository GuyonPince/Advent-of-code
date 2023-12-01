#2nd try
import time
start_time = time.time()
score_matrix = [[1,2,0],[0,1,2],[2,0,1]]
p0 = ["A","B","C"]
p1 = ["X","Y","Z"]

def calc_1(line):
    i,j = line.split()
    sub_score1 = score_matrix[p0.index(i)][p1.index(j)] * 3
    sub_score2 = p1.index(j) + 1
    score = sub_score1 + sub_score2
    return score

def calc_2(line):
    i,j = line.split()
    sub_score1 = p1.index(j)
    sub_score2 = score_matrix[p0.index(i)].index(sub_score1) + 1
    score = sub_score1 * 3 + sub_score2
    return score

score1M = 0
score2M = 0
with open("day2.txt") as file:
    for line in file:
       #score1 += calc_score1(line)
       #score2 += calc_score2(line)
       score1M += calc_1(line)
       score2M += calc_2(line)

print("Part 1 matrix = ", score1M)
print("Part 2 matrix = ", score2M)
print("--- %s seconds ---" % (time.time() - start_time))

