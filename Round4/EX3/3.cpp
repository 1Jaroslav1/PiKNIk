#include <iostream>
#include <vector>
#include "math.h"
using namespace std;

#define INF 1000000000

int main() {
    int n, start, end;
    cin >> n >> start >> end;

    start--;
    end--;

    int count;
    cin >> count;
    
    vector<vector<int>> a(n, vector<int> (n, INF));
    for(int i = 0; i < count; i++){
        int x, y;
        cin >> x >> y;

        x--;
        y--;
        a[x][y] = 1;
    }

    for(int k = 0; k < n; k++){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                a[i][j] = min(a[i][j], a[i][k] + a[k][j]);  
            }
        }
    }
	
    if(a[start][end] < INF)
        cout << "TAK";
    else
        cout << "NIE";

    return 0;
}