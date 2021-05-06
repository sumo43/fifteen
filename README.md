# fifteen

fifteen puzzle solver implementation 
https://docs.cs50.net/2016/ap/problems/fifteen/3/fifteen3.html

### Algorithm

I used an IDA* search algorithm to find a path to the goal state. The game states are represented as arrays, and the heuristic is the manhattan distance of each position in the state from its goal position. 
