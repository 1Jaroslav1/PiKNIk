#include "iostream"
#include "vector"
#include "math.h"
using namespace std;

void printArray(vector<vector<long long>> &a){
	long long n = a[0].size();
	for(long long i = 0; i < n; i++){
        for(long long j = 0; j < n; j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
}

long long findHeavierBranch(vector<vector<long long>> &tree){
    long long treeLength = tree[0].size();
    long long answer = tree[0][0];
    vector<vector<long long>> ansArray(treeLength, vector<long long> (treeLength));

    ansArray[0][0] = tree[0][0];
    for(long long i = 1; i < treeLength; i++){
        ansArray[i][0] = ansArray[i-1][0] + tree[i][0];
    }

    for(long long i = 1; i < treeLength; i++){
        for(long long j = 1; j < treeLength; j++){
            long long maxSum = max(ansArray[i-1][j-1], ansArray[i-1][j]);
            if(i == j){
            	maxSum = ansArray[i-1][j-1];
            }
            ansArray[i][j] = maxSum + tree[i][j];
        }
    }
    vector<long long> a = ansArray[treeLength-1];
    answer = a[0];
    for(long long e: a){
    	answer = max(answer, e);
    }
    return answer;
}

long long findEasierBranch(vector<vector<long long>> &tree){
    long long treeLength = tree[0].size();
    long long answer = tree[0][0];
    vector<vector<long long>> ansArray(treeLength, vector<long long> (treeLength));

    ansArray[0][0] = tree[0][0];
    for(long long i = 1; i < treeLength; i++){
        ansArray[i][0] = ansArray[i-1][0] + tree[i][0];
    }

    for(long long i = 1; i < treeLength; i++){
        for(long long j = 1; j < treeLength; j++){
            long long minSum = min(ansArray[i-1][j-1], ansArray[i-1][j]);
            if(i == j){
            	minSum = ansArray[i-1][j-1];
            }
            ansArray[i][j] = minSum + tree[i][j];
        }
    }
    vector<long long> a = ansArray[treeLength-1];
    answer = a[0];
    for(long long e: a){
    	answer = min(answer, e);
    }
    return answer;
}

vector<vector<long long>> inputVector(long long n){
    long long newElem;
    vector<vector<long long>> array(n, vector<long long> (n, 0));
    for(long long i = 0; i < n; i++){
        for(long long j = 0; j < n; j++){
            cin >> newElem;
            array[i][j] = newElem;
        }
    }
    return array;
}


int main(){
    long long n;
    cin >> n;

    vector<vector<long long>> array = inputVector(n);
    
    cout << "MAX: " << findHeavierBranch(array) << endl;
    cout << "MIN: " << findEasierBranch(array) << endl;
    return 0;
}