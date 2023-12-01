import re
import numpy as np

text = ""
with open("day8.txt") as file:
    text = file.read()

forest1 = []
forest2 = []

for line in text.splitlines():
    forest1.append([[int(x),False] for x in list(line)])
    forest2.append([int(x) for x in list(line)])

forest1 = np.array(forest1)
forest2 = np.array(forest2)

#part 1
def countVisibleTrees():
    visible = 0
    for i in range(len(forest1)):
        highest = -1
        for j in range(len(forest1[i])):
            tree = forest1[i][j]
            if tree[0] > highest: 
                if tree[1] == False:
                    visible+=1
                    forest1[i][j] = [tree[0], True]
                highest = tree[0]
                
    return visible

#part 2
def scenicScore (pos_x,pos_y):
    temp_score = [0,0,0,0]
    value = forest2[pos_y][pos_x]
    # look to the right
    for i in range(pos_x+1,len(forest1[pos_y])):
        tree = forest2[pos_y][i]
        temp_score[0] += 1
        if tree >= value:
            break

    #look to the left
    for i in range(pos_x-1,-1,-1):
        tree = forest2[pos_y][i]
        temp_score[1] += 1
        if tree >= value:
            break

    #look down
    for i in range(pos_y+1,len(forest2)):
        tree = forest2[i][pos_x]
        temp_score[2] += 1
        if tree < value:
            if tree == value:break
        else: break

    #look up
    for i in range(pos_y-1,-1,-1):
        tree = forest2[i][pos_x]
        temp_score[3] += 1
        if tree >= value:
            break
    return np.prod(temp_score)


#part 1
visibleTreeCount = 0
for i in range(4):
    visibleTreeCount += countVisibleTrees()
    forest1 = np.rot90(forest1)
print ("part 1 = ", visibleTreeCount)

#part 2
highScore = 0
for pos_y,trees in enumerate(forest2):
    for pos_x,tree in enumerate(trees):
        score = scenicScore(pos_x,pos_y)
        if score > highScore:
            highScore = score
print ("part 2 = ", highScore)
