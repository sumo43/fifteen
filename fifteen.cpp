#include <cstdlib>
#include <unistd.h>
#include "util.h" // utility function

// returns -1 if found, min otherwise

int search(vector<array<int, size*size> > &visited, vector<array<int, size*size> > &path, int g, int bound)
{
    
    array<int, size*size> node = path.back();
    
    int f = g + h(node);

    if(f > bound)
    {
        return f;
    }

    if (is_goal(node))
    {
        pprint(node);
        cout << h(node) << endl;
        return -1;
    }
    int min = 400000;

    vector< array<int, size*size> > succ = successors(node);

    for(int i = 0; i < succ.size(); i++)
    {
        if(!in(path, succ[i]) && !in(visited, succ[i]))
        {
            path.push_back(succ[i]);
            int t = search(visited, path, g + 1, bound);
            if(t == -1)
            {
                return -1;
            }
            if(t < min)
            {
                min = t;
            }
            path.pop_back();
        }
    
    }

    return min;

}

// IDA* Algorithm
// uses vector for path

vector <array<int, size*size> > IDAStar (array<int, size*size> start)
{

    vector<array<int, size*size> > path;
    vector<array<int, size*size> > visited;
    path.push_back(start);

    int bound = h(start);

    int t;
    
    while(true) {

        t = search(visited, path, 0, bound);

        if(t == -1)
        {
            return path;
        }
        
        if(t == 400000)
        {
            vector<array<int,size*size> > not_found;
            return not_found;
        }

        bound = t;
        
    }

    return path;
}

class Game
{
    private:
        array<int, size*size> state;
        int zeropos;

    public:
        Game() {
            state = randomSolvableState();

            zeropos = find_zero(state);
        }

        bool move(char m) {
            if(m == 'a') {
                if(zeropos % 4 == 0) {
                    return false;
                }
                else {
                    swap(state, zeropos, zeropos - 1);
                    return true;
                }

            }
            else if(m == 's') {
                if(zeropos > 11) {
                    return false;
                }
                else {
                    swap(state, zeropos, zeropos + 4);
                    return true;
                }
            }
            else if(m == 'w') {
                if(zeropos < 4) {
                    return false;
                }
                else {
                    swap(state, zeropos, zeropos - 4);
                    return true;
                }
            }
            else if(m == 'd') {
                if(zeropos % 4 == 3) {
                    return false;
                }
                else {
                    swap(state, zeropos, zeropos + 1);
                    return true;
                }
            }
            else if(m == 'G') {
                
                
                vector< array<int, size*size>> path = IDAStar(state);
                cout << path.size();
                for(int i = 0; i < path.size(); i++) {
                    pprint(path[i]);
                    usleep(100000);
                }
                

                return true;
            }


        }
     
        void run() {
            cout << "Game of Fifteen" << endl;
            char m;
            
            while(!is_goal(state)) {
                pprint(state);
                cout << "pick a move (w,a,s,d). G for god mode" << endl;
                cin >> m;
                while(!move(m)) {
                    cout << "invalid move, pick again" << endl;
                    cin >> m;
                }
                if(m == 'G') {
                    cout << "solved" << endl;
                    return;
                }
                zeropos = find_zero(state);
            }
            
        }

};

int main(int argc, char **argv)
{
    Game *g = new Game();
    g->run();
}
