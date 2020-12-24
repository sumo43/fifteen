import numpy as np
from board import *
import random

SIZE = 3

def main():


    nums = [i for i in range(1, SIZE*SIZE+1)]
    nums[SIZE*SIZE-1] = 0

    goal = np.reshape(nums, (SIZE,SIZE))

    random.shuffle(nums)
    start = nums
    while not solvable(start):
        print("Not solvable")
        random.shuffle(start)
    
    print("Solvable")
    start = np.reshape(start, (SIZE,SIZE))

    start = node(start, None)


    astar(start, goal, h)
    
if __name__ == "__main__":
    main()
