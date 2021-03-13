#include <iostream>
#include <array>

//TODO                                                                                                                                                                                                     
//working fifteen puzzle with moves
//working solvable, gscore, hscore
//working cameFrom
//working astar
//working astar



using namespace std;
const int size = 4;



bool solvable(array<int, size*size> state)
{
    int count = 0;
    
    for (int i = 0; i < size*size; i++)
    {
        for(int j = 0; j < size*size; j++)
        {
            if (i < j && state[i] > state[j] && state[j] != 0)
            {
                count++;
            }
        }
    }

    if (size % 2 == 1)
    {
        return count % 2 == 0;
    }

    else
    {
        //fix positions
        int zeropos = find_zero(state);
        zero_odd = zero_pos > 11 || (zeropos > 3 && zeropos < 8);

        if((zero_odd && count % 2 == 0) || (!zero_odd && count % 2 == 1)
        {
            return true;
        }
    }
}





int find_zero(array <int, size*size> state)
{
    for (int i = 0; i < size * size; i++)
    {
        if (state[i] == 0)
        {
            return i;
        }
    }
}

void pprint (array <int, size*size> state)
{
    for (int i = 0; i < size*size; i++)
    {

        if(state[i] > 9)
        {
            printf("%i ", i);
        }
        else
        {
            printf("%i  ", i);
        }

        if(i % 4 == 0)
        {
            printf("\n");
            
        }
    }

}


array <int, size*size> randomSolvableState(int s)
{

    std::array <int, size*size> goalState;

    for(int i = 0; i < size*size; i++)
    {
        goalState[i] = i+1;
    }
    goalState[size*size-2] = 0;


    return goalState;

}

class game
{

    public:

        std::array <int, size*size> board;

        game(int s)
        {
            board = randomSolvableState(s);
        }

        void printBoard()
        {
            for(int i = 0; i < 16; i++)
            {
                printf("%i ", board[i]);
                if (i % 4 == 0 && i > 0)
                {
                    printf("\n");
                }
            }
        }

        void run()
        {
            bool end = false;

            while (!end)
            {
                
                this->printBoard();
                printf("pick number to move, type e to end");

                char move;
                cin >> move;

                if (move == 'e')
                {
                    return;
                }


            }
        }
};


