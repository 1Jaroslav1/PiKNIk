#include <iostream>
#include <Windows.h>
using namespace std;
void printB();
int alive();
char board[22][102];
char new_board[22][102];
void cond(int,int,int);
void reset();
void set();
void printN();

int main()
{
	for (int i = 0; i < 22; i++) {
		for (int j = 0; j < 102; j++) {
			if (i == 0 || i == 21 || j == 0 || j == 101) {
				board[i][j] = '#';
				new_board[i][j] = '#';
				cout << (board[i][j]);
				continue;
			}
			board[i][j] = '.';
			new_board[i][j] = '.';
			cout << (board[i][j]);
		}
		cout << endl;
	}

	cout << ("select presets 1-6: ");
	char a;
	cin >> a;
	if (a == '1') {
		board[10][50] = '@';
		board[10][51] = '@';
		board[10][52] = '@';
	}
	if (a == '2') {
		board[10][50] = '@';
		board[10][51] = '@';
		board[11][50] = '@';
		board[11][51] = '@';
	}
	
	if (a == '3') {
		board[10][50] = '@';
		board[11][51] = '@';
		board[11][52] = '@';
		board[11][50] = '@';
		board[10][51] = '@';
		board[12][49] = '@';
		board[12][48] = '@';
		board[12][47] = '@';
		board[12][46] = '@';
	}
	
	if (a == '4') {
		board[10][45] = '@';
		board[11][45] = '@';
		board[12][46] = '@';
		board[10][47] = '@';
		board[11][47] = '@';
		board[12][47] = '@';
	}
	
	if (a == '5') {
		board[10][50] = '@';
		board[10][49] = '@';
		board[11][50] = '@';
		board[9][50] = '@';
		board[19][51] = '@';

	}
	if (a == '6') {
		board[10][50] = '@';
		board[11][49] = '@';
		board[12][49] = '@';
		board[13][50] = '@';
		board[14][51] = '@';
		board[13][52] = '@';
		board[12][52] = '@';
		board[11][50] = '@';
		board[13][45] = '@';
		board[13][46] = '@';
		board[12][47] = '@';
		board[11][48] = '@';

		board[7][10] = '@';
		board[8][11] = '@';
		board[8][12] = '@';
		board[9][13] = '@';
		board[8][14] = '@';
		board[8][13] = '@';
		board[7][12] = '@';
		board[6][11] = '@';
		board[7][13] = '@';
		board[6][13] = '@';
		board[6][12] = '@';
		board[7][11] = '@';

	}

	
	set();
	while (alive()) {
		reset();
		printB();
	}
	
}

int alive() {
	
	int y = 0;
	for (int i = 1; i < 21; i++) {
		for (int j = 1; j < 101; j++) {
			
			int neighbours = 0;
				
				if (board[i-1][j - 1] == '@') {
					neighbours++;
				}
				if (board[i-1][j] == '@') {
					neighbours++;
				}
				if (board[i-1][j + 1] == '@') {
					neighbours++;
				}
				if (board[i][j - 1] == '@') {
					neighbours++;
				}
				if (board[i][j + 1] == '@') {
					neighbours++;
				}
				if (board[i+1][j-1] == '@') {
					neighbours++;
				}
				if (board[i+1][j] == '@') {
					neighbours++;
				}
				if (board[i+1][j + 1] == '@') {
					neighbours++;
				}
				if (board[i][j] == '@') {
					y++;
				}
				cond(neighbours, i, j);
		}
	}
	if (y == 0) {
		return 0;
	}
	return 1;
}

void printB() {
	system("cls");
	for (int i = 0; i < 22; i++) {
		for (int j = 0; j < 102; j++) {
			cout << (board[i][j]);
		}
		cout << endl;
	}
	Sleep(500);
}

void cond(int x,int I,int J) {
	if (x != 2 && x != 3) {
		new_board[I][J] = '.';
	}
	if (board[I][J] == '.' && x==3) {
		new_board[I][J] = '@';
	}
}

void set() {
	for (int i = 0; i < 22; i++) {
		for (int j = 0; j < 102; j++) {
			new_board[i][j] = board[i][j];
		}
	}
}

void reset() {
	for (int i = 0; i < 22; i++) {
		for (int j = 0; j < 102; j++) {
			board[i][j] = new_board[i][j];
		}
	}
}

/*void cond(int x,int I,int J) {
	if (x != 2 && x != 3) {
		board[I][J] = '.';
	}
	if (board[I][J] == '.' && x==3) {
		board[I][J] = '@';
	}
}*/

void printN() {
	system("cls");
	for (int i = 0; i < 22; i++) {
		for (int j = 0; j < 102; j++) {
			cout << (new_board[i][j]);
		}
		cout << endl;
	}
	Sleep(100);
}