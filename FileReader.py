import tkinter as tk
from tkinter import filedialog

#the file has to be a .txt

root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()
f = open(file)

field = []
foundG = False

#The state contains the x and y coordinate of the current position, the start and goal position, as well as the current path we are searching in
# state = ["x","y","startPosition","goalPosition","pathAsList"]
#"x", "y" and "pathAsList" are not relevant until future homework.
state = ['x', 'y', 'pathAsList']

#Parses every line from the .txt file into a list, so that we get a list of lists.
def parseEnv():
    for lines in f:
        print("Lines: " + lines.strip())
        field.append(lines.strip())

#Finds the "s" in the list of lists, by iterating over every character.
#The grid starts at the top left corner with [0,0].
def findStart():
    for i, lines in enumerate(field):
        for j, chars in enumerate(lines):
            if lines[j] == "s":
                global start
                start=[i,j]
                print("Start-position has been found at: {0}".format(start))
                state.insert(2, start)


#Finds the "g" in the list of lists, by iterating over every character.
#The grid starts at the top left corner with [0,0].
def findGoal():
    for i, lines in enumerate(field):
        for j, chars in enumerate(lines):
            if lines[j] == "g":
                global goal
                goal=[i,j]
                print("Goal-position has been found at: {0}".format(goal))
                state.insert(3, goal)


#Prints the current search state.
def printState():
    print(state)

"""
#4.1 Finds every node, that is available from the given node. A node is not available,
# if it is already in the set "visited" with every visited node.
#It looks for every node its direct neighbors.
def bfsNeighbors(x,y):
    global breadthFrontier
    global foundG
    global visited

    if field[x-1][y] != 'x' and [x-1,y] not in visited:
        if field[x-1][y] == 'g':
            foundG = True
            breadthFrontier.append([x-1,y])
            print("Goal found at " + str(x-1)+","+str(y))

        else:
            breadthFrontier.append([x-1,y])

    if field[x+1][y] != 'x' and [x+1,y] not in visited:
        if field[x+1][y] == 'g':
            foundG = True
            breadthFrontier.append([x+1,y])
            visited.append([x+1,y])
            print("Goal found at " + str(x+1)+","+str(y))
        else:
            breadthFrontier.append([x+1,y])
            visited.append([x+1,y])

    if field[x][y-1] != 'x' and [x,y-1] not in visited:
        if field[x][y-1] == 'g':
            foundG = True
            breadthFrontier.append([x,y-1])
            visited.append([x,y-1])
            print("Goal found at " + str(x)+","+str(y-1))
        else:
            breadthFrontier.append([x,y-1])
            visited.append([x,y-1])

    if field[x][y+1] != 'x':
        if field[x][y+1] == 'g' and [x,y+1] not in visited:
            foundG = True
            breadthFrontier.append([x,y+1])
            visited.append([x,y+1])
            print("Goal found at " + str(x)+","+str(y+1))
        else:
            breadthFrontier.append([x,y+1])
            visited.append([x,y+1])

    del breadthFrontier[0]

#breadthsearch first
#while g wasnt found and there are less than 200 loop runs, it calls the bfsNeighbors methode,
#which is looking for all possible neighbors.
#If a goal g was found, it prints the location.
def bfs(x,y):
    global visited
    visited = []
    global breadthFrontier
    breadthFrontier=[[x,y]]
    i = 0
    while not foundG and i < 500:
        print("Step " + str(i) + ": " + str(breadthFrontier))
        i += 1
        bfsNeighbors(breadthFrontier[0][0],breadthFrontier[0][1])

def hasBeenVisited(x,y):
    global visited
    if [x,y] not in visited:
        return True
    else:
        return False

"""

parseEnv()
findStart()
findGoal()
print(["x","y","startPosition","goalPosition","pathAsList"])
printState()