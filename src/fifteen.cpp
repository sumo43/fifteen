#include <cstdlib>
#include "game.h"

//TODO 
//working fifteen puzzle with moves
//working solvable, gscore, hscore
//working continuity of cameFrom dictionary without scanning entire dictionary for matches
//working implementation of astar
//working implementation of idastar

using namespace std;

int main(int argc, char **argv)
{
    
    game newGame = game(4);
    newGame.printBoard();
    newGame.run();
}
