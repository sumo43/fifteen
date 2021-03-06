#include <iostream>
#include <array>

using namespace std;
const int size = 4;

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

std::array <int, size*size> neighbors(std::ar)

std::array <int, size*size> randomSolvableState(int s)
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


