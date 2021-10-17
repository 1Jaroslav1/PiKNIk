#include "iostream"
#include "vector"
using namespace std;

int main()
{

    long long m, n;
    cin >> m >> n;

    long long d;
    cin >> d;

    vector<vector<long long> > a(m, vector<long long> (n, 0));

    for(long long j = 0; j < d; j++){
        long long x, y;
        cin >> x >> y;

        a[x][y] += 1;
    }

    vector<vector<long long>> x(m, vector<long long> (n));
    vector<vector<string>> y(m, vector<string> (n));

    x[0][0] = a[0][0];
    y[0][0] = "";
    
    for(long long i = 1; i < n; i++)
    {
        x[0][i] = x[0][i-1] + a[0][i];
        y[0][i] = y[0][i-1] + "P";
    }

    for(long long i = 1; i < m; i++)
    {
        x[i][0] = x[i-1][0] + a[i][0];
        y[i][0] = y[i-1][0] + "D";
    }

    for(long long i = 1; i < m; i++)
    {
        for(long long j = 1; j < n; j++)
        {
            long long t = max(x[i-1][j],x[i][j-1]);
            x[i][j] = a[i][j] + t;
            if(t == x[i-1][j])
                y[i][j] = y[i-1][j] + "D";
            else
                y[i][j] = y[i][j-1] + "P";
        }
    }


    cout << x[m-1][n-1] << endl;
    cout << y[m-1][n-1] << endl;

    return 0;
}
