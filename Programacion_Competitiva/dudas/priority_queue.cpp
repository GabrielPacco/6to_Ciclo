#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

// Declaramos una cola de prioridad invertida
priority_queue<int, vector<int>, greater<int>> q;

int main( int argc, char *argv[] ) {
    
    q.push(1);
    q.push(2);
    q.push(3);
    q.push(4);
    q.push(5);
    q.push(6);
    q.push(7);
    q.push(8);
    q.push(9);
    q.push(10);
    
    while(!q.empty()) {
        cout << q.top() << endl;
        q.pop();
    }
    
    return 0;
}