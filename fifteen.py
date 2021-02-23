import sys
from random import shuffle
from copy import copy
import queue

s = 3
large = 400000



#TODO
#can optimize by keeping track of the zero in the last line of the board
# find better way to implement cameFrom
#the boards should be sets

#TODO fix openset

def find_zero(state):

    e = list(state)

    for i in range(s*s):
        if e[i] == 0:
            return i

def pprint(state):

    for i in range(s):
            for item in state[i * s: i * s + s]:
                if item > 9:
                    print(item, " ", end="")
                else:
                    print(item, "  ", end="")
            
            print()


def neighbors(state, cameFrom):

    #since state is not a compound object, shallow copy works fine

    neighbors = []
    zero = find_zero(state)

    #try to safe access cameFrom dict before creating each new state
    if zero < s*(s-1):
        #swap with below
        newboard = list(state)

        temp = newboard[zero + s]
        newboard[zero + s] = newboard[zero]
        newboard[zero] = temp

        newboard = tuple(newboard)
        neighbors.append(newboard)

    if zero > s-1:
        #swap with above
        newboard = list(state)

        temp = newboard[zero - s]
        newboard[zero - s] = newboard[zero]
        newboard[zero] = temp

        newboard = tuple(newboard)
        neighbors.append(newboard)

    if zero % s > 0:
        #swap with left
        newboard = list(state)

        temp = newboard[zero - 1]
        newboard[zero - 1] = newboard[zero]
        newboard[zero] = temp

        newboard = tuple(newboard)
        neighbors.append(newboard)

    if zero % s < s-1:
        #swap with right
        newboard = list(state)

        temp = newboard[zero + 1]
        newboard[zero + 1] = newboard[zero]
        newboard[zero] = temp

        newboard = tuple(newboard)
        neighbors.append(newboard)


    return neighbors


def h(se):

    #total manhattan dist of the board
    state = list(se)
    
    cost = 0
    
    for i in range(s*s):
        
        val = state[i]

        if val == 0:
            cost += abs(s - 1 - (i // s)) + abs(s - 1 - (i % s))
        else:
            val -= 1
            cost += abs(val // s - i // s) + abs(val % s - i % s)

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


def random_state():

    nums = [i for i in range(s*s)]
    shuffle(nums)

    return nums


def solvable(state):

    #parity of the permutation
    #this is dumb

    goal = [i for i in range(1, (s*s+1))]
    goal[s*s-1] = 0

    a = 0

    while not state==goal:

        for i in range(s*s):

            if state[i] != goal[i]:

                for j in range(s*s):

                    if state[j] == goal[i]:

                        temp = state[j]
                        state[j] = state[i]
                        state[i] = temp
                        a += 1

    b = 0
    for i in range(s*s):
        if(state[i] == 0):
            b = abs(s - i // s) + abs(s - i % s)
            return (a % 2 + b % 2) % 2 == 0

def AStar(start):

    # goal state
    goal = [i for i in range(1, (s*s+1))]
    goal[s*s-1] = 0
    
    goal = tuple(goal)
    

    #test w goal, make openset and fscore work


    #For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    #to n currently known.
    openSet = []
    openSet.append(start)


    cameFrom = dict()
    cameFrom[start] = None

    #default value of infinity
    gScore = dict()
    gScore[start] = 0

    fScore = queue.PriorityQueue()
    # priority, data
    fScore.put((h(start), start)) 

    while(len(openSet) != 0):

        

        f, state = fScore.get()

        if state in openSet:
            openSet.remove(state)
        # take the lowe

        if state == goal:
            #implement win mechanics
            return state

        for neighbor in neighbors(state, cameFrom):

            tentative_gscore = gScore[state] + 1

   
            old_gscore = gScore.get(neighbor)
            if(old_gscore == None):
                old_gscore = large

            #you found a better path, record it
            if tentative_gscore < old_gscore:

                cameFrom[neighbor] = state
                gScore[neighbor] = tentative_gscore
                fScoreNeighbor = gScore[neighbor] + h(neighbor)

                if neighbor not in openSet:

                    openSet.append(state)
                    fScore.put((fScoreNeighbor, neighbor))

    return state

    
class game():
    
    def __init__(self):

        self.s = s

        self.state = random_state() 
        i= 0
        while not solvable(copy(self.state)):
            i+=1
            print(i)
            self.state = random_state()


        self.state = tuple(self.state)

        print(self.state)

        self.state = list(AStar(self.state))
        self.prints()


        

    def prints(self):

        print(h(self.state))

        for i in range(s):
            for item in  self.state[i * s: i * s + s]:
                if item > 9:
                    print(item, " ", end="")
                else:
                    print(item, "  ", end="")
            
            print()

    def solved(self):

        self.state = AStar(self.state)



a = game()    
    












