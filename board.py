import queue
import copy
import numpy as np
from itertools import count
from time import sleep


SIZE = 3

def h(n):

    #total manhattan dist of the board
    
    cost = 0
    
    for i in range(SIZE*SIZE):
        
        val = n.state[i // SIZE, i % SIZE]
        if val == 0:
            cost += abs(SIZE*SIZE // SIZE - i // SIZE) + abs(SIZE*SIZE % SIZE - i % SIZE)
        else:
            val -= 1
            cost += abs(val // SIZE - i // SIZE) + abs(val % SIZE - i % SIZE)

    # other heuristic, only checks positions
    
    """
    for i in range(16):
        val = n.state[i // 4, i % 4]
        if val == 0 and (i // 4, i % 4) != (3, 3):
            cost += 1
        elif val != i + 1:
            cost += 1
    """

    return cost


def g(n, cameFrom):

    #cost of the path from start position to current position

    pos = {}
    cost = 0

    """
    for i in range(16):
        
        pos[start.state[i // 4, i % 4]] = (i // 4, i % 4)

    for i in range(16):
        
        #compare start pos to current pos

        val = n.state[i // 4, i % 4]
        pos1, pos2 = pos[val]
        cost += abs(i // 4 - pos1) + abs(i % 4 - pos2)
    """

    i = 0
    node = n
    while(cameFrom[node] != None):
        node = cameFrom[node]
        i += 1
    
    return i

def solvable(state):

    #parity of the permutation
    test = copy.deepcopy(state)

    goal = [i for i in range(1, (SIZE*SIZE+1))]
    goal[SIZE*SIZE-1] = 0
    a = 0

    while not np.array_equal(test, goal):

        for i in range(SIZE*SIZE):

            if test[i] != goal[i]:

                for j in range(SIZE*SIZE):

                    if test[j] == goal[i]:

                        temp = test[j]
                        test[j] = test[i]
                        test[i] = temp
                        a += 1


    b = 0
    for i in range(SIZE*SIZE):
        if(state[i] == 0):
            b = abs(SIZE - i // SIZE) + abs(SIZE - i % SIZE)
            return (a % 2 + b % 2) % 2 == 0
    


    ############




class node(object):
    #board object w state

    state = None
    parent = None

    def __init__(self, board, parentNode):
        self.state = board
        parent = parentNode 

    def move(self, num, gScore):

        
        newState = copy.deepcopy(self.state)
        vals = self.validMove(num)

        if not vals['valid']:
            return None

        zero1, zero2 = vals['zero']
        num1, num2 = vals['num']

        newState[zero1, zero2] = num
        newState[num1, num2] = 0

        for prevNode in gScore.keys():
            if np.array_equal(newState, prevNode.state):
                return prevNode


        return node(newState, self)

    def validMove(self, num):
        
        zero = None
        numloc = None
        ret = {}

        for i in range(SIZE):
            for j in range(SIZE):
                if self.state[i][j] == 0:
                    zero = (i, j)
                if self.state[i][j] == num:
                    numloc = (i,j)
        
        if abs(numloc[0] - zero[0]) + abs(numloc[1] - zero[1]) == 1:
            ret["valid"] = True
        else:
            ret["valid"] = False

        ret["zero"] = zero
        ret["num"] = numloc

        return ret

        
#based on the a star pseudocode from Wikipedia
def astar(start, goal, h):
    
    #priority queue with starting node
    unique = count()


    openSet = queue.PriorityQueue()
    openSet.put((h(start), next(unique), start))

    inOpenSet = []
    inOpenSet.append(start)

    cameFrom = {}
    cameFrom[start] = None

    

    gScore = {}
    gScore[start] = 0

    fScore = {}
    fScore[start] = h(start)

    # You should only assign nodes if they are a new board state
    # also look into why the costs are so messed up

    
    a = 0

    while(not openSet.empty()):

        a += 1
        _, _, current = openSet.get()
        inOpenSet.remove(current)

        if np.array_equal(goal, current.state):
            print(current.state)
            print("FIN")
            print(a)
            return 1;
        
        if(h(current)) < 10:
            print(current.state)

        neighbors = []

        #find neighbors of current - assign prev gscore
        #if we already have them in map

        for i in range(SIZE*SIZE):

            

            newNode = current.move(i, gScore)

            #check if the move is valid
            if newNode is not None:
                
                #add neighbor
                
                neighbors.append(newNode)

                #if any node in cameFrom has the same state, assign
                #current to that node

                
                #initialize node values if its a new node
                if newNode not in gScore:
                    gScore[newNode] = 400000
                    fScore[newNode] = 400000
                    cameFrom[newNode] = current
                
                

        for neighbor in neighbors:

            
            tentative_gScore = g(current, cameFrom) + 1
            if tentative_gScore < gScore[neighbor]:
                
                gScore[neighbor] = tentative_gScore
                cameFrom[neighbor] = current
                fScore[neighbor] = gScore[neighbor] + h(neighbor) 
                
                
                
                if neighbor not in inOpenSet:
                    inOpenSet.append(neighbor)
                    openSet.put((fScore[neighbor], next(unique), neighbor))
                
    return False









                        


