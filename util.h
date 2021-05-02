#include <iostream>
#include <array>
#include <algorithm>
#include <random>
#include <chrono>
#include <vector>
#include <stack>

using namespace std;
const int size = 4;

//TODO add dynamic sizing for print and array checks
//next project - pathfinder for maps
//re-implemet weighted sort for successors
//fix algorithm, try with linux cloud machine or something


//possible sources of error: h score, slow successors, 

//this is good

int g(vector<array<int, size*size> > path)
{
    return path.size();
}

int h(array<int, size*size> node)
{
    int cost = 0;

    for(int i = 0; i < size; i++) {
        for(int j = 0; j < size; j++) {
            int val = node[i * 4 + j];
            if(val == 0) {
                //distance from [3][3]
                cost += abs(3 - i) + abs(3 - j);
            }
            else {
                val -= 1;
                cost += abs((val / 4) - i) + abs((val % 4) - j);
            }
        }
    }

    return cost;
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

    return 0;
}

bool is_goal(array<int, size*size> state) {
    for(int i = 0; i < 15; i++) {
        if(state[i] != i + 1) return false;
    }
    if(state[15] != 0) return false;
    return true;
}

void swap(array<int, size*size >&state, int pos1, int pos2) {
    int temp = state[pos1];
    state[pos1] = state[pos2];
    state[pos2] = temp;
}

//lambda for comparing the h scores for each state

auto hLambda = [](array<int, size*size> &a, array<int, size*size> &b) -> bool
{
    return h(a) < h(b);
};


vector< array<int, size*size> > successors(array<int, size*size> state) {

    vector <array<int, size*size> > succ;
    int zeropos = find_zero(state);

    if(zeropos % 4 != 0) {
        array<int, size*size> temp = state;
        swap(temp, zeropos, zeropos - 1);
        succ.push_back(temp);
    }
    if(zeropos % 4 != 3) {
        array<int, size*size> temp = state;
        swap(temp, zeropos, zeropos + 1);
        succ.push_back(temp);
    }
    if(zeropos < 12) {
        array<int, size*size> temp = state;
        swap(temp, zeropos, zeropos + 4);
        succ.push_back(temp);
    }
    if(zeropos > 3) {
        array<int, size*size> temp = state;
        swap(temp, zeropos, zeropos - 4);
        succ.push_back(temp);
    }


    //implement the weighted sort again
    //when using sort with lambda, the smaller value according to the function comes first
    //order by g + h(node)

    sort(succ.begin(), succ.end(), hLambda);

    return succ;

}



//this is good



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
        bool zero_odd = zeropos > 11 || (zeropos > 3 && zeropos < 8);

        if((zero_odd && count % 2 == 0) || (!zero_odd && count % 2 == 1))
        {
            return false;
        }
    }

    return true;
}


//this is good

void pprint (array <int, size*size> state)
{

    for(int i = 0; i < size*size; i++)
    {


        if(i % 4 == 0 && i != 0)
        {
            cout << "\n";
        }
        if(state[i] > 9)
        {
            cout << state.at(i) << " ";
        }
        else
        {
            cout << state.at(i) << "  ";
        }

    }
    cout << endl;
    cout << endl;
    

} 

//this is fine
array <int, size*size> randomSolvableState()
{

    std::array <int, size*size> goalState;

    for(int i = 0; i < size*size; i++)
    {
        goalState[i] = i;
    }

    int seed = chrono::system_clock::now().time_since_epoch().count();
    shuffle(goalState.begin(), goalState.end(), std::default_random_engine(seed));
    /**
    while(!solvable(goalState)) {
        cout << "not solvable" << endl;
        seed = chrono::system_clock::now().time_since_epoch().count();
        shuffle(goalState.begin(), goalState.end(), std::default_random_engine(seed));
    }
    */

    return goalState;

}




int in(vector<array<int, size*size> > path, array<int, size*size> pos)
{
    int in = 0;
    for(array<int, size*size> node : path)
    {
        if(equal(begin(node), end(node), begin(pos)))
        {
            in++;
        }
    }
    return in != 0;
}

