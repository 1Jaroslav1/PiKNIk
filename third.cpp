#include "iostream"
#include "vector"
#include "math.h"
#include "string"
using namespace std;


string findHeavierBranch(vector<vector<long long>> &tree){
    long long treeLength = tree[0].size();
    long long answer = tree[0][0];
    vector<vector<long long>> ansArray(treeLength, vector<long long> (treeLength));
    vector<vector<string>> path(treeLength, vector<string> (treeLength));

    ansArray[0][0] = tree[0][0];
    path[0][0] = to_string(tree[0][0]);
    for(long long i = 1; i < treeLength; i++){
        ansArray[i][0] = ansArray[i-1][0] + tree[i][0];
        path[i][0] = path[i-1][0] + "-> " + to_string(tree[i][0]);
    }

    for(long long i = 1; i < treeLength; i++){
        for(long long j = 1; j < treeLength; j++){
            long long maxSum;
            string maxPath;
            if(ansArray[i-1][j-1] < ansArray[i-1][j]){
                maxSum = ansArray[i-1][j];
                maxPath = path[i-1][j];
            }
            else{
                maxSum = ansArray[i-1][j-1];
                maxPath = path[i-1][j-1];
            }

            if(i == j){
            	maxSum = ansArray[i-1][j-1];
            }
            ansArray[i][j] = maxSum + tree[i][j];
            path[i][j] = maxPath + "-> " + to_string(tree[i][j]);
        }
    }
    vector<long long> a = ansArray[treeLength-1];
    answer = a[0];
    long long index = 0;
    for(long long i = 1; i < treeLength; i++){
    	if(answer < a[i]){
            answer = a[i];
            index = i;
        }
    }
    return path[treeLength-1][index];
}

string findEasierBranch(vector<vector<long long>> &tree){
    long long treeLength = tree[0].size();
    long long answer = tree[0][0];
    vector<vector<long long>> ansArray(treeLength, vector<long long> (treeLength));
    vector<vector<string>> path(treeLength, vector<string> (treeLength));

    ansArray[0][0] = tree[0][0];
    path[0][0] = to_string(tree[0][0]);
    for(long long i = 1; i < treeLength; i++){
        ansArray[i][0] = ansArray[i-1][0] + tree[i][0];
        path[i][0] = path[i-1][0] + "-> " + to_string(tree[i][0]);
    }

    for(long long i = 1; i < treeLength; i++){
        for(long long j = 1; j < treeLength; j++){
            long long minSum;
            string minPath;
            if(ansArray[i-1][j-1] > ansArray[i-1][j]){
                minSum = ansArray[i-1][j];
                minPath = path[i-1][j];
            }
            else{
                minSum = ansArray[i-1][j-1];
                minPath = path[i-1][j-1];
            }

            if(i == j){
            	minSum = ansArray[i-1][j-1];
            }
            ansArray[i][j] = minSum + tree[i][j];
            path[i][j] = minPath + "-> " + to_string(tree[i][j]);
        }
    }
    vector<long long> a = ansArray[treeLength-1];
    answer = a[0];
    long long index = 0;
    for(long long i = 1; i < treeLength; i++){
    	if(answer > a[i]){
            answer = a[i];
            index = i;
        }
    }
    return path[treeLength-1][index];
}

vector<vector<long long>> inputVector(long long n){
    long long newElem;
    vector<vector<long long>> array(n, vector<long long> (n, 0));
    for(long long i = 0; i < n; i++){
        for(long long j = 0; j < i+1; j++){
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