import sys
from random import shuffle
from copy import copy
import queue

s = 4
large = 400000



#TODO IDA

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


def neighbors(state):

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

    #SOLVABILITY
    # an inversion is when i < j but state[i] > state[j]
    #if n is odd, the number of inversions has to be even 
    #if n is even:
    # if number of inversions is even, the position of the zero is odd counting from bottom
    # if number of inversions is odd, the position of the zero is even from bottom

    count = 0

    for i in range(s*s):
        for j in range(s*s):
            if i < j and state[i] > state[j] and state[j] != 0:
                count += 1

    
    if s % 2 == 1:
        return count % 2 == 0
    
    else:

        zeropos = find_zero(state)
        zero_odd = zeropos > 11 or 3 < zeropos < 8
        
        if (zero_odd and count % 2 == 0) or (not zero_odd and count % 2 == 1):
            return True


#works for n < 4, too slow for n >= 4    

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

    
    # priority, state
    fScore = queue.PriorityQueue()
    fScore.put((h(start), start)) 

    while(len(openSet) != 0):


        f, state = fScore.get()
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

                    openSet.append(neighbor)
                    fScore.put((fScoreNeighbor, neighbor))

    return state

def IDAStar(start):

    #goal node
    goal = [i for i in range(1, (s*s+1))]
    goal[s*s-1] = 0
    goal = tuple(goal)

    #current search path (stack)
    #bound is the current threshold

    bound = h(start)
    path = [start]

    while True:
        t = search(path, 0, bound, goal)
        if t == 'FOUND':
            print("FOUND")
            return
        if t == large:
            print("NOT FOUND")
        bound = t

def successors(node, gscore):
    n = neighbors(node)
    return sorted(n, key=lambda node: gscore + h(node))

def search(path, gscore, bound, goal):

    node = path[-1]

    f = gscore + h(node)
    if f > bound:
        return f
    if node == goal:
        return 'FOUND'
    m = large
    n = successors(node, gscore)
    for succ in n:
        if succ not in path:
            path.append(succ)
            t = search(path, gscore + 1, bound, goal)
            if t == 'FOUND':
                return 'FOUND'
            if t < m:
                m = t
            path.pop(-1)
    
    return m

class game():
    
    def __init__(self):

        self.s = s
        

        self.state = random_state() 

        while not solvable(copy(self.state)):
            self.state = random_state()


        self.state = tuple(self.state)
        
        pprint(self.state)

        print(solvable((13,2,10,3,1,12,8,4,5,0,9,6,15,14,11,7)))

        self.state = (13,2,10,3,1,12,8,4,5,0,9,6,15,14,11,7)

        self.state = IDAStar(self.state)
        print(self.state)


        

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

        self.state = IDAStar(self.state)



a = game()    
    












