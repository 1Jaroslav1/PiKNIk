#include <iostream>
using namespace std;

int main()
{
	// n - stopien, x - argument
    int n, x;
    cin >> n >> x;
 
    int arr[n+1];

    for (int i = n; i >= 0; --i)
        cin >> arr[i]; // wspolczyniki
    
    int s = arr[n];
    for (int i = 1; i <= n; i++)
    {
        s *= x;
        s += arr[n-i];
    }

    cout << s << endl;

    return 0;
}