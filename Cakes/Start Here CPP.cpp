#include <iostream>
#include <cstdlib>
#include<string>
using namespace std;


int who = 0;

int main()
{
	cout << "\nWho is it?" << endl;
	
	cin >> who;
	
	switch (who)
	{
		case 7: cout << "\nWelcome, BossMan.\n";
		break;
		
		case 6: cout << "\nSorry this ain't Kansas.\n";
		break;
		
		case 1: cout << "\nYou ain't the boss o' me!\n";
		break;
		
		default: cout << "GTFO!\n";
	}
}
